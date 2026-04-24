import numpy as np


def var_backtest(pnl, var_series, alpha=0.05):
    breaches = pnl < var_series
    breach_rate = np.mean(breaches)

    expected = alpha
    kupiec_ratio = breach_rate / expected

    return {
        "breach_rate": breach_rate,
        "expected_rate": expected,
        "kupiec_ratio": kupiec_ratio
    }