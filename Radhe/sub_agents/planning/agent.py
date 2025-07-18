"""Planning agent. A pre-booking agent covering the planning part of the trip."""

from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool
from google.genai.types import GenerateContentConfig
from Radhe.shared_libraries import types
from Radhe.sub_agents.planning import prompt
from Radhe.sub_agents.reporting import agent as reporting_agent_factory
from Radhe.sub_agents.local_guide import agent as local_guide_agent_factory
from Radhe.sub_agents.expense_manager import agent as expense_manager_agent_factory
from Radhe.sub_agents.emergency_assistant import (
    agent as emergency_assistant_agent_factory,
)
from Radhe.tools.memory import memorize


itinerary_agent = Agent(
    model="gemini-2.5-flash",
    name="itinerary_agent",
    description="Create and persist a structured JSON representation of the itinerary",
    instruction=prompt.ITINERARY_AGENT_INSTR,
    disallow_transfer_to_parent=True,
    disallow_transfer_to_peers=True,
    output_schema=types.Itinerary,
    output_key="itinerary",
    generate_content_config=types.json_response_config,
)


hotel_room_selection_agent = Agent(
    model="gemini-2.5-flash",
    name="hotel_room_selection_agent",
    description="Help users with the room choices for a hotel",
    instruction=prompt.HOTEL_ROOM_SELECTION_INSTR,
    disallow_transfer_to_parent=True,
    disallow_transfer_to_peers=True,
    output_schema=types.RoomsSelection,
    output_key="room",
    generate_content_config=types.json_response_config,
)

hotel_search_agent = Agent(
    model="gemini-2.5-flash",
    name="hotel_search_agent",
    description="Help users find hotel around a specific geographic area",
    instruction=prompt.HOTEL_SEARCH_INSTR,
    disallow_transfer_to_parent=True,
    disallow_transfer_to_peers=True,
    output_schema=types.HotelsSelection,
    output_key="hotel",
    generate_content_config=types.json_response_config,
)


flight_seat_selection_agent = Agent(
    model="gemini-2.5-flash",
    name="flight_seat_selection_agent",
    description="Help users with the seat choices",
    instruction=prompt.FLIGHT_SEAT_SELECTION_INSTR,
    disallow_transfer_to_parent=True,
    disallow_transfer_to_peers=True,
    output_schema=types.SeatsSelection,
    output_key="seat",
    generate_content_config=types.json_response_config,
)

flight_search_agent = Agent(
    model="gemini-2.5-flash",
    name="flight_search_agent",
    description="Help users find best flight deals",
    instruction=prompt.FLIGHT_SEARCH_INSTR,
    disallow_transfer_to_parent=True,
    disallow_transfer_to_peers=True,
    output_schema=types.FlightsSelection,
    output_key="flight",
    generate_content_config=types.json_response_config,
)


planning_agent = Agent(
    model="gemini-2.5-flash",
    description="""Helps users with travel planning, complete a full itinerary for their vacation, finding best deals for flights and hotels.""",
    name="planning_agent",
    instruction=prompt.PLANNING_AGENT_INSTR,
    tools=[
        AgentTool(agent=flight_search_agent),
        AgentTool(agent=flight_seat_selection_agent),
        AgentTool(agent=hotel_search_agent),
        AgentTool(agent=hotel_room_selection_agent),
        AgentTool(agent=local_guide_agent_factory.local_guide_agent),
        AgentTool(agent=expense_manager_agent_factory.expense_manager_agent),
        AgentTool(
            agent=emergency_assistant_agent_factory.emergency_assistant_agent
        ),
        AgentTool(agent=itinerary_agent),
        AgentTool(agent=reporting_agent_factory.report_generation_agent),
        memorize,
    ],
    generate_content_config=GenerateContentConfig(
        temperature=0.1, top_p=0.5
    )
)
