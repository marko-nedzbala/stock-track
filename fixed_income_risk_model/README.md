📌 Title
Fixed Income Market Risk Simulation & VaR Framework
📌 Overview

This project implements a quantitative market risk framework for fixed income portfolios using Python. It models interest rate dynamics, simulates portfolio PnL under stochastic rate paths, and computes risk metrics including Value-at-Risk (VaR) and stress loss distributions.

📌 Key Features
Monte Carlo simulation of interest rate paths
Historical and parametric VaR models
Portfolio loss distribution modeling
Stress testing under extreme rate shocks
Duration-based sensitivity analysis
📌 Methodology

The framework combines:

Geometric Brownian Motion–style interest rate simulation
Duration-based fixed income risk approximation
Statistical loss distribution analysis
Tail-risk quantification using percentile-based VaR
📌 Risk Metrics Implemented
Historical VaR (non-parametric)
Parametric VaR (Gaussian assumption)
Tail loss estimation
Stress scenario analysis
📌 Tech Stack
Python (NumPy, Pandas, SciPy)
Matplotlib
Monte Carlo Simulation
Financial Risk Modeling Concepts
📌 Example Output
Portfolio loss distribution histogram
VaR thresholds (95%, 99%)
Stress loss scenarios under rate shocks
📌 Use Cases
Market risk modeling
Fixed income portfolio analysis
Regulatory capital estimation
Risk management stress testing
📌 Author

Quantitative Risk Professional
Specializing in Market Risk, VaR, and Fixed Income Analytics




How to run
$ docker-compose up --build

goto:
http://localhost:8501

Name the repo
fixed-income-risk-platform




