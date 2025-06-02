from crewai import Task
from src.agents.agent import create_researcher

def create_research_task(task_description, selection):
    
    researcher = create_researcher(selection)
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
        output_file= "output/research_report.md"
    )