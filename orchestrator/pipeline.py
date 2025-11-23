# orchestrator/pipeline.py
from google.adk.agents import SequentialAgent
from google.adk.runners import InMemoryRunner
from agents.project_agents import trend_analyzer_agent,report_generator_agent,data_collector_agent
import os

#get GOOGLE_API_KEY from environment
from dotenv import load_dotenv
load_dotenv()

def api_key_authentication():
       try:
            GOOGLE_API_KEY = os.environ["GOOGLE_API_KEY"]            
            print("✅ Setup and authentication complete.")
       except Exception as e:
            print(f"🔑 Authentication Error: Please make sure you have added 'GOOGLE_API_KEY'")

# build datacollector,trendanalyzer,reportgenerator agents
def buildagents():
    agent1=data_collector_agent()
    agent2=trend_analyzer_agent()
    agent3=report_generator_agent()
    return agent1,agent2,agent3

# procedure to run an agent
async def run_agent(question: str) -> str:    
    #call build agents on every run becuase user may select diffrent inputs
    datacollector,trendanalyzer,reportgenerator=buildagents()
    
    #create sequential agent
    agent = SequentialAgent(
    name="FinanceReportPipeline",
    sub_agents=[datacollector,trendanalyzer,reportgenerator,],
    )   
    
    #run the agent
    runner = InMemoryRunner(agent=agent)
    events = await runner.run_debug(question)

    # ADK returns a list of Event objects
    try:        
        answer = events[4].content.parts[0].text
    except Exception as e:
        answer = f"❌ Could not extract output: {e}"
    
    return answer






