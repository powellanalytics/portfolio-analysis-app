import pandas as pd
import requests
from bs4 import BeautifulSoup
import yfinance as yf
from config import WIKI_URL, BASE_URL

def get_sp500_tickers_and_urls():
    request = requests.get(WIKI_URL)
    soup = BeautifulSoup(request.content, 'html.parser')
    main_table = soup.find(id='constituents')
    rows = main_table.find('tbody').findAll('tr')[1:]

    tickers = [row.findAll('td')[0].text.strip() for row in rows]
    urls = [BASE_URL + row.findAll('a')[1]['href'] for row in rows]

    return tickers, urls

def download_stock_returns(tickers, start_date, end_date):
    if end_date == '':
        return yf.download(tickers, start=start_date)
    return yf.download(tickers, start=start_date, end=end_date)
