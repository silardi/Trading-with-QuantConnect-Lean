import pandas as pd
from pathlib import Path
from datetime import timedelta
from yahoo_fin.stock_info import get_data
from AlgorithmImports import *


def get_yahoo_ticker(ticker, folder, start_date, end_date):

    # check if the ticker file exists
    fname = ticker.lower() + '.csv'
    path = Path(folder)/fname

    # get the dates if the file already exists
    if path.exists():
        # open the file and get the dates
        df = pd.read_csv(path, index_col=0)
        dates = pd.DatetimeIndex(df.index.sort_values(ascending=True))

    else:
        dates = None

    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)

    # if the range is not included in the file or if there is no file at all
    if dates is None or start_date < dates[0] or end_date > dates[-1]:

        # try to retrieve the data from Yahoo_fin
        try:
            delta = timedelta(days=3)
            df = get_data(ticker, start_date=start_date -
                          delta, end_date=end_date+delta)
            df.to_csv(path)
            print(f'Retrieving ticker: {ticker}')

        except BaseException as e:
            print(f'Problem getting ticker {ticker}')
            return None

    else:
        print(f'Ticker {ticker} already loaded')

    return ticker


def get_yahoo_data(tickers: list, start_date, end_date):
    """Get a list of tickers from yahoo and save them in the Default LEAN data directory"""

    # transform tickers into a list (if it is not)
    tickers = tickers if isinstance(tickers, list) else [tickers]

    # check the directory
    folder = Path(Globals.DataFolder)/'yahoo'

    if not folder.exists():
        folder.mkdir()
        print(f'Folder {str(folder)} - Created')

    else:
        print(f'Folder {str(folder)} - Ok')

    # create a list to store all loaded tickers
    loaded_tickers = []
    for ticker in tickers:
        loaded_tickers.append(get_yahoo_ticker(
            ticker, folder, start_date, end_date))

    return [ticker for ticker in loaded_tickers if ticker is not None]
