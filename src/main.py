from data_processor import create_tickers_dataframe, process_stock_returns, get_company_info

def main():
    # Create DataFrame of tickers and URLs
    df = create_tickers_dataframe()
    print(df.tail())

    # Process stock data
    stock_returns = process_stock_returns()
    print(stock_returns.head(20))

    # Get company information
    info_df = get_company_info(df['tickers'].tolist())
    print(info_df.tail())

if __name__ == "__main__":
    main()