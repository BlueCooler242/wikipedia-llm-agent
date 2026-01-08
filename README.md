# Simple LLM Agent with Wikipedia Tool (LangGraph)

This repository contains a minimal working example of an LLM Agent using the **LangGraph’s ReAct pattern** and a **Wikipedia search tool**. For this example, we use OpenRouter, which provides access to multiple models, including free models, behind a single API. This allows you to run the agent without adding a credit card.

# Step 1: Create an OpenRouter account

Go to the OpenRouter website and sign up with an email or GitHub account.

# Step 2: Generate an API key

Once logged in: <br/>

- Open your account dashboard
- Navigate to API Keys
- Create a new key
- Copy & save the key. You will only see it once!
  
# Step 3: Add the key to your .env file
OPENROUTER_API_KEY=your_openrouter_api_key_here



# Model Choice
This tutorial uses a free OpenRouter model:

model="google/gemini-2.0-flash-exp:free"

# Notes on Free Models

Free models may:

- have rate limits

- be slightly less consistent than paid models

- change availability over time

For learning and experimentation, however, they are more than sufficient.

## What This Agent Does

- Accepts a question from the user
- Uses an LLM to reason about the question
- Automatically decides whether to call Wikipedia
- Returns a final answer to the user

The agent follows the **ReAct pattern**:
> Reason → Act (use tool if needed) → Observe → Answer

## Environment Variables

This agent uses an API key provided via an environment file.

An example file is provided: 

example.env
> OPENROUTER_API_KEY=your_api_key_here


# Project Files

├── wikipedia_llm_agent.py - The agent implementation <br/>
├── example.env - Environment variable template <br/>
├── requirements.txt - Python dependencies <br/>
└── README.md

# Documentation
**Wikipedia Tool** 
- https://notes.kodekloud.com/docs/LangChain/Using-Tools/Using-Wikipedia-Tool

**Langchain**
- https://docs.langchain.com/?_gl=1*ubhsi*_gcl_au*MTU5NDcxMzk5Ni4xNzY3ODAyMjM2

**Openrouter**
- https://openrouter.ai/


```python

```
