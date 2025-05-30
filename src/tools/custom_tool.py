from typing import Type
from crewai.tools import BaseTool
from pydantic import BaseModel, Field
import requests
from requests.exceptions import HTTPError
import streamlit as st

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
            "x-api-key": st.secrets["EXA_API_KEY"]
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
