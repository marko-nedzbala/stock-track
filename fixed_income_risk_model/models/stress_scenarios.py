import numpy as np

def stress_test(pnl):
    return {
        "extreme_loss": np.min(pnl),
        "avg_tail_loss": np.mean(pnl[pnl < np.percentile(pnl, 5)])
    }

def stress_scenarios(base_rate):
    return {
        "parallel_up_100bp": base_rate + 1.00,
        "parallel_down_100bp": base_rate - 1.00,
        "steepening": base_rate + np.linspace(0, 1.5, 10),
        "flattening": base_rate - np.linspace(0, 1.5, 10)
    }

def model_risk_score(pnl):
    return {
        "volatility": np.std(pnl),
        "skew": (np.mean((pnl - np.mean(pnl))**3)) / np.std(pnl)**3,
        "tail_ratio": np.mean(pnl[pnl < np.percentile(pnl, 5)])
    }