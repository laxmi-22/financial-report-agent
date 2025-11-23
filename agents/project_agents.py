
from google.adk.models.google_llm import Gemini
from google.genai import types
from google.adk.agents import Agent
from tools.stock_api import fetch_market_data

#get GOOGLE_API_KEY from environment
from dotenv import load_dotenv
load_dotenv()


#retry option
retry_config=types.HttpRetryOptions(
    attempts=5,  # Maximum retry attempts
    exp_base=7,  # Delay multiplier
    initial_delay=1,
    http_status_codes=[429, 500, 503, 504], # Retry on these HTTP errors
)


# Define the DataCollectorAgent

def data_collector_agent():    
    return(Agent(
    name="DataCollectorAgent",
    model=Gemini(
        model="gemini-2.5-flash-lite",
        retry_options=retry_config
    ),
    instruction=f"""
    You are the Data Collector. Your job is to acquire raw stock market data.
    1. You MUST call the 'fetch_market_data' tool with the ticker , start date and end date received in your initial message
    2. After the tool executes and returns a result, you **MUST** make that exact result your **ONLY and FINAL** output text. 
    3. Do not add any extra commentary, greetings, or text wrappers (like "Here is the data:").
    """,
    
    # 🚨 CRITICAL: Pass the tool instance to the tools list
    tools=[fetch_market_data], 
    
    # CRITICAL: This stores the final output (the result of the tool call)
    output_key="json_datacollector", 
)
)


#Trend Analyzer Agent - Analyzes the raw, high-token data and applies data reduction logic.
def trend_analyzer_agent():
  return(Agent(
    name="TrendAnalyzerAgent",
    model=Gemini(
        model="gemini-2.5-flash-lite",
        retry_options=retry_config
    ),
    # The `{json_datacollector}` placeholder automatically injects the state value from the previous agent(data collector)'s output.
    instruction="""
    You are the Trend Analyzer. Your sole job is to process raw financial data and apply statistical analysis to extract only the 
    most critical, high-signal insights. You MUST condense the input data into a concise summary adhering to the three required points below.

     
    input data: {json_datacollector} 
    
    **Compaction Rules:**
    DO NOT include any other information or commentary. 
    DO NOT use bullet points. 
    Your output must be a single, continuous block of text. 
    
    Based on the input data, generate a summary that includes ONLY the following three points. 
    
    1. Overall Performance: Calculate and report the net percentage change (first close to last close) and the average daily trading volume. 
    2. Significant Anomaly: Identify the single day with the largest percentage price change (up or down). State the date and magnitude. 
    3. Trend Analysis: Describe the dominant price trend for the first half of the period and the dominant trend for the second half.
    
    Output Format
    A single paragraph summary containing only the three required insights, ready for the Report Generator.
    """,
        
    output_key="trend_summary",  # The result of this agent will be stored with this key.
)
  )

#Report Generator Agent - Creates the final, client-facing document.
def report_generator_agent():
  return(Agent(
    name="ReportGeneratorAgent",
    model=Gemini(
        model="gemini-2.5-flash-lite",
        retry_options=retry_config
    ),
    # This agent receives the `{trend_summary}` from the Trend Analyzer agent's output.
    instruction="""
    You are the Financial Report Generator. Your task is to write a polished, professional, client-facing financial report based ONLY on 
    the "Trend Summary" provided. You MUST NOT make up any facts, use external information, or generate commentary not supported by the summary.

    Trend Summary: {trend_summary}
    
    Write a formal report titled "[TICKER] Performance Analysis." 
    
    The report should be structured into: 
    1. Executive Summary: 
        A brief opening that states the key outcome. Highlight the metric values and display in order(bullet points)
    2. Performance Review: 
        A brief discussing the overall results and the average trading volume. Highlight the metric values and display in order(bullet points)
    3. Anomaly & Outlook: 
        A brief discussing the significant price movement and 
        the different trends observed in the first and second halves.Highlight the metric values and display in order(bullet points).
    4.Evaluation metrics: 
        Factual Accuracy
        Flesch-Kincaid Grade Level
        Hallucination Score
    

    Constraint:
    The final report MUST pass the Agent Evaluation metrics: Factual Accuracy > 95% 
    and Flesch-Kincaid Grade Level < 12, and Zero Hallucination Score.
    """,      
    
    output_key="final_report",  # This is the final output of the entire pipeline.
)
  )