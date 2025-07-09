from google.adk.agents import Agent
from Radhe.sub_agents.local_guide import prompt
from Radhe.tools.search import google_search_grounding

local_guide_agent = Agent(
    model="gemini-2.5-flash",
    name="local_guide_agent",
    description="Provide local cultural insights, must-visit attractions, restaurant recommendations, and event details for the destination.",
    instruction=prompt.LOCAL_GUIDE_AGENT_INSTR,
    tools=[google_search_grounding],
)
