from google.adk.agents import Agent
from google.adk.tools import google_search  # Import the tool

from .prompts import travel_agent_prompt  # Import the prompt

model = "gemini-2.0-flash-live-001"

# agent to plan travel itinerary using all the data captured by root_Agent
itinerary_agent = Agent(
   name="travel_agent",
   model=model,
   description="Agent which will plan a Travel itinerary using all the data captured by root_Agent.",
   instruction="You are a helpful Agent which helps plan a Travel itinerary using all the data captured by root_Agent. " \
   "Create a day-wise travel itinerary with places to visit, stay and food options.",
)

# google map agent to calculate the distance between all the places planned 
google_map_agent = Agent(
   name="google_map_agent",
   model=model,
   description="Agent which will calculate distance between all the places planned in the itinerary using google maps.",
   instruction="You are a helpful Agent which will calculate distance between all the places planned in the itinerary using google maps. " \
   "Use google maps to get accurate distance and travel time.",
   tools=[google_search],
)

# hotel booking agent to find hotels in the destination city
hotel_booking_agent = Agent(
   name="hotel_booking_agent",
   model="gemini-2.0-flash-live-001",
   description="Agent which will find hotels in the destination city using google search.",
   instruction="You are a helpful Agent which will find hotels in the destination city using google search",
   tools=[google_search],
)

# travel details agent to find travel details to reach destination city
travel_details_agent = Agent(
   name="travel_details_agent",
   model="gemini-2.0-flash-live-001",
   description="Agent which will find travel details which would be best way to reach destination city using google search. " \
   "Provide details about travel duration and cost for each of the mode. " \
   "Depending on user preferences provide details on available flights/train/bus options and Suggest best options based on cost "
   "and travel time. ",
   tools=[google_search],
)

# activity agent to find the activities in the destination city and provides the details on how to book the activities
activity_agent = Agent(
   # A unique name for the agent.
   name="activity_agent",
   model="gemini-2.0-flash-live-001",
   description="Agent which will find the activities in the destination city ",
   instruction="You are a helpful Agent which will find the activities in the destination city using google search "
   "and provides the details on how to book the activities.",
   tools=[google_search],
)

# summarization agent to summarize all the data generated from other agents
summarization_agent = Agent(
   # A unique name for the agent.
   name="summarization_agent",
   model="gemini-2.0-flash-live-001",
   description="Agent which will summarize all the data generated from other agents .",
   instruction="You are a helpful Agent which will summarize all the data generated from other agents and provide a concise summary of the travel itinerary.",
)

# booking agent to help user book hotels, activities and travel tickets
booking_agent = Agent(
   name="booking_agent",
   model="gemini-2.0-flash-live-001",
   description="Agent which will help user to book hotels, activities and travel tickets.",
   instruction="Once user confirms the travel itinerary, you are a helpful Agent which will help user to book hotels, activities and travel tickets.",
)

#Orchestration agent which will collect all the required information from user and then call relavent agents to plan travel iternary
orchestration = Agent(
   name="google_search_agent",
   model="gemini-2.0-flash-live-001",
   description="Orchestration Agent which will gather information from user and then call other agents to plan travel itinerary.",
   instruction=travel_agent_prompt,
   # Add google_search tool to perform grounding with Google search.
   #sub_agents=[travel_agent, google_map_agent, hotel_booking_agent, activity_agent],
   tools=[google_search],
)

root_agent = activity_agent;