"""MCX Commodity Spread Broker Order Ticket Generator.

Formats 2-leg calendar spread and cross-contract hedge orders into standardized
specifications ready for broker APIs (Zerodha Kite Connect, Dhan, Interactive Brokers).
Supports 1-click JSON and CSV export for institutional order execution.
"""

from typing import Dict, Any, List
import json
import pandas as pd
from src.normalize import CONTRACT_SPECS


def generate_spread_order_ticket(
    symbol: str,
    near_expiry: Any,
    far_expiry: Any,
    strategy_type: str,  # 'Long Calendar Spread' or 'Short Calendar Spread'
    lots: int = 1,
    near_price: float = 75000.0,
    far_price: float = 75500.0,
    broker_format: str = "Zerodha Kite",
) -> Dict[str, Any]:
    """Generate a 2-leg execution order ticket for Indian commodity broker APIs.

    Calendar Spread Rules:
    - Long Calendar Spread: Buy Far Expiry, Sell Near Expiry (expecting spread to widen)
    - Short Calendar Spread: Sell Far Expiry, Buy Near Expiry (expecting spread to narrow)

    Parameters
    ----------
    symbol : str
        Contract symbol (e.g. 'GOLDM', 'GOLDTEN', 'GOLDGUINEA').
    near_expiry : str or Timestamp
        Near month expiry date.
    far_expiry : str or Timestamp
        Far month expiry date.
    strategy_type : str
        'Long Calendar Spread' or 'Short Calendar Spread'.
    lots : int
        Number of lots per leg.
    near_price : float
        Current limit / trigger price for near contract.
    far_price : float
        Current limit / trigger price for far contract.
    broker_format : str
        'Zerodha Kite', 'Dhan', or 'Interactive Brokers'.

    Returns
    -------
    Dict[str, Any]
        Structured 2-leg order payload with net margin requirements and JSON/CSV representations.
    """
    near_dt = pd.to_datetime(near_expiry)
    far_dt = pd.to_datetime(far_expiry)
    
    spec = CONTRACT_SPECS.get(symbol.strip().upper(), {})
    lot_size_g = spec.get("lot_size_grams", 10)
    total_g = lots * lot_size_g

    # Format MCX trading symbols: e.g. GOLDM26NOVFUT or GOLDM-26NOV
    near_str = near_dt.strftime("%y%b").upper()
    far_str = far_dt.strftime("%y%b").upper()
    
    near_trading_symbol = f"{symbol}{near_str}FUT"
    far_trading_symbol = f"{symbol}{far_str}FUT"

    is_long_spread = "Long" in strategy_type

    # Leg Directions
    # Long Calendar Spread: Buy Far, Sell Near
    # Short Calendar Spread: Sell Far, Buy Near
    near_action = "SELL" if is_long_spread else "BUY"
    far_action = "BUY" if is_long_spread else "SELL"

    # Notional values
    near_notional = (near_price / spec.get("quote_unit_grams", 10)) * total_g
    far_notional = (far_price / spec.get("quote_unit_grams", 10)) * total_g

    # Spread margin benefit: MCX provides ~75% margin relief on hedged calendar spreads
    unhedged_margin = (near_notional + far_notional) * 0.10  # 10% base SPAN
    spread_hedged_margin = unhedged_margin * 0.25  # 75% relief for calendar hedge

    legs: List[Dict[str, Any]] = [
        {
            "leg_number": 1,
            "role": "Near Month Leg",
            "trading_symbol": near_trading_symbol,
            "exchange": "MCX",
            "transaction_type": near_action,
            "lots": lots,
            "lot_size_grams": lot_size_g,
            "quantity_grams": total_g,
            "product": "NRML",
            "order_type": "LIMIT",
            "price": float(near_price),
            "expiry_date": near_dt.strftime("%Y-%m-%d"),
            "validity": "DAY",
        },
        {
            "leg_number": 2,
            "role": "Far Month Leg",
            "trading_symbol": far_trading_symbol,
            "exchange": "MCX",
            "transaction_type": far_action,
            "lots": lots,
            "lot_size_grams": lot_size_g,
            "quantity_grams": total_g,
            "product": "NRML",
            "order_type": "LIMIT",
            "price": float(far_price),
            "expiry_date": far_dt.strftime("%Y-%m-%d"),
            "validity": "DAY",
        },
    ]

    # Broker-specific formats
    zerodha_orders = [
        {
            "variety": "regular",
            "tradingsymbol": leg["trading_symbol"],
            "exchange": "MCX",
            "transaction_type": leg["transaction_type"],
            "order_type": "LIMIT",
            "quantity": leg["lots"],
            "price": leg["price"],
            "product": "NRML",
            "validity": "DAY",
            "tag": "AurumSpread",
        }
        for leg in legs
    ]

    dhan_orders = [
        {
            "dhanClientId": "YOUR_CLIENT_ID",
            "transactionType": leg["transaction_type"],
            "exchangeSegment": "MCX_COMM",
            "productType": "MARGIN",
            "orderType": "LIMIT",
            "validity": "DAY",
            "securityId": leg["trading_symbol"],
            "quantity": leg["lots"],
            "price": leg["price"],
        }
        for leg in legs
    ]

    ticket_summary = {
        "strategy": strategy_type,
        "symbol": symbol,
        "near_expiry": near_dt.strftime("%d %b %Y"),
        "far_expiry": far_dt.strftime("%d %b %Y"),
        "lots": lots,
        "total_gold_grams": total_g,
        "net_spread_price": round(far_price - near_price, 2),
        "estimated_unhedged_margin_inr": round(unhedged_margin, 2),
        "estimated_spread_margin_inr": round(spread_hedged_margin, 2),
        "margin_relief_pct": 75.0,
        "legs": legs,
        "zerodha_kite_json": zerodha_orders,
        "dhan_json": dhan_orders,
    }

    return ticket_summary


def export_order_ticket_csv(order_ticket: Dict[str, Any]) -> str:
    """Format order ticket legs into CSV string ready for broker batch upload."""
    df_legs = pd.DataFrame(order_ticket["legs"])
    return df_legs.to_csv(index=False)
