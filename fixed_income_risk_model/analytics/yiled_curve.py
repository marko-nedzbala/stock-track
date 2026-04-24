import numpy as np

def nelson_siegel(t, beta0, beta1, beta2, tau):
    term1 = beta0
    term2 = beta1 * ((1 - np.exp(-t/tau)) / (t/tau))
    term3 = beta2 * (((1 - np.exp(-t/tau)) / (t/tau)) - np.exp(-t/tau))
    return term1 + term2 + term3

def yield_curve_slope(rates):
    rates["slope"] = rates["DGS10"] - rates["DGS2"]
    return rates