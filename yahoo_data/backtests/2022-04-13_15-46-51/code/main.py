from AlgorithmImports import *
from yahoo_reader import YahooData


class FirstAlgorithm(QCAlgorithm):
    def Initialize(self):
        self.SetStartDate(2013, 10, 7)  # Set Start Date
        self.SetEndDate(2013, 10, 11)  # Set End Date
        self.SetCash(100000)  # Set Strategy Cash

        self.AddEquity("SPY", Resolution.Minute)
        # self.symbol = self.AddData(YahooData, "UDOW", Resolution.Daily).Symbol

    def OnData(self, data):
        """OnData event is the primary entry point for your algorithm. Each new data point will be pumped in here.
            Arguments:
                data: Slice object keyed by symbol containing the stock data
        """
        if not self.Portfolio.Invested:
            self.SetHoldings("SPY", 1)
            self.Debug("Purchased Stock")

        # Keep track of the values
        # self.Debug(f"{self.symbol.Value} - {self.Time}: Close={data[self.symbol].Close}")

        # close = self.Securities["UDOW"].Close
        # self.StopMarketOrder("UDOW", 10, round((close * .90), 2))
        # self.Debug(f"{self.Portfolio.TotalPortfolioValue}")
