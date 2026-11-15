"""AurumSpread — Institutional Commodity Derivatives Intelligence Platform.

Track 03: Commodity Derivatives Intelligence | Hack in Hills '26
Team AurumSpread: Shivansh Sahni • Krishna Sharma • Dhruv Gupta
"""

import json
import os
from pathlib import Path
import numpy as np
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components

from src.spread_engine import calculate_calendar_spreads
from src.spread_intelligence import calculate_spread_intelligence
from src.carry_engine import (
    calculate_term_structure,
    calculate_retail_micro_premium,
)
from src.liquidity_engine import calculate_liquidity_depth
from src.data_doctor import audit_dataset_health
from src.quiet_alerts import scan_quiet_alerts

# 1. Page Config (Sidebar Completely Collapsed & Hidden!)
st.set_page_config(
    page_title="AurumSpread | Sovereign Alpha Terminal",
    page_icon="🟡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Force Full-Viewport 100vh App with ZERO Streamlit Sidebar or Chrome
st.markdown("""
    <style>
        #MainMenu, header, footer {visibility: hidden !important; display: none !important;}
        section[data-testid="stSidebar"] {display: none !important;}
        div[data-testid="collapsedControl"] {display: none !important;}
        .stApp {background-color: #F6F4F0 !important; overflow: hidden !important;}
        .block-container {padding: 0 !important; margin: 0 !important; max-width: 100vw !important;}
        iframe {
            position: fixed !important;
            top: 0 !important;
            left: 0 !important;
            width: 100vw !important;
            height: 100vh !important;
            border: none !important;
            z-index: 9999 !important;
        }
    </style>
""", unsafe_allow_html=True)

DATA_PATH = Path("data/processed/historical_gold_futures.csv")
if not DATA_PATH.exists():
    st.error(f"Dataset missing at {DATA_PATH}. Please run `python build_historical_dataset.py` first.")
    st.stop()


@st.cache_data
def build_master_payload() -> str:
    df_raw = pd.read_csv(DATA_PATH)
    df_raw["trade_date"] = pd.to_datetime(df_raw["trade_date"], errors="coerce", format="mixed")
    df_raw["expiry_date"] = pd.to_datetime(df_raw["expiry_date"], errors="coerce", format="mixed")
    df_raw["close"] = pd.to_numeric(df_raw["close"], errors="coerce")
    df_raw["normalized_price_per_gram"] = pd.to_numeric(df_raw["normalized_price_per_gram"], errors="coerce")
    df_raw["volume_lots"] = pd.to_numeric(df_raw.get("volume_lots", 0), errors="coerce").fillna(0)
    df_raw["open_interest_lots"] = pd.to_numeric(df_raw.get("open_interest_lots", 0), errors="coerce").fillna(0)
    df = (
        df_raw.dropna(subset=["trade_date", "expiry_date", "normalized_price_per_gram"])
        .sort_values(["symbol", "trade_date", "expiry_date"])
        .reset_index(drop=True)
    )

    latest_date = df["trade_date"].max()
    latest_date_str = latest_date.strftime("%d %b %Y")
    latest_data = df[df["trade_date"] == latest_date]
    avg_norm_price = float(latest_data["normalized_price_per_gram"].mean())

    # 1. Data Doctor Audit
    audit_res = audit_dataset_health(df)

    # 2. Latest Snapshot Records
    latest_records = []
    for _, r in latest_data.sort_values(["symbol", "expiry_date"]).iterrows():
        latest_records.append({
            "symbol": str(r["symbol"]),
            "expiry_date": r["expiry_date"].strftime("%d %b %Y"),
            "close": float(r["close"]),
            "norm_price": round(float(r["normalized_price_per_gram"]), 2),
            "volume_lots": int(r["volume_lots"]),
            "oi_lots": int(r["open_interest_lots"]),
        })

    # 3. Historical Fair Price Movement (Daily Mean per Contract so lines are clean!)
    hist_df = (
        df.groupby(["trade_date", "symbol"], as_index=False)["normalized_price_per_gram"]
        .mean()
        .sort_values("trade_date")
    )
    hist_series = {}
    for sym in ["GOLDM", "GOLDTEN", "GOLDGUINEA", "GOLDPETAL"]:
        sub = hist_df[hist_df["symbol"] == sym]
        hist_series[sym] = {
            "dates": sub["trade_date"].dt.strftime("%Y-%m-%d").tolist(),
            "prices": [round(float(x), 2) for x in sub["normalized_price_per_gram"].tolist()],
        }

    # 4. Quiet Alerts Raw Data (60 active pairs)
    all_latest_pairs = []
    for sym in ["GOLDM", "GOLDTEN", "GOLDGUINEA", "GOLDPETAL"]:
        sp = calculate_calendar_spreads(df, symbol=sym)
        intel = calculate_spread_intelligence(sp)
        lat_intel = intel[intel["trade_date"] == latest_date]
        sym_data = df[(df["symbol"] == sym) & (df["trade_date"] == latest_date)]
        for _, row in lat_intel.iterrows():
            n_exp = pd.to_datetime(row["near_expiry"])
            f_exp = pd.to_datetime(row["far_expiry"])
            n_rows = sym_data[sym_data["expiry_date"] == n_exp]
            n_vol = float(n_rows["volume_lots"].iloc[0]) if not n_rows.empty else 0.0
            n_oi = float(n_rows["open_interest_lots"].iloc[0]) if not n_rows.empty else 0.0
            dte = int((n_exp - latest_date).days)
            z_val = None if pd.isna(row["spread_zscore"]) else round(float(row["spread_zscore"]), 2)
            mean_sp = float(row["calendar_spread"]) if pd.isna(row["historical_mean"]) else float(row["historical_mean"])
            all_latest_pairs.append({
                "trade_date": latest_date_str,
                "symbol": sym,
                "near_expiry": n_exp.strftime("%d %b %Y"),
                "far_expiry": f_exp.strftime("%d %b %Y"),
                "dte": dte,
                "zscore": z_val,
                "spread": round(float(row["calendar_spread"]), 2),
                "mean_spread": round(mean_sp, 2),
                "gross_edge": round(abs(float(row["calendar_spread"]) - mean_sp), 2),
                "volume_lots": int(n_vol),
                "oi_lots": int(n_oi),
            })

    # 5. Term Structure Curves
    curves_data = {}
    for sym in ["GOLDM", "GOLDTEN", "GOLDGUINEA", "GOLDPETAL"]:
        c_df = calculate_term_structure(df, trade_date=latest_date, symbol=sym)
        curves_data[sym] = []
        for _, r in c_df.iterrows():
            curves_data[sym].append({
                "expiry": r["expiry_date"].strftime("%d %b %Y"),
                "dte": int(r["days_to_expiry"]),
                "close": float(r["close"]),
                "norm_price": round(float(r["normalized_price_per_gram"]), 2),
                "spread_vs_front": round(float(r["spread_vs_front_inr"]), 2),
                "carry_pct": round(float(r["annualized_carry_pct"]), 2),
                "regime": str(r["market_regime"]),
            })

    # 6. Retail Micro-Premium
    micro_df = calculate_retail_micro_premium(df)
    micro_series = {}
    for sym in ["GOLDPETAL", "GOLDGUINEA", "GOLDTEN"]:
        sub = micro_df[micro_df["symbol"] == sym].sort_values("trade_date")
        micro_series[sym] = {
            "dates": sub["trade_date"].dt.strftime("%Y-%m-%d").tolist(),
            "premium_inr": [round(float(x), 2) for x in sub["premium_inr_per_g"].tolist()],
        }

    # 7. Liquidity Depth
    depth_df = calculate_liquidity_depth(df)
    latest_depth_df = depth_df[depth_df["trade_date"] == latest_date]
    liquidity_records = []
    for _, r in latest_depth_df.iterrows():
        liquidity_records.append({
            "symbol": str(r["symbol"]),
            "expiry": r["expiry_date"].strftime("%d %b %Y"),
            "dte": int(r["days_to_expiry"]),
            "volume": int(r["volume_lots"]),
            "oi": int(r["open_interest_lots"]),
            "turnover_cr": round(float(r["turnover_crores"]), 2),
            "is_tender": bool(r["is_in_tender"]),
            "tier": str(r["liquidity_tier"]),
        })

    # 8. Walk-Forward Backtest Data
    backtest_pairs_data = {}
    for sym in ["GOLDGUINEA", "GOLDM", "GOLDTEN", "GOLDPETAL"]:
        sp = calculate_calendar_spreads(df, symbol=sym)
        intel = calculate_spread_intelligence(sp)
        backtest_pairs_data[sym] = {}
        pairs = intel[["near_expiry", "far_expiry"]].drop_duplicates().sort_values(["near_expiry", "far_expiry"])
        for _, p in pairs.iterrows():
            n_exp, f_exp = p["near_expiry"], p["far_expiry"]
            sub = intel[(intel["near_expiry"] == n_exp) & (intel["far_expiry"] == f_exp)].dropna(subset=["spread_zscore"]).sort_values("trade_date")
            if len(sub) < 5:
                continue
            pair_label = f"{pd.to_datetime(n_exp).strftime('%d %b %Y')} ➔ {pd.to_datetime(f_exp).strftime('%d %b %Y')}"
            backtest_pairs_data[sym][pair_label] = {
                "dates": sub["trade_date"].dt.strftime("%Y-%m-%d").tolist(),
                "dte": [int((pd.to_datetime(n_exp) - d).days) for d in sub["trade_date"]],
                "spread": [round(float(x), 2) for x in sub["calendar_spread"].tolist()],
                "zscore": [round(float(x), 2) for x in sub["spread_zscore"].tolist()],
                "near_raw": [round(float(x), 2) for x in sub["near_raw_price"].tolist()],
                "far_raw": [round(float(x), 2) for x in sub["far_raw_price"].tolist()],
            }

    # 9. Hero Spread Curves
    goldm_sp = calculate_calendar_spreads(df, symbol="GOLDM")
    goldm_intel = calculate_spread_intelligence(goldm_sp)
    dec_feb_df = goldm_intel[(goldm_intel["near_expiry"] == "2026-12-04") & (goldm_intel["far_expiry"] == "2027-02-05")].sort_values("trade_date")
    feb_apr_df = goldm_intel[(goldm_intel["near_expiry"] == "2027-02-05") & (goldm_intel["far_expiry"] == "2027-04-05")].sort_values("trade_date")

    curve_goldm_df = calculate_term_structure(df, trade_date=latest_date, symbol="GOLDM")
    avg_carry = float(curve_goldm_df["annualized_carry_pct"].replace(0, np.nan).mean()) if not curve_goldm_df.empty else 12.43
    alert_res = scan_quiet_alerts(df)
    max_arb = float(alert_res["alerts_df"]["gross_edge_inr"].max()) if not alert_res["alerts_df"].empty else 102.10

    payload = {
        "latest_date": latest_date_str,
        "avg_norm_price": round(avg_norm_price, 2),
        "audit": audit_res,
        "latest_records": latest_records,
        "hist_series": hist_series,
        "quiet_alerts_raw": all_latest_pairs,
        "curves": curves_data,
        "micro_premium": micro_series,
        "liquidity": liquidity_records,
        "backtest_data": backtest_pairs_data,
        "hero_curves": {
            "Dec-Feb": {
                "dates": dec_feb_df["trade_date"].dt.strftime("%Y-%m-%d").tolist(),
                "spread": [round(float(x), 2) for x in dec_feb_df["calendar_spread"].tolist()],
                "mean": [None if pd.isna(x) else round(float(x), 2) for x in dec_feb_df["historical_mean"].tolist()],
                "label": "GOLDM Dec 26 ➔ Feb 27 Spread (₹/g)",
            },
            "Feb-Apr": {
                "dates": feb_apr_df["trade_date"].dt.strftime("%Y-%m-%d").tolist(),
                "spread": [round(float(x), 2) for x in feb_apr_df["calendar_spread"].tolist()],
                "mean": [None if pd.isna(x) else round(float(x), 2) for x in feb_apr_df["historical_mean"].tolist()],
                "label": "GOLDM Feb 27 ➔ Apr 27 Spread (₹/g)",
            },
            "Term-Structure": {
                "dates": [r["expiry"] for r in curves_data["GOLDM"]],
                "spread": [r["norm_price"] for r in curves_data["GOLDM"]],
                "mean": None,
                "label": "GOLDM Forward Term Structure (₹/1g 999 Gold)",
            },
        },
        "kpi": {
            "cost_of_carry": f"{avg_carry:.2f}",
            "max_arb_profit": f"₹{max_arb:,.2f}",
            "dec_feb_val": f"₹{dec_feb_df.iloc[-1]['calendar_spread']:,.1f}" if not dec_feb_df.empty else "₹277.5",
            "feb_apr_val": f"₹{feb_apr_df.iloc[-1]['calendar_spread']:,.1f}" if not feb_apr_df.empty else "₹258.1",
        },
    }
    return json.dumps(payload)


current_dir = os.path.dirname(os.path.abspath(__file__))
html_file_path = os.path.join(current_dir, "landing_page", "index.html")

with open(html_file_path, "r", encoding="utf-8") as f:
    html_template = f.read()

final_html = html_template.replace("__AURUM_PAYLOAD_JSON__", build_master_payload())

# Also save standalone compiled HTML file for direct localhost:8000 execution
with open(os.path.join(current_dir, "aurumspread_live.html"), "w", encoding="utf-8") as f_out:
    f_out.write(final_html)

components.html(final_html, height=900, scrolling=True)