#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
LLM Agent with Wikipedia Tool using LangGraph
This agent can decide when to use Wikipedia to answer questions
"""
import os
import sys


# Add current directory to Python path
sys.path.append(os.getcwd())

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent

# wikipedia tool imports
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper

# -------------------------
# Setup Wikipedia Tool
# -------------------------
api_wrapper = WikipediaAPIWrapper(
    top_k_results=1,
    doc_content_chars_max=300
)
wikipedia_tool = WikipediaQueryRun(api_wrapper=api_wrapper)
TOOLS = [wikipedia_tool]


# -------------------------
# Load environment variables
# -------------------------
load_dotenv("example.env")

# -------------------------
# Initialize LLM (Free OpenRouter model)
# -------------------------
llm = ChatOpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    model="google/gemini-2.0-flash-exp:free",
    temperature=0
)

# -------------------------
# Create ReAct Agent with Wikipedia Tool
# -------------------------
# The agent will autonomously decide when to use Wikipedia
agent = create_react_agent(llm, TOOLS)

# -------------------------
# Function to query agent
# -------------------------
def run_agent(query: str) -> str:
    """
    Run the LLM agent with Wikipedia tool access.
    The agent will autonomously decide whether to call the tool.
    
    Args:
        query: The user's question
        
    Returns:
        The agent's final answer
    """
    result = agent.invoke({"messages": [("user", query)]})
    
    # Extract the final message content from the agent
    final_message = result["messages"][-1]
    return final_message.content

# -------------------------
# CLI usage
# -------------------------
if __name__ == "__main__":
    print("=" * 60)
    print("Wikipedia LLM Agent")
    print("=" * 60)
    print("This agent can search Wikipedia to answer your questions.")
    print("Type 'exit' to quit.\n")
    
    while True:
        user_input = input("\nAsk a research question: ")
        if user_input.lower() == "exit":
            print("\nGoodbye!")
            break
        
        try:
            answer = run_agent(user_input)
            print("\n" + "=" * 60)
            print("Answer:")
            print("=" * 60)
            print(answer)
        except Exception as e:
            print(f"\nError: {str(e)}")
            print("Please check your API key and internet connection.")

