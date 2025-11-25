import streamlit as st
import os
import pandas as pd
import datetime as dt
import calendar
from datetime import date

# procedure to apply css(format) to streamlit page
# css file is placed in project folder with name as localcss.css
def apply_css():
    #path to fetch local css file and apply style to page
    ROOT_DIR = os.path.abspath(os.curdir)    
    filepath=ROOT_DIR + "\\localcss.css"
    filename=filepath.replace("\\","//")

    with open(filename) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


# procedure for ticker selection in sidebar.
# csv file with popular 50 tickers is placed in project folder. 
# this can be improved by calling API to get ticker names
def ticker_select():
    # Load tickers from CSV
    tickers_df = pd.read_csv("nse_bse_tickers.csv")
    ticker_dict = dict(zip(tickers_df['Company Name'], tickers_df['Ticker']))
    return ticker_dict



# procedure to set start and end date in page to default(by default start date is 1st of current month and end date to current month end
def set_date():     
    ct_month= dt.datetime.now().month
    ct_yr = dt.datetime.now().year
    num_days_in_current_month = calendar.monthrange(ct_yr, ct_month)[1]
    sdate = dt.date(ct_yr, ct_month, 1)
    edate = dt.date(ct_yr, ct_month, num_days_in_current_month)

    return sdate,edate

def validate_dates(start_date_input, end_date_input):
        """
        Validates the start and end dates based on the following rules:
        1. Start date cannot be in the future.
        2. Start date must be before or on the same day as the end date.
        
        Returns True if valid, otherwise displays an error and returns False.
        """
        today = date.today()

        if start_date_input > today:            
            st.error("❌ Error: Start date cannot be a future date.")
            # Stop the script execution here
            return False
        
        if start_date_input > end_date_input:            
            st.error("❌ Error: Start date must be before the end date.")
            # Stop the script execution here
            return False
        
        return True
    #validation ends
