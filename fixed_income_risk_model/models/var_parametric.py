import numpy as np

def parametric_var(pnl, confidence=1.65):
    return -(np.mean(pnl) - confidence * np.std(pnl))