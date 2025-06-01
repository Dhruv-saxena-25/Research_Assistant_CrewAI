import streamlit as st 
from crewai import LLM


def get_llm(selection):
    provider = selection['provider']
    model = selection['model']
    
    if provider == "GROQ":
        llm = LLM(
            api_key=st.secrets["GROQ_API_KEY"],
            model=f"groq/{model}"
        )
        
    elif provider == "Ollama":
        llm = LLM(
            base_url="http://localhost:11434",
            model=f"ollama/{model}",
        )
    
    elif provider == "Google":
        llm = LLM(
            api_key= st.secrets['GEMINI_API_KEY'],
            model= f"gemini/{model}")
    else:
        # Map friendly names to concrete model names for OpenAI
        if model == "GPT-3.5":
            model = "gpt-3.5-turbo"
        elif model == "GPT-4":
            model = "gpt-4"
        elif model == "o1":
            model = "o1"
        elif model == "o1-mini":
            model = "o1-mini"
        elif model == "o1-preview":
            model = "o1-preview"
        # If model is custom but empty, fallback
        if not model:
            model = "o1"
        llm = LLM(
            api_key=st.secrets["OPENAI_API_KEY"],
            model=f"openai/{model}"
        )
    return llm  

