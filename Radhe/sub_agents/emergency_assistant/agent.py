from google.adk.agents import Agent
from Radhe.sub_agents.emergency_assistant import prompt
from Radhe.tools.search import google_search_grounding

emergency_assistant_agent = Agent(
    model="gemini-2.5-flash",
    name="emergency_assistant_agent",
    description="Provide essential emergency contacts and guidelines for the destination.",
    instruction=prompt.EMERGENCY_ASSISTANT_AGENT_INSTR,
    tools=[google_search_grounding],
)
