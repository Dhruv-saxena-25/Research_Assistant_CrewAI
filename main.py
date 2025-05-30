import streamlit as st
import os
from src.UI.sidebar import render_sidebar
from src.agenets.agent import create_researcher
from src.tasks.task import create_research_task
from src.crew import run_research
from src.utils.output_handler import capture_output
from src.llms.init_llms import get_llm


# Streamlit App 

# Configure the page
st.set_page_config(
    page_title="Research Assistant",
    page_icon="🕵️‍♂️",
    layout="wide",
    initial_sidebar_state="expanded"
)



# Main Layout 
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.title("🔍 Research Assistant", anchor=False)

# Render sidebar and get selection (provider and model)
selection = render_sidebar()


# Check if API keys are set based on provider
if selection["provider"] == "OpenAI":
    if not os.environ.get("OPENAI_API_KEY"):
        st.warning("⚠️ Please enter your OpenAI API key in the sidebar to get started")
        st.stop()
elif selection["provider"] == "GROQ":
    if not os.environ.get("GROQ_API_KEY"):
        st.warning("⚠️ Please enter your GROQ API key in the sidebar to get started")
        st.stop()

# Check EXA key for non-Ollama providers
if selection["provider"] != "Ollama":
    if not os.environ.get("EXA_API_KEY"):
        st.warning("⚠️ Please enter your EXA API key in the sidebar to get started")
        st.stop()

# Add Ollama check
if selection["provider"] == "Ollama" and not selection["model"]:
    st.warning("⚠️ No Ollama models found. Please make sure Ollama is running and you have models loaded.")
    st.stop()

## Init LLM
llm = get_llm(selection)

# Create two columns for the input section
input_col1, input_col2, input_col3 = st.columns([1, 3, 1])
with input_col2:
    task_description = st.text_area(
        "What would you like to research?",
        value="Research the latest AI Agent news in February 2025 and summarize each.",
        height=68
    )
    
col1, col2, col3 = st.columns([1, 0.5, 1])
with col2:
    start_research = st.button("🚀 Start Research", use_container_width=False, type="primary")
    
if start_research:
    with st.status("🤖 Researching...", expanded=True) as status:
        try:
            # Create persistent container for process output with fixed height.
            process_container = st.container(height=300, border=True)
            output_container = process_container.container()
            
            # Single output capture context.
            with capture_output(output_container):
                researcher = create_researcher(selection)
                task = create_research_task(task_description, selection)
                result = run_research(task_description, selection)
                status.update(label="✅ Research completed!", state="complete", expanded=False)
        except Exception as e:
            status.update(label="❌ Error occurred", state="error")
            st.error(f"An error occurred: {str(e)}")
            st.stop()
    
    # Convert CrewOutput to string for display and download
    result_text = str(result)
    
    # Display the final result
    st.markdown(result_text)
    
    # Create download buttons
    st.divider()
    download_col1, download_col2, download_col3 = st.columns([1, 2, 1])
    with download_col2:
        st.markdown("### 📥 Download Research Report")
        
        # Download as Markdown
        st.download_button(
            label="Download Report",
            data=result_text,
            file_name="research_report.md",
            mime="text/markdown",
            help="Download the research report in Markdown format"
        )

# Add footer
st.divider()
footer_col1, footer_col2, footer_col3 = st.columns([1, 2, 1])
with footer_col2:
    st.caption("Made By Dhruv Saxena using [CrewAI](https://crewai.com), [Exa](https://exa.ai) and [Streamlit](https://streamlit.io)")
    
    