from typing import Type
from crewai import Agent, Task, Crew, Process, LLM
from crewai.tools import BaseTool
from pydantic import BaseModel, Field
import requests
from requests.exceptions import HTTPError
import os
from dotenv import load_dotenv


load_dotenv()

openai_api_key = os.environ['OPENAI_API_KEY']
exa_api_key = os.environ['EXA_API_KEY']
gemini_api_key= os.environ['GEMINI_API_KEY'] 


class EXAAnswerToolSchema(BaseModel):
    query: str = Field(..., description="The question you want to ask Exa.")
    
class EXAAnswerTool(BaseTool):
    name: str = "Ask EXA a question"
    description: str = "A tool that asks Exa a question and returns the answer."
    args_schema: Type[BaseModel] = EXAAnswerToolSchema
    answer_url: str = "https://api.exa.ai/answer" 
    
    def _run(self, query: str):
        
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "x-api-key": exa_api_key
        }
        
        
        try: 
            response= requests.post(
                self.answer_url,
                json= {"query": query, "text": True},
                headers= headers
            )
        
        except HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Log the HTTP error
            print(f"Response content: {response.content}")  # Log the response content for more details
            raise
        
        except Exception as err:
            print(f"Other error occurred: {err}")  # Log any other errors
            raise
        
        response_data = response.json()
        
        answer = response_data["answer"]
        
        citations = response_data.get("citations", [])
        
        output = f'Answer: {answer}\n\n'
        
        if citations:
            output += "Citations:\n"
            for citation in citations:
                output += f"- {citation['title']} ({citation['url']})\n"

        return output
    
    
llm = LLM(
    api_key= gemini_api_key,
    model="gemini/gemini-1.5-flash",
    temperature=0.7,
)


def create_researcher():
    """Create a research agent with the specified LLM configuration."""
    researcher = Agent(
        role= "Research Analyst",
        goal= "Conduct thorough research on given topics for the current year 2025",
        backstory= "Expert at analyzing and summarizing complex information",
        tools= [EXAAnswerTool()],
        llm= llm,
        verbose= True,
        allow_delegation= False
    )
    return researcher


def create_research_task(researcher, task_description):
    return Task(
        description=task_description,
        expected_output="""A comprehensive research report for the year 2025. 
        The report must be detailed yet concise, focusing on the most significant and impactful findings.
        
        Format the output in clean markdown (without code block markers or backticks) using the following structure:

        # Executive Summary
        - Brief overview of the research topic (2-3 sentences)
        - Key highlights and main conclusions
        - Significance of the findings

        # Key Findings
        - Major discoveries and developments
        - Market trends and industry impacts
        - Statistical data and metrics (when available)
        - Technological advancements
        - Challenges and opportunities

        # Analysis
        - Detailed examination of each key finding
        - Comparative analysis with previous developments
        - Industry expert opinions and insights
        - Market implications and business impact

        # Future Implications
        - Short-term impacts (next 6-12 months)
        - Long-term projections
        - Potential disruptions and innovations
        - Emerging trends to watch

        # Recommendations
        - Strategic suggestions for stakeholders
        - Action items and next steps
        - Risk mitigation strategies
        - Investment or focus areas

        # Citations
        - List all sources with titles and URLs
        - Include publication dates when available
        - Prioritize recent and authoritative sources
        - Format as: "[Title] (URL) - [Publication Date if available]"

        Note: Ensure all information is current and relevant to 2025. Include specific dates, 
        numbers, and metrics whenever possible to support findings. All claims should be properly 
        cited using the sources discovered during research.
        """,
        
        agent= researcher,
        output_file= "research_report.md"
    )
    
def run_research(researcher, task):    
    crew = Crew(
        agents= [researcher],
        tasks= [task],
        verbose= True,
        process= Process.sequential
    )
    
    return crew.kickoff()

# app.py

def main():
    task_description = "Research the latest AI Agent news in 2025 and summarize each."

    researcher = create_researcher()
    task = create_research_task(researcher, task_description)
    result = run_research(researcher, task)

    print("\nResearch Completed. Output saved to:", task.output_file)

if __name__ == "__main__":
    main()

