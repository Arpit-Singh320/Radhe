from google.adk.agents import Agent
from Radhe.sub_agents.expense_manager import prompt
from Radhe.tools.search import google_search_grounding

expense_manager_agent = Agent(
    model="gemini-2.5-flash",
    name="expense_manager_agent",
    description="Estimate travel expenses based on the itinerary, optimize for cost-efficiency, and suggest ways to stay within the budget.",
    instruction=prompt.EXPENSE_MANAGER_AGENT_INSTR,
    tools=[google_search_grounding],
)
