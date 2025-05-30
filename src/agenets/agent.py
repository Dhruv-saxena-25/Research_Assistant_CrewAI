from crewai import Agent
from src.llms.init_llms import get_llm
from src.tools.custom_tool import EXAAnswerTool

def create_researcher(selection):
    
    researcher = Agent(
        role= "Research Analyst",
        goal= "Conduct thorough research on given topics for the current year 2025",
        backstory= "Expert at analyzing and summarizing complex information",
        tools= [EXAAnswerTool()],
        llm= get_llm(selection),
        verbose= True,
        allow_delegation= False
    )
    return researcher


