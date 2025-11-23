# The Function Logic to collect stock data from yahoo finance library
import yfinance as yf
import pandas as pd
import json
from datetime import datetime, timedelta

# ... other imports (pandas, json, datetime)

def fetch_market_data(ticker: str, start: str, end: str) -> str:
    """
    Fetches historical stock data (OHLCV) for a given ticker over a specified number of days
    using the yfinance API. Returns the data as a JSON string.
    
    Args:
        ticker: The valid stock ticker symbol (e.g., 'TSLA', 'GOOGL').
        start: The start date to fetch market data of ticker (e.g. "2025-10-01" ).
        end: The end date to fetch market data of ticker (e.g. "2025-10-31" ).
        
    Returns:
        A JSON string containing the fetched market data, including the ticker, 
        date range, and a list of OHLCV data points.
    """

    try:
        # Define the date range
        start_date = datetime.strptime(start, '%Y-%m-%d')
        end_date = datetime.strptime(end, '%Y-%m-%d')

        # Use yfinance to download data
        data = yf.download(
            ticker, 
            start=start_date, 
            end=end_date,
            progress=False # Suppress download messages
        )

        if data.empty:
            return json.dumps({"error": f"No data found for {ticker} within the date range."})

        # Convert the Pandas DataFrame into a JSON format suitable for the LLM
        # The 'records' orientation is usually the easiest for the LLM to process
        json_data_string = data.reset_index().to_json(orient='records', date_format='iso')
        
        # Wrap the data with context for the LLM
        result = {
            "ticker": ticker,
            "date_range": f"{start_date} to {end_date}",
            "ohlcv_data": json.loads(json_data_string) # The actual list of data objects
        }
        
        # Return the final JSON string that the ADK agent will output
        return json.dumps(result, indent=2)

    except Exception as e:
        return json.dumps({"error": f"API or network error during fetch: {e}"})
    


