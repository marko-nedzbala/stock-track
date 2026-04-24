import matplotlib.pyplot as plt

def plot_distribution(pnl, hist_var, param_var):
    plt.hist(pnl, bins=50)
    plt.axvline(hist_var, color='red', linestyle='dashed', label="Historical VaR")
    plt.axvline(param_var, color='green', linestyle='dashed', label="Parametric VaR")
    plt.legend()
    plt.title("Portfolio Loss Distribution")
    plt.show()