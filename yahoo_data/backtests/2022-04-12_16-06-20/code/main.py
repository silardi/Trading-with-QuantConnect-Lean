from AlgorithmImports import *
from yahoo_reader import YahooData


class Yahoodata(QCAlgorithm):
    def Initialize(self):
        self.SetStartDate(2021, 1, 1)  # Set Start Date
        self.SetEndDate(2022, 1, 1)  # Set End Date
        self.SetCash(100000)  # Set Strategy Cash

        # self.AddEquity("SPY", Resolution.Minute)
        self.symbol = self.AddData(YahooData, "TQQQ", Resolution.Daily).Symbol

    def OnData(self, data):
        """OnData event is the primary entry point for your algorithm. Each new data point will be pumped in here.
            Arguments:
                data: Slice object keyed by symbol containing the stock data
        """
        # if not self.Portfolio.Invested:
        #     self.SetHoldings("TQQQ", 1)
        #     self.Debug("Purchased Stock")

        # Keep track of the values
        # self.Debug(f"{self.symbol.Value} - {self.Time}: Close={data[self.symbol].Close}")

        close = self.Securities["TQQQ"].Close
        self.StopMarketOrder("TQQQ", 10, close * .90)
        self.Debug(f"{self.Portfolio.TotalPortfolioValue}")
