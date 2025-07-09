"""Demonstration of Travel AI Conceirge using Agent Development Kit"""

from google.adk.agents import Agent

from Radhe import prompt

from Radhe.sub_agents.booking.agent import booking_agent
from Radhe.sub_agents.in_trip.agent import in_trip_agent
from Radhe.sub_agents.inspiration.agent import inspiration_agent
from Radhe.sub_agents.planning.agent import planning_agent
from Radhe.sub_agents.post_trip.agent import post_trip_agent
from Radhe.sub_agents.pre_trip.agent import pre_trip_agent
from Radhe.sub_agents.local_guide.agent import local_guide_agent
from Radhe.sub_agents.expense_manager.agent import expense_manager_agent
from Radhe.sub_agents.emergency_assistant.agent import emergency_assistant_agent
from Radhe.sub_agents.reporting.agent import report_generation_agent

from Radhe.tools.memory import _load_precreated_itinerary


root_agent = Agent(
    model="gemini-2.5-flash",
    name="root_agent",
    description="Radhe.ai using the services of multiple sub-agents for seamless travel planning and booking",
    instruction=prompt.ROOT_AGENT_INSTR,
    sub_agents=[
        inspiration_agent,
        planning_agent,
        booking_agent,
        pre_trip_agent,
        in_trip_agent,
        post_trip_agent,
        local_guide_agent,
        expense_manager_agent,
        emergency_assistant_agent,
        report_generation_agent,
    ],
    before_agent_callback=_load_precreated_itinerary,
)
