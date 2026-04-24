import numpy as np
import pandas as pd

np.random.seed(42)

n = 5000
rates = np.cumsum(np.random.normal(0, 0.01, n)) + 0.03

df = pd.DataFrame({
    "rate": rates,
    "shock": np.diff(np.insert(rates, 0, rates[0]))
})

df.to_csv("data/simulated_rates.csv", index=False)