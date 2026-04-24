import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

from models.monte_carlo_rates import simulate_rate_paths
from analytics.portfolio_risk import compute_portfolio_pnl
from models.var_historical import historical_var
from models.var_parametric import parametric_var

st.set_page_config(page_title="Fixed Income Risk Dashboard", layout="wide")

st.title("📊 Fixed Income Market Risk & VaR Dashboard")

# Sidebar controls
n_sims = st.sidebar.slider("Monte Carlo Simulations", 1000, 20000, 5000)
duration = st.sidebar.slider("Portfolio Duration", 1, 10, 5)

# Run simulation
rate_paths = simulate_rate_paths(n_sims=n_sims)
pnl = compute_portfolio_pnl(rate_paths, duration=duration)

hist_var = historical_var(pnl)
param_var = parametric_var(pnl)

# --- Metrics ---
col1, col2, col3 = st.columns(3)

col1.metric("Mean PnL", f"{np.mean(pnl):,.2f}")
col2.metric("Historical VaR (95%)", f"{hist_var:,.2f}")
col3.metric("Parametric VaR", f"{param_var:,.2f}")

# --- Histogram ---
st.subheader("Loss Distribution")
fig, ax = plt.subplots()
ax.hist(pnl, bins=50)
ax.axvline(hist_var, color="red", linestyle="dashed")
ax.axvline(param_var, color="green", linestyle="dashed")
st.pyplot(fig)

# --- Stress Insight ---
st.subheader("Tail Risk Insight")
st.write("5% Tail Mean Loss:", np.mean(pnl[pnl < np.percentile(pnl, 5)]))