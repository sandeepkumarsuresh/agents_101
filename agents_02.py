"""
Author: Sandeep Kumar Suresh

Code to connect to local db and retrieve data

After executing this module,
1. Connect to tools and DB using MCP.
2. Make your own MCP server and make the agent retrieve information from it.

"""

from langchain_community.tools.sql_database.tool import QuerySQLDataBaseTool
from langchain_community.utilities import SQLDatabase
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import initialize_agent, AgentType

from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Get the API key from the environment
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY not found in .env file") 


# Load local SQLite file
db = SQLDatabase.from_uri("sqlite:///farm.db")

# SQL query tool
sql_tool = QuerySQLDataBaseTool(db=db)

# Gemini model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash-001",
)
# Create an agent with SQL tool
agent = initialize_agent(
    tools=[sql_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)


answer = agent.run("Which crop needs high water?")
print("\nANSWER:", answer)
