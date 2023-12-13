import pandas as pd
import yfinance as yf
from data_fetcher import get_sp500_tickers_and_urls, download_stock_returns
from config import START_DATE, END_DATE

def create_tickers_dataframe():
    tickers, urls = get_sp500_tickers_and_urls()
    df = pd.DataFrame({'tickers': tickers, 'url': urls})
    return df

def process_stock_returns():
    tickers, _ = get_sp500_tickers_and_urls()
    data = download_stock_returns(tickers, START_DATE, END_DATE)
    returns_df = data.stack().reset_index().rename(columns={"level_1": "Symbol"})
    returns_df.sort_values(['Symbol', 'Date'], inplace=True)
    returns_df.set_index('Date', inplace=True)
    return returns_df

def get_company_info(tickers):
    info_tickers = yf.Tickers(tickers)
    info_df = pd.DataFrame()

    for ticker in tickers:
        stock_info = info_tickers.tickers[ticker].info
        stock_info_df = pd.DataFrame.from_dict(stock_info, orient='index').T
        info_df = pd.concat([info_df, stock_info_df])

    info_df.reset_index(inplace=True, drop=True)
    return info_df