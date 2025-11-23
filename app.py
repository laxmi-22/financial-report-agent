# app.py
from orchestrator.pipeline import run_agent,api_key_authentication
from tools.utilities import apply_css,ticker_select,set_date
import asyncio
import streamlit as st


if __name__ == "__main__":
    
    #google key authentication
    api_key_authentication()

    #apply formating for streamlit page
    apply_css()   
   

    # sidebar title and header
    st.title="abc"
    st.sidebar.title("Financial Market Analysis and Reporting System ")
    st.sidebar.header("Inputs")

    
     # Dropdown selection for company names
    ticker_dict=ticker_select()
    selected_company = st.sidebar.selectbox("Choose a company", list(ticker_dict.keys()))

    # Resolve to ticker
    ticker = ticker_dict[selected_company]
    st.sidebar.write(f"Selected ticker: {ticker}")
    
    #start and end date (by default start date is current month 1st to current month end    
    sdate,edate=set_date()

    #start date
    start_date = st.sidebar.date_input("Start date", value=sdate,key="start")
    
    #end date
    end_date = st.sidebar.date_input("End date", value=edate,key="end")
    st.sidebar.write("")
    
    
    message="Begin data collection for ticker " +  ticker + " start from " + start_date.strftime('%Y-%m-%d') + " and end by " + end_date.strftime('%Y-%m-%d') + "."
    

    # Create a submit button
    if st.sidebar.button("Performace Report"):        
        try:
            answer = asyncio.run(run_agent(message))
        except RuntimeError:
            loop = asyncio.get_event_loop()
            answer = loop.run_until_complete(run_agent(message))
        
        st.write(answer)
        

    