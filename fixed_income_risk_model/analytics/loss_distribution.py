import numpy as np

def compute_portfolio_pnl(rate_paths, duration=5, notional=1_000_000):
    pnl = []

    for path in rate_paths:
        shocks = np.diff(path)
        pnl_path = -duration * notional * shocks
        pnl.append(np.sum(pnl_path))

    return np.array(pnl)