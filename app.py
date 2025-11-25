# app.py
from orchestrator.pipeline import run_agent,api_key_authentication
from tools.utilities import apply_css,ticker_select,set_date,validate_dates
import asyncio
import streamlit as st


if __name__ == "__main__":
    
    #google key authentication
    api_key_authentication()

    #apply formating for streamlit page
    apply_css()    

   
    # sidebar title and header    
    st.sidebar.title("Financial Market Analysis and Reporting System ")
    st.sidebar.header("User Inputs")

    
     # Dropdown selection for company names(load from csv)
    ticker_dict=ticker_select()
    company=list(ticker_dict.keys())

    #start and end date (by default start date is current month 1st to current month end    
    sdate,edate=set_date()


     # Initialize defaults in session
    if "companyticker" not in st.session_state:
        st.session_state["companyticker"] = "Microsoft Corporation"   # default ticker
    if "startdate" not in st.session_state:        
        st.session_state["startdate"] = sdate
    if "enddate" not in st.session_state:        
        st.session_state["enddate"] = edate

    selected_company = st.sidebar.selectbox("Choose a company", company,key="companyticker")

    # Resolve to ticker
    ticker = ticker_dict[selected_company]
    st.sidebar.write(f"Selected ticker: {ticker}")

    #start date  
    start_date = st.sidebar.date_input("Start date", key="startdate")
    
    #end date   
    end_date = st.sidebar.date_input("End date", key="enddate")
    st.sidebar.write("")
    
    # Create a submit button
    if st.sidebar.button("Performace Report"):
        # Perform validation    
        if validate_dates(start_date, end_date):     
            message="Begin data collection for ticker " +  ticker + " start from " + start_date.strftime('%Y-%m-%d') + " and end by " + end_date.strftime('%Y-%m-%d') + "."
    
            try:
                answer = asyncio.run(run_agent(message))
            except RuntimeError:
                loop = asyncio.get_event_loop()
                answer = loop.run_until_complete(run_agent(message))
            
            st.write(answer)
        

    
