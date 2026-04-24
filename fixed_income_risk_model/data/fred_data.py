import pandas_datareader.data as web
import datetime

def get_treasury_rates():
    start = datetime.datetime(2020, 1, 1)
    end = datetime.datetime(2026, 1, 1)

    rates = web.DataReader(
        ["DGS2", "DGS10"],  # 2Y and 10Y Treasury
        "fred",
        start,
        end
    )

    rates = rates.dropna()
    return rates