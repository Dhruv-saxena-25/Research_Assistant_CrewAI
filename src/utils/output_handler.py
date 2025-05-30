import streamlit as st
import sys
from contextlib import contextmanager
from io import StringIO
import re


# Output Handler
"""
To capture and clean terminal output and display it live inside a Streamlit app, instead of the browser console or terminal.
"""

class ProcessTerminalOutput:
    
    def __init__(self, container):
        self.container  = container
        self.output_text = ""
        self.seen_lines = set()
        
    def clean_text(self, text):
        
        # Remove ANSI escape codes
        ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
        text = ansi_escape.sub('', text)
        
        # Remove LLM debug messages
        if text.strip().startswith('LiteLLM.Info:') or text.strip().startswith('Provider List:'):
            return None
        
        # Clean up the formatting
        text = text.replace('[1m', '').replace('[95m', '').replace('[92m', '').replace('[00m', '')
        return text
    
    def write(self, text):
        
        cleaned_text = self.clean_text(text)
        if cleaned_text is None:
            return
        
        # Split into lines and process each line
        lines = cleaned_text.split('\n')      # Splits the cleaned text into individual lines.
        new_lines = []                        # Creates a list to store new, unseen lines.
        
        for line in lines:                    # Strips spaces from each line.
            line = line.strip()
            if line and line not in self.seen_lines:   # Only keeps lines that are not empty and haven’t been shown before.
                self.seen_lines.add(line)
                new_lines.append(line)
                
        if new_lines:
            # Add the new lines to the output
            new_content = '\n'.join(new_lines)                      # Joins new lines together.
            self.output_text = f"{self.output_text}\n{new_content}" if self.output_text else new_content   # Appends them to previous output.
            
            # Update the display
            self.container.text(self.output_text)                       # Updates the Streamlit container to display the new content.
    def flush(self):
        """Flush remaining output to the container."""
        if self.output_text:
            self.container.text(self.output_text)      


# This creates a custom with block that redirects stdout to our class.
@contextmanager
def capture_output(container):
    """Capture stdout and redirect it to a Streamlit container."""
    string_io = StringIO()
    output_handler = ProcessTerminalOutput(container)
    old_stdout = sys.stdout
    sys.stdout = container
    try:
        yield string_io
    finally:
        sys.stdout = old_stdout

# Export the capture_output function
__all__ = ['capture_output']
