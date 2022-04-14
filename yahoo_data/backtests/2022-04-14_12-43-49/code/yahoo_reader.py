from AlgorithmImports import *
from pathlib import Path
from datetime import datetime, timedelta


class YahooData(PythonData):
    def GetSource(self, config, date, isLiveMode):
        # print(f'GetSource YAHOO for date {date}')

        # The name of the asset is the symbol in lowercase .csv (ex. spy.csv)
        fname = config.Symbol.Value.lower() + '.csv'

        # The source folder depends on the directory initialized in lean-cli
        # https://www.quantconnect.com/docs/v2/lean-cli/tutorials/local-data/importing-custom-data
        source = Path(Globals.DataFolder)/'yahoo'/fname

        # The subscription method is LocalFile in this case
        return SubscriptionDataSource(source.as_posix(), SubscriptionTransportMedium.LocalFile)

    def Reader(self, config, line, date, isLiveMode):

        # print(f'Reading date {date}')
        # print(f'line ==> {line}')

        equity = YahooData()
        equity.Symbol = config.Symbol

        # Parse the Line from the Yahoo CSV
        try:
            data = line.split(',')

            # If value is zero, return None
            value = data[4]
            if value == 0:
                return None

            equity.Time = datetime.strptime(data[0], "%Y-%m-%d")
            equity.EndTime = equity.Time + timedelta(days=1)
            equity.Value = value
            equity["Open"] = float(data[1])
            equity["High"] = float(data[2])
            equity["Low"] = float(data[3])
            equity["Close"] = float(data[4])
            equity["AdjClose"] = float(data[5])
            equity["VolumeUSD"] = float(data[6])

            # print(f'Returning --> {coin.EndTime} - {coin}')
            return equity

        except ValueError:
            # Do nothing, possible error in csv decoding
            return None
