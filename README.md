# 🟡 AurumSpread
<<<<<<< HEAD
### Commodity Derivatives Intelligence Platform for MCX Gold Futures
**Hack in Hills '26** | **Track 03: Commodity Derivatives Intelligence**

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Tests](https://img.shields.io/badge/pytest-23%20passed-brightgreen.svg)]()
[![Platform](https://img.shields.io/badge/dashboard-Streamlit-orange.svg)]()
[![MCX Data](https://img.shields.io/badge/data-MCX%20Bhavcopy-yellow.svg)]()
=======
### Commodity Derivatives Intelligence & Execution Platform for MCX Bullion Futures
**Hack in Hills '26** | **Track 03: Commodity Derivatives Intelligence** | **Final Round**

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Tests](https://img.shields.io/badge/pytest-26%20passed-brightgreen.svg)]()
[![Platform](https://img.shields.io/badge/dashboard-Streamlit-orange.svg)]()
[![MCX Data](https://img.shields.io/badge/data-MCX%20Bhavcopy-yellow.svg)]()
[![Commodity](https://img.shields.io/badge/universe-Gold%20%26%20Silver-gold.svg)]()
>>>>>>> 89235d3b588cfa496b409f8ec238c511a4fd88b1

---

## 👥 Team AurumSpread

| Team Member | Role | Core Deliverables |
|---|---|---|
<<<<<<< HEAD
| **Shivansh Sahni** | Data & Python Backend | MCX Bhavcopy ingestion, symbol trimming, date validation, and ₹/1g 999 gold normalization. |
| **Krishna Sharma** | Quant Logic & Backtesting | Day-by-day walk-forward simulator, cost-of-carry decomposition, liquidity penalty, and tender lifecycle rules. |
| **Dhruv Gupta** | Frontend UI & Outreach | 4-tab institutional Streamlit dashboard, Plotly interactive analytics, and demo presentation. |
=======
| **Shivansh Sahni** | Data & Python Backend | MCX Bhavcopy ingestion across 82 market dates, Gold & Silver normalization (₹/1g 999 gold & ₹/1kg silver), COMEX landed parity model, and expanded multi-commodity database (4,009 rows). |
| **Krishna Sharma** | Quant Logic & Backtesting | Day-by-day walk-forward simulator, cost-of-carry decomposition, liquidity penalty, tender lifecycle rules, exchange SPAN margin relief, and Aurum Copilot NLP rule-based engine. |
| **Dhruv Gupta** | Frontend UI & Outreach | 5-tab institutional Streamlit dashboard, commodity universe switcher, dynamic observation date scrubber, broker ticket export (Kite & Dhan), Plotly analytics, and demo presentation. |
>>>>>>> 89235d3b588cfa496b409f8ec238c511a4fd88b1

---

## 🎯 Problem Statement & Theme Alignment

In the Indian commodities market on the **Multi Commodity Exchange (MCX)**:
<<<<<<< HEAD
- **Same Gold, 4 Different Contracts**: Lot sizes (100g, 10g, 8g, 1g), quotation bases (per 10g, 8g, 1g), purities (995 vs 999), and expiry cycles (3rd–5th vs 27th–31st) all diverge.
- **Messy MCX Bhavcopy**: Space-padded symbols, mixed date formats (`%d %b %Y` vs `%d%b%Y`), and silent holiday fallbacks create false signals.
- **The Arbitrage Mirage**: Apparent calendar spread arbitrage profits vanish once realistic exchange turnover fees, STT/CTT taxes, delivery margins, and thin liquidity haircuts are accounted for.
- **Continuous Series Rollover Distortion**: Retail terminals (e.g. TradingView continuous contracts) stitch together contracts, introducing artificial price jumps at expiry that corrupt econometric spreads.

### Theme Alignment: Track 03 (Commodity Derivatives Intelligence)
AurumSpread delivers **analytical rigor over daily signals**: proving that an apparent paper edge does **not** survive realistic transaction costs is itself an essential, actionable institutional quant finding.

---

## 🚀 The 4 Core USPs (Novelty)
=======
- **Same Bullion, Multiple Contracts**: Lot sizes, quotation bases, purities, and expiry cycles diverge across contracts (`GOLD`, `GOLDM`, `GOLDTEN`, `GOLDGUINEA`, `GOLDPETAL` and `SILVER`, `SILVERM`, `SILVERMIC`, `SILVER100`).
- **Messy MCX Bhavcopy**: Space-padded symbols, mixed date formats (`%d %b %Y` vs `%d%b%Y`), and silent holiday gaps create false signals.
- **The Arbitrage Mirage**: Apparent calendar spread arbitrage profits vanish once realistic exchange turnover fees, STT/CTT taxes, delivery margins, and thin liquidity haircuts are accounted for.
- **Continuous Series Rollover Distortion**: Retail terminals (e.g. TradingView continuous contracts) stitch together contracts, introducing artificial price jumps at expiry that corrupt econometric spreads.
- **Global vs Domestic Disconnect**: Physical bullion traders and hedgers struggle to reconcile international COMEX benchmark prices (USD/oz) with Indian landed import parity (BCD + AIDC + SWC duties + USD/INR + GST).

### Theme Alignment: Track 03 (Commodity Derivatives Intelligence)
AurumSpread delivers **institutional analytical rigor over daily signals**: proving whether an apparent edge survives realistic transaction costs, providing actionable landed import parity intelligence, generating broker-ready execution tickets, and equipping traders with an interactive AI Quant Copilot.

---

## 🚀 The 6 Core USPs (Novelty)
>>>>>>> 89235d3b588cfa496b409f8ec238c511a4fd88b1

1. **Contract-by-Contract Lifecycle Engine**  
   Every contract is tracked as an independent `(Symbol, Expiry)` pair. Eliminates artificial rollover jumps and blocks new entries during illiquid and **MCX physical tender windows** (5 days pre-expiry).
2. **Unit + Purity + Carry Normalization**  
<<<<<<< HEAD
   Converts all four contracts to a uniform **₹ per 1 gram of 999 purity gold**:
   - `GOLDM`: $\text{Close} \div 10 \times \frac{999}{995}$ *(adjusted from 995 purity)*
   - `GOLDTEN`: $\text{Close} \div 10$
   - `GOLDGUINEA`: $\text{Close} \div 8$
   - `GOLDPETAL`: $\text{Close} \div 1$  
   Separates predictable time-value roll-down from true pricing discrepancies.
3. **Liquidity-Penalised Fill Estimator**  
   MCX settlement price is **not** an executable price. A dynamic slippage haircut derived from Volume and Open Interest depth is applied before any trade is counted.
4. **Honest Pre-Cost vs Post-Cost Survival Proof**  
   Directly charts pre-cost theoretical equity against post-cost net equity, proving whether an apparent edge survives real-world fees and slippage.

---

## 🖥️ The 4-Tab Trader Dashboard

```text
AurumSpread/
├── Tab 1: Fair Price & Quiet Alert      → Normalized ₹/g for all 4 contracts; alerts only post-cost
├── Tab 2: Expiry Calendar & Liquidity   → Lifecycle timeline, volume & OI depth, tender zones
├── Tab 3: Futures Curve & Carry         → Curve by expiry; roll-down vs real mispricing
└── Tab 4: Profit vs Fees Simulator      → Walk-forward replay, "What kills the edge?" sensitivity
```

### 1. Tab 1: Fair Price & Quiet Alert
- **4-Contract Normalized Snapshot**: Real-time comparison of all 4 contracts on a ₹/1g of 999 gold benchmark.
- **Quiet Alert System**: Scans 60 active spread pairs on the latest market date. Alerts fire **only** when a post-cost executable edge ($> 0$) survives all statutory charges, slippage, and liquidity filters. Suppresses noise and false arbitrage traps.
=======
   Converts all gold contracts to a uniform **₹ per 1 gram of 999 purity gold** and silver contracts to **₹ per 1 kg**:
   - `GOLD` (1kg): $\text{Close} \div 100 \times \frac{999}{995}$
   - `GOLDM` (100g): $\text{Close} \div 10 \times \frac{999}{995}$
   - `GOLDTEN` (10g): $\text{Close} \div 10$
   - `GOLDGUINEA` (8g): $\text{Close} \div 8$
   - `GOLDPETAL` (1g): $\text{Close} \div 1$  
   Separates predictable time-value roll-down from true pricing discrepancies.
3. **Liquidity-Penalised Fill Estimator**  
   MCX settlement price is **not** an executable price. A dynamic slippage haircut derived from Volume and Open Interest depth is applied before any trade is counted.
4. **MCX vs COMEX Landed Import Parity Model**  
   Converts COMEX spot/futures ($/troy oz) to Indian landed cost using live USD/INR exchange rates, statutory customs duties (5% Basic Customs Duty + 1% AIDC + 10% Social Welfare Surcharge), assessable value formulas, and 3% domestic GST. Computes the **India Gold Basis (₹/g)** to reveal true domestic premiums or discounts.
5. **Broker Execution Ticket Generator (Kite & Dhan)**  
   Converts viable spread opportunities into exchange-compliant 2-leg order payloads for Zerodha Kite Connect and Dhan APIs. Automatically calculates contract lot matching and factors in **~75% exchange calendar spread margin relief** on MCX SPAN margins.
6. **Aurum Copilot (AI Quant Conversational Assistant)**  
   An institutional chatbot capable of natural language queries on spread opportunities, physical inventory hedging (delta-neutral sizing across lot types), tender period risk warnings, COMEX import parity, and execution commands.

---

## 🖥️ The 5-Tab Trader Dashboard

```text
AurumSpread/
├── 🟡/⚪ Commodity Universe Switcher   → Instant toggle between MCX Gold and Silver contracts
├── 📅 Dynamic Date Scrubber          → Historical replay across 82 daily market dates
├── Tab 1: Fair Price & Quiet Alert   → Normalized ₹/g & ₹/kg snapshots; alerts only post-cost
├── Tab 2: Expiry Calendar & Depth    → Lifecycle timeline, volume & OI depth, tender lockout zones
├── Tab 3: Curves, Carry & Parity     → Term structure, carry rate, retail micro-premium & COMEX Parity
├── Tab 4: Simulator & Order Tickets  → Walk-forward replay, "What kills the edge?", Kite/Dhan tickets
└── Tab 5: Aurum Copilot (AI Quant)   → Conversational trade screener, physical hedge sizing & risk audit
```

### 1. Tab 1: Fair Price & Quiet Alert
- **Multi-Contract Normalized Snapshot**: Real-time comparison of all contracts on a standardized ₹/g (Gold) or ₹/kg (Silver) benchmark.
- **Quiet Alert System**: Scans all active spread pairs on the selected market date. Alerts fire **only** when a post-cost executable edge ($> 0$) survives all statutory charges, slippage, and liquidity filters. Suppresses noise and false arbitrage traps.
>>>>>>> 89235d3b588cfa496b409f8ec238c511a4fd88b1

### 2. Tab 2: Expiry Calendar & Liquidity
- **Lifecycle Timeline**: Tracks contract roll-off across calendar months.
- **Volume & Open Interest Depth**: Visualizes liquidity concentration across near vs far expiries.
- **Tender Delivery Exclusion Zones**: Highlights the MCX 5-day pre-expiry tender window where physical delivery allocation and margin spikes occur.

<<<<<<< HEAD
### 3. Tab 3: Futures Curve & Carry
- **Term Structure Curve**: Interactive forward curve (₹/g vs Expiry) displaying Contango / Backwardation regimes.
- **Annualized Implied Carry Rate**: Quantifies financing cost (% p.a.) between front and deferred contracts.
- **Retail Micro-Premium Analysis**: Tracks the structural premium that retail-sized contracts (`GOLDPETAL`, `GOLDGUINEA`) command over mini (`GOLDM`).

### 4. Tab 4: Profit vs Fees Simulator ("What Kills the Edge?")
- **Walk-Forward Simulator**: Replays calendar spread strategies without future data leakage.
- **Overlaid Pre-Cost vs Post-Cost Equity Curves**: Shows paper profit vs realized net equity.
- **"What Kills the Edge?" Breakeven Slider**: Automatically computes the exact cost per leg at which the strategy's net P&L drops to zero.
- **Signal Suppression Funnel**: Visualizes how raw statistical anomalies are filtered out by tender windows, liquidity minimums, and fee barriers.
=======
### 3. Tab 3: Futures Curve, Carry & COMEX Parity
- **Term Structure Curve**: Interactive forward curve (₹/g vs Expiry) displaying Contango / Backwardation regimes.
- **Annualized Implied Carry Rate**: Quantifies financing cost (% p.a.) between front and deferred contracts.
- **Retail Micro-Premium Analysis**: Tracks the structural premium that retail-sized contracts (`GOLDPETAL`, `GOLDGUINEA`) command over mini (`GOLDM`).
- **MCX vs COMEX Import Parity**: Live calculation card displaying landed cost breakdown (Tariff, Duties, GST) and the India Basis (Domestic vs Landed Parity ₹/g) alongside an interactive historical basis timeline.

### 4. Tab 4: Profit vs Fees Simulator & Broker Order Tickets
- **Walk-Forward Simulator**: Replays calendar spread strategies without future data leakage.
- **Overlaid Pre-Cost vs Post-Cost Equity Curves**: Shows paper profit vs realized net equity.
- **"What Kills the Edge?" Breakeven Slider**: Automatically computes the exact cost per leg at which the strategy's net P&L drops to zero.
- **2-Leg Execution Order Ticket**: Displays complete broker payload with 1-click JSON download for Zerodha Kite Connect and CSV download for Dhan / multi-broker terminals.

### 5. Tab 5: Aurum Copilot (AI Quant)
- **Conversational Quant Intelligence**: Interactive chat interface with pre-built prompt pills:
  - `💡 Best Spread Today`: Identifies the top executable spread opportunity after costs.
  - `🛡️ Hedge 250g Gold`: Computes exact integer lot-hedging combinations across contracts with delta mismatch analysis.
  - `🌐 COMEX Import Basis`: Explains current domestic parity, tariff duties, and whether gold is trading at an import premium or discount.
  - `⚠️ Tender Window Risk`: Flags contracts in or approaching the 5-day physical delivery tender window.
- **Natural Language Parsing**: Type custom questions (e.g., *"How do I hedge 1kg of gold with mini contracts?"*, *"Give me the broker order ticket for GOLDM"*, *"Why is there a tender lockout?"*).
>>>>>>> 89235d3b588cfa496b409f8ec238c511a4fd88b1

---

## 🌟 Stretch Features Highlighted in Presentation

<<<<<<< HEAD
- **📐 Lot-Size Hedge Ratio Optimizer**: Calculates exact delta-neutral integer lot ratios between mismatched contracts (e.g. 1 GOLDM 100g vs 12 GOLDGUINEA 8g, or exact zero-delta 2 GOLDM : 25 GOLDGUINEA).
- **🩺 MCX Data Doctor**: Automated Bhavcopy integrity audit checking symbol padding, ISO date formatting, holiday continuity, zero volumes, and contract lifecycle ordering (100/100 score).
- **🏷️ Retail Micro-Premium Heatmap**: Quantifies retail convenience markups over wholesale mini contracts.
=======
- **📐 Lot-Size Hedge Ratio Optimizer**: Calculates exact delta-neutral integer lot ratios between mismatched contracts (e.g. 1 GOLD 1kg = 10 GOLDM = 100 GOLDTEN = 125 GOLDGUINEA = 1000 GOLDPETAL).
- **🩺 MCX Data Doctor**: Automated Bhavcopy integrity audit checking symbol padding, ISO date formatting, holiday continuity, zero volumes, and contract lifecycle ordering (100/100 score).
- **🏷️ Retail Micro-Premium Heatmap**: Quantifies retail convenience markups over wholesale mini contracts.
- **⚡ Calendar Spread Margin Relief**: Integrates MCX's ~75% margin discount on matched calendar spreads into risk & capital allocation.
>>>>>>> 89235d3b588cfa496b409f8ec238c511a4fd88b1

---

## 🥊 What Exists Today vs AurumSpread

| Capability | Retail Terminals (Zerodha, Groww) | Charting (TradingView) | Derivatives Portals (Sensibull) | Institutional (Bloomberg) | **AurumSpread** |
|---|---|---|---|---|---|
<<<<<<< HEAD
| **Purity & Unit Normalization** | ❌ Raw quote only | ❌ None | ❌ None | ⚠️ Manual formula | ✅ **Automated (995 to 999 ₹/g)** |
=======
| **Purity & Unit Normalization** | ❌ Raw quote only | ❌ None | ❌ None | ⚠️ Manual formula | ✅ **Automated (995 to 999 ₹/g & ₹/kg)** |
>>>>>>> 89235d3b588cfa496b409f8ec238c511a4fd88b1
| **No Rollover Discontinuity** | ❌ Rollover jumps | ❌ Continuous jumps | ❌ None | ⚠️ Manual roll rules | ✅ **Contract-by-contract lifecycle** |
| **MCX Tender Period Lockout** | ❌ None | ❌ None | ❌ None | ❌ Custom setup | ✅ **Automated 5-day tender lockout** |
| **Dynamic Liquidity Haircut** | ❌ Uses settlement px | ❌ None | ❌ None | ⚠️ Static bid-ask | ✅ **Dynamic Volume/OI haircut** |
| **Quiet Alert Noise Suppression** | ❌ Raw price alerts | ❌ Indicator noise | ❌ None | ❌ High false-alarm rate | ✅ **Post-cost survival alerts only** |
<<<<<<< HEAD
=======
| **COMEX Landed Import Parity** | ❌ None | ❌ Raw ratio only | ❌ None | ⚠️ Custom pricing sheet | ✅ **Full Duty + GST Landed Parity** |
| **Broker-Ready 2-Leg Ticket** | ❌ Single leg only | ❌ None | ⚠️ Equity/Index only | ❌ Terminal only | ✅ **Kite & Dhan 2-Leg Spread Tickets** |
| **Conversational AI Quant** | ❌ Generic helpdesk | ❌ None | ❌ None | ⚠️ BloombergGPT | ✅ **Aurum Copilot (Commodity Native)** |
>>>>>>> 89235d3b588cfa496b409f8ec238c511a4fd88b1
| **Cost** | Free (Brokered) | \$15–\$60/mo | \$10–\$25/mo | \$24,000+/year | ✅ **Open-Source Quant Prototype** |

---

## 🛠️ Technology Stack & Architecture

- **Language & Runtime**: Python 3.10+
- **Analytics & Quants**: Pandas, NumPy
- **Interactive UI**: Streamlit
- **Visualizations**: Plotly Express & Plotly Graph Objects
<<<<<<< HEAD
- **Test Automation**: Pytest (23 unit & integration tests)
- **Data Source**: Official MCX Bhavcopy (public daily exchange data)

```text
AurumSpread/
├── app.py                     # 4-Tab Institutional Streamlit Dashboard
├── build_historical_dataset.py # Pipeline cleaning raw Bhavcopy CSVs
├── requirements.txt           # Project dependencies
├── pytest.ini                 # Pytest configuration
│
├── src/                       # Core Analytical Engines
│   ├── normalize.py           # Unit & 999 purity normalization
│   ├── spread_engine.py       # Calendar spread pair generator
│   ├── spread_intelligence.py # Expanding-window Z-score & percentiles
│   ├── carry_engine.py        # Forward curve, annualized carry & micro-premium
│   ├── liquidity_engine.py    # Volume/OI depth, tender lockout, dynamic slippage
│   ├── backtest_engine.py     # Walk-forward backtester & survival proof
│   ├── quiet_alerts.py        # Quiet alert scanner & noise suppression
│   ├── hedge_optimizer.py     # Lot-size integer delta hedge optimizer
│   └── data_doctor.py         # Automated Bhavcopy health auditor
│
├── data/
│   ├── raw/                   # Raw daily MCX Bhavcopy CSV files
│   └── processed/             # Cleaned historical_gold_futures.csv
│
└── tests/                     # 23 automated pytest test cases
=======
- **Test Automation**: Pytest (26 unit & integration tests, 100% passing)
- **Data Source**: Official MCX Bhavcopy (public daily exchange data across 82 market sessions)

```text
AurumSpread/
├── app.py                         # 5-Tab Institutional Streamlit Dashboard
├── requirements.txt               # Project dependencies
├── pytest.ini                     # Pytest configuration
│
├── src/                           # Core Analytical Engines
│   ├── normalize.py               # Unit & 999 purity normalization (Gold + Silver)
│   ├── spread_engine.py           # Calendar spread pair generator
│   ├── spread_intelligence.py     # Expanding-window Z-score & percentiles
│   ├── carry_engine.py            # Forward curve, annualized carry & micro-premium
│   ├── liquidity_engine.py        # Volume/OI depth, tender lockout, dynamic slippage
│   ├── backtest_engine.py         # Walk-forward backtester & survival proof
│   ├── quiet_alerts.py            # Quiet alert scanner & noise suppression
│   ├── hedge_optimizer.py         # Lot-size integer delta hedge optimizer
│   ├── data_doctor.py             # Automated Bhavcopy health auditor
│   ├── parity_engine.py           # COMEX Landed Import Parity & India Basis
│   ├── order_ticket.py            # Kite Connect & Dhan 2-leg order tickets
│   └── copilot_engine.py          # Aurum Copilot conversational quant intelligence
│
├── data/
│   ├── raw/                       # 82 Raw daily MCX Bhavcopy CSV files
│   └── processed/                 # Cleaned datasets
│       ├── historical_gold_futures.csv     # 5 Gold contracts (2,445 records)
│       ├── historical_silver_futures.csv   # 4 Silver contracts (1,564 records)
│       └── historical_bullion_futures.csv  # Unified Bullion dataset (4,009 records)
│
├── scripts/
│   ├── build_historical_dataset.py # Original Gold builder
│   └── build_expanded_dataset.py   # Multi-commodity Gold + Silver builder
│
└── tests/                         # 26 automated pytest test cases
    ├── test_suite.py
    └── test_new_engines.py
>>>>>>> 89235d3b588cfa496b409f8ec238c511a4fd88b1
```

---

## ⚡ Quickstart & Installation

### 1. Clone the repository & create virtual environment
```bash
<<<<<<< HEAD
git clone https://github.com/<your-username>/AurumSpread.git
=======
git clone https://github.com/Dhruvgupta018/AurumSpread.git
>>>>>>> 89235d3b588cfa496b409f8ec238c511a4fd88b1
cd AurumSpread
python -m venv .venv
```

Activate environment:
- **Windows**: `.venv\Scripts\activate`
- **Linux / macOS**: `source .venv/bin/activate`

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the automated test suite
```bash
pytest
```
<<<<<<< HEAD
*Expected result: 23 passed, 0 failures.*
=======
*Expected result: 26 passed, 1 skipped (0 failures).*
>>>>>>> 89235d3b588cfa496b409f8ec238c511a4fd88b1

### 4. Launch the Streamlit dashboard
```bash
streamlit run app.py
```
Open your browser at `http://localhost:8501`.

---

## 🏆 Hackathon Submission Checklist (Final Round)

- [x] **Track 03 Alignment**: Rigorous commodity derivatives intelligence with cost-of-carry and walk-forward backtesting.
<<<<<<< HEAD
- [x] **4 Core USPs Implemented**: Contract lifecycle, unit+purity normalization, liquidity-penalised fill, honest pre vs post-cost survival proof.
- [x] **4-Tab Trader Dashboard**: Exactly matches PPT Slide 6 structure and features.
- [x] **Stretch Features**: Lot-size hedge optimizer, MCX Data Doctor audit, "What kills the edge?" sensitivity, retail micro-premium analysis.
- [x] **100% Passing Test Suite**: 23 clean pytest tests verifying data integrity, quant models, and zero future data leakage.
- [x] **Production Ready**: Beautiful institutional dark-gold theme, responsive interactive charts, zero runtime errors.
=======
- [x] **6 Core USPs Implemented**: Contract lifecycle, unit+purity normalization, liquidity-penalised fill, honest survival proof, COMEX landed parity, and 2-leg broker tickets.
- [x] **Multi-Commodity Expansion**: Full support for both Gold (`GOLD`, `GOLDM`, `GOLDTEN`, `GOLDGUINEA`, `GOLDPETAL`) and Silver (`SILVER`, `SILVERM`, `SILVERMIC`, `SILVER100`).
- [x] **5-Tab Trader Dashboard**: Intuitive institutional UI with dynamic date replay, interactive Plotly visuals, and zero raw code leaks.
- [x] **Aurum Copilot AI**: Interactive Quant Assistant with prompt chips and conversational hedging/pricing intelligence.
- [x] **100% Passing Test Suite**: 26 automated pytest tests verifying data integrity, quant models, and zero future data leakage.
- [x] **Production Ready**: Verified against 82 MCX Bhavcopy sessions with Kite Connect / Dhan integration export.
>>>>>>> 89235d3b588cfa496b409f8ec238c511a4fd88b1

---
*Built with ❤️ for **Hack in Hills '26** by Team AurumSpread.*
