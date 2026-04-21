from models.monte_carlo_rates import simulate_rate_paths
from analytics.portfolio_risk import compute_portfolio_pnl
from models.var_historical import historical_var
from models.var_parametric import parametric_var
from models.stress_scenarios import stress_test
from analytics.loss_distribution import plot_distribution

# 1. Simulate interest rate paths
rate_paths = simulate_rate_paths(n_sims=5000, n_steps=252)

# 2. Compute portfolio PnL under rate paths
pnl = compute_portfolio_pnl(rate_paths)

# 3. VaR calculations
hist_var = historical_var(pnl)
param_var = parametric_var(pnl)

# 4. Stress testing
stress_results = stress_test(pnl)

# 5. Output visualization
plot_distribution(pnl, hist_var, param_var)

print("Historical VaR:", hist_var)
print("Parametric VaR:", param_var)