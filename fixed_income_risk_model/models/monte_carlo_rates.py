import numpy as np


def simulate_rate_paths(n_sims=1_000, n_steps=252, r0=0.03, mu=0.0, sigma=0.01):
    trading_days = 1 / 252
    paths = np.zeros( (n_sims, n_steps))

    mu = rates["slope"].mean() / 100

    for i in range(n_sims):
        rates = [r0]
        for t in range(1, n_steps):
            dr = (mu * trading_days) + (sigma * np.sqrt(trading_days) * np.random.normal())
            rates.append(max(rates[-1] + dr, 0))
        paths[i] = rates
    return paths














