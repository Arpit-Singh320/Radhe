from google.adk.agents import Agent
from Radhe.sub_agents.itinerary import prompt

itinerary_agent = Agent(
    model="gemini-2.5-flash",
    description="Compiles all travel information into a final itinerary.",
    name="itinerary_agent",
    instruction=prompt.ITINERARY_AGENT_INSTR,
    tools=[],
)
