import numpy as np

def historical_var(pnl, alpha=5):
    return np.percentile(pnl, alpha)