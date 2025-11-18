"""
Author: Sandeep Kumar Suresh

The below code does observability for agent_01.py. Create a laminar account and view the observability

Practice Question

1. Do the below for agents_02.py and view the observability in the platform

"""
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import initialize_agent, AgentType
from langchain.tools import tool


from dotenv import load_dotenv
import os

from lmnr import Laminar
Laminar.initialize()    # Uses LMNR_PROJECT_API_KEY
laminar = Laminar()

# Load .env file
load_dotenv()

# Get the API key from the environment
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY not found in .env file") 


@tool
def text_length_tool(text: str) -> int:
    """Returns the number of characters in the given text."""
    return len(text)


# Create Gemini model
model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.2
)

# Create agent with tools
agent = initialize_agent(
    tools=[text_length_tool],
    llm=model,
    agent=AgentType.OPENAI_FUNCTIONS,   
    verbose=True
)

response = agent.run("How many characters are in the text 'Vanakkam'?")
print(response)


