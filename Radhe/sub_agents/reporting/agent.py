import os
from google.adk.agents import Agent
from google.adk.tools.function_tool import FunctionTool
from Radhe.sub_agents.reporting.prompt import REPORT_GENERATION_AGENT_INSTR

# --- Tool Definition using @function_tool ---
# This defines the tool as a simple, decorated function. It is stateless and clean.
@FunctionTool
def update_report_section(section_placeholder: str, new_html_content: str) -> str:
    """
    Reads itinerary.html, replaces a placeholder with new content,
    and writes the result back. If the file doesn't exist, it creates it.

    Args:
        section_placeholder: The placeholder to replace (e.g., '__local_guide_content__').
        new_html_content: The new HTML content to insert.

    Returns:
        A string indicating success or failure.
    """
    file_path = "itinerary.html"

    # Create the file with the base template if it doesn't exist.
    if not os.path.exists(file_path):
        try:
            # Extract the template from the shared prompt instructions.
            template_start = REPORT_GENERATION_AGENT_INSTR.find("<!DOCTYPE html>")
            template_end = REPORT_GENERATION_AGENT_INSTR.rfind("</html>") + len("</html>")
            base_template = REPORT_GENERATION_AGENT_INSTR[template_start:template_end]
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(base_template)
        except Exception as e:
            return f"Error: Could not create the initial report file. Details: {e}"

    # Proceed with reading the file, replacing the placeholder, and writing the update.
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            current_content = f.read()

        updated_content = current_content.replace(section_placeholder, new_html_content)

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)

        return f"Successfully updated section '{section_placeholder}' in {file_path}."
    except Exception as e:
        return f"An unexpected error occurred during file update: {e}"


# --- Agent Definition ---
# The Agent class is now much simpler. It just needs to be initialized with the
# instruction prompt and the list of available tools.
class ReportGenerationAgent(Agent):
    def __init__(self, **kwargs):
        """
        Initializes the agent by passing the instructions and the list of tools
        to the parent constructor.
        """
        super().__init__(
            instruction=REPORT_GENERATION_AGENT_INSTR,
            # The tool is the decorated function itself, passed in a list.
            tools=[update_report_section],
            **kwargs
        )


# --- Agent Instantiation ---
# This creates an instance of our ReportGenerationAgent, which is now correctly configured.
report_generation_agent = ReportGenerationAgent(
    model="gemini-2.5-flash",
    name="report_generation_agent",
    description="Generates and updates a polished, interactive HTML report for a travel plan.",
)