from crewai import Crew, Process
from src.tasks.task import create_research_task
from src.agents.agent import create_researcher



def run_research(task_description, selection):
    
    researcher = create_researcher(selection)
    task = create_research_task(task_description, selection)
    
    crew = Crew(
        agents= [researcher],
        tasks= [task],
        verbose= True,
        process= Process.sequential
    )
    
    return crew.kickoff()

