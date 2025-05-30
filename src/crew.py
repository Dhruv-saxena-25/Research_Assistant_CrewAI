from crewai import Crew, Process
from src.tasks.task import create_research_task
from src.agenets.agent import create_researcher



def run_research(llm, selection):
    
    researcher = create_researcher(llm, selection)
    task = create_research_task()
    
    crew = Crew(
        agents= [researcher],
        tasks= [task],
        verbose= True,
        process= Process.sequential
    )
    
    return crew.kickoff()

