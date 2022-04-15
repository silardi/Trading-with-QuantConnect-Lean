from AlgorithmImports import *
from yahoo_reader import YahooData

from yahoo_loader import *


class FirstAlgorithm(QCAlgorithm):
    def Initialize(self):

        get_yahoo_data('TQQQ', '2021-01-01', '2022-01-01')

        self.SetStartDate(2021, 1, 1)  # Set Start Date
        self.SetEndDate(2021, 2, 1)  # Set End Date
        self.SetCash(100000)  # Set Strategy Cash

        # self.AddEquity("SPY", Resolution.Minute)
        # self.symbol = self.AddData(YahooData, "SPY", Resolution.Daily).Symbol
        self.symbol = self.AddData(YahooData, "TQQQ", Resolution.Daily).Symbol
        # self.symbol = self.AddData(YahooData, "UDOW", Resolution.Daily).Symbol

    def OnData(self, data):
        """OnData event is the primary entry point for your algorithm. Each new data point will be pumped in here.
            Arguments:
                data: Slice object keyed by symbol containing the stock data
        """
        if not self.Portfolio.Invested:
            # self.SetHoldings("SPY", 1)
            self.SetHoldings("TQQQ", 1)
            # self.SetHoldings("UDOW", 1)
            self.Debug("Purchased Stock")

        # Keep track of the values
        self.Debug(
            f"{self.symbol.Value} - {self.Time}: Close={data[self.symbol].Close}")

        # close = self.Securities["UDOW"].Close
        # self.StopMarketOrder("UDOW", 10, round((close * .90), 2))
        # self.Debug(f"{self.Portfolio.TotalPortfolioValue}")
