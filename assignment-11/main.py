"""
Assignment 11: Build an AI Agent for Weather & Search Queries Using Langchain, OpenWeather, and Tavily APIs

This script implements a Langchain-based AI agent that can:
- Handle weather-related queries using OpenWeather API
- Handle web search queries using Tavily Search API
- Route queries to appropriate tools using Langchain's agent capabilities
- Simulate a conversational interface with mock user inputs
"""

import os
from langchain.tools import tool
from langchain_openai import AzureChatOpenAI
from langchain_community.utilities import OpenWeatherMapAPIWrapper
from langchain_tavily import TavilySearch
from langgraph.prebuilt import create_react_agent

# Import configuration
try:
    from config import (
        AZURE_OPENAI_ENDPOINT,
        AZURE_OPENAI_API_KEY,
        AZURE_DEPLOYMENT_NAME,
        OPENWEATHERMAP_API_KEY,
        TAVILY_API_KEY,
        AZURE_OPENAI_API_VERSION
    )
except ImportError:
    print("Error: Please copy config_template.py to config.py and fill in your API keys")
    exit(1)

def setup_environment():
    """Setup environment variables from config"""
    os.environ["AZURE_OPENAI_ENDPOINT"] = AZURE_OPENAI_ENDPOINT
    os.environ["AZURE_OPENAI_API_KEY"] = AZURE_OPENAI_API_KEY
    os.environ["AZURE_DEPLOYMENT_NAME"] = AZURE_DEPLOYMENT_NAME
    os.environ["OPENWEATHERMAP_API_KEY"] = OPENWEATHERMAP_API_KEY
    os.environ["TAVILY_API_KEY"] = TAVILY_API_KEY

def create_weather_tool():
    """Create weather tool using Langchain wrapper"""
    weather = OpenWeatherMapAPIWrapper()
    
    @tool
    def get_weather(city: str) -> str:
        """Get the current weather for a given city.
        
        Args:
            city (str): The name of the city to get the weather for.
            
        Returns:
            str: A string describing the current weather in the specified city.
        """
        print(f"get_weather tool calling: Getting weather for {city}")
        try:
            return weather.run(city)
        except Exception as e:
            return f"Error getting weather for {city}: {str(e)}"
    
    return get_weather

def create_search_tool():
    """Create Tavily search tool"""
    tavily_search_tool = TavilySearch(
        max_results=3,
        topic="general",
    )
    return tavily_search_tool

def create_llm():
    """Initialize Azure OpenAI LLM"""
    try:
        llm = AzureChatOpenAI(
            azure_deployment=os.getenv("AZURE_DEPLOYMENT_NAME"),
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
            api_version=AZURE_OPENAI_API_VERSION,
            api_key=os.getenv("AZURE_OPENAI_API_KEY"),
            temperature=0.1,
        )
        return llm
    except Exception as e:
        print(f"Error initializing Azure OpenAI LLM: {str(e)}")
        return None

def create_agent(llm, tools):
    """Setup Langchain agent with tools"""
    try:
        agent = create_react_agent(
            model=llm,
            tools=tools,
        )
        return agent
    except Exception as e:
        print(f"Error creating agent: {str(e)}")
        return None

def run_conversation(agent):
    """Run the conversation loop with mock user inputs"""
    print("Welcome to the AI Weather & Search Assistant!")
    print("=" * 50)
    
    messages = []
    
    # Mock user questions for automatic input (as required by assignment)
    mock_questions = [
        "What's the weather in Hanoi?",
        "Tell me about the latest news in AI.",
        "Who won the last World Cup?",
        "What's the weather like in London?",
        "Search for information about renewable energy trends.",
        "exit",
    ]
    
    for user_input in mock_questions:
        print(f"\nUser: {user_input}")
        
        if user_input.lower() == "exit":
            print("Goodbye! Thank you for using the AI Assistant.")
            break
        
        # Add user message to conversation history
        messages.append({"role": "user", "content": user_input})
        
        try:
            # Get response from agent
            response = agent.invoke({"messages": messages})
            
            # Extract the last message content
            if response and "messages" in response and response["messages"]:
                ai_response = response["messages"][-1].content
                messages.append({"role": "assistant", "content": ai_response})
                print(f"AI: {ai_response}")
            else:
                print("AI: Sorry, I couldn't process that request.")
                
        except Exception as e:
            error_msg = f"Sorry, I encountered an error: {str(e)}"
            messages.append({"role": "assistant", "content": error_msg})
            print(f"AI: {error_msg}")
        
        print("-" * 50)

def main():
    """Main function to run the AI agent"""
    print("Initializing AI Weather & Search Agent...")
    
    # Setup environment variables
    setup_environment()
    
    # Validate API keys
    if (AZURE_OPENAI_ENDPOINT == "your-azure-openai-endpoint-here" or
        AZURE_OPENAI_API_KEY == "your-azure-openai-api-key-here" or
        OPENWEATHERMAP_API_KEY == "your-openweathermap-api-key-here" or
        TAVILY_API_KEY == "your-tavily-api-key-here"):
        print("Error: Please update config.py with your actual API keys")
        print("Copy config_template.py to config.py and fill in the required values")
        return
    
    # Create tools
    print("Creating weather tool...")
    weather_tool = create_weather_tool()
    
    print("Creating search tool...")
    search_tool = create_search_tool()
    
    # Create LLM
    print("Initializing Azure OpenAI LLM...")
    llm = create_llm()
    if not llm:
        print("Failed to initialize LLM. Please check your Azure OpenAI configuration.")
        return
    
    # Create agent
    print("Setting up Langchain agent...")
    tools = [weather_tool, search_tool]
    agent = create_agent(llm, tools)
    if not agent:
        print("Failed to create agent. Please check your configuration.")
        return
    
    print("Agent setup complete! Starting conversation...")
    print()
    
    # Run the conversation
    run_conversation(agent)

if __name__ == "__main__":
    main()
