# Assignment 11: AI Agent for Weather & Search Queries

## Overview

This assignment implements a Langchain-based AI agent that can handle real-time weather and web search queries. The agent integrates with OpenWeather API for weather information and Tavily Search API for web search capabilities, using Langchain's tool routing to automatically select the appropriate tool for each query.

## Features

- **Weather Tool**: Get current weather information for any city using OpenWeather API
- **Search Tool**: Perform real-time web searches using Tavily Search API
- **Intelligent Routing**: Langchain agent automatically routes queries to the appropriate tool
- **Conversational Interface**: Simulates a chat interface with mock user inputs
- **Error Handling**: Robust error handling for API failures and configuration issues

## Prerequisites

- Python 3.8 or higher
- Azure OpenAI Resource with API key, endpoint URL, and deployment name
- OpenWeather API key ([Get it here](https://openweathermap.org/api))
- Tavily API key ([Get it here](https://app.tavily.com/))

## Installation

1. **Clone or download this repository**

2. **Install required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Setup configuration**:
   - Copy `config_template.py` to `config.py`
   - Fill in your actual API keys in `config.py`:
     ```python
     AZURE_OPENAI_ENDPOINT = "your-actual-endpoint"
     AZURE_OPENAI_API_KEY = "your-actual-api-key"
     AZURE_DEPLOYMENT_NAME = "your-deployment-name"
     OPENWEATHERMAP_API_KEY = "your-openweather-api-key"
     TAVILY_API_KEY = "your-tavily-api-key"
     ```

## Usage

Run the AI agent:

```bash
python3 main.py
```

The agent will automatically process a series of mock questions including:
- Weather queries for different cities
- Web search queries for various topics
- Mixed queries to demonstrate tool routing

## How It Works

### 1. Tool Creation
- **Weather Tool**: Uses `OpenWeatherMapAPIWrapper` to fetch weather data
- **Search Tool**: Uses `TavilySearch` for real-time web search results

### 2. Agent Setup
- Initializes Azure OpenAI LLM with your configuration
- Creates a React-style agent using `create_react_agent`
- Combines both tools for intelligent query routing

### 3. Query Processing
- User queries are automatically routed to appropriate tools
- Weather-related questions → OpenWeather API
- Search-related questions → Tavily Search API
- Agent maintains conversation history for context

### 4. Response Generation
- Agent processes tool outputs and generates user-friendly responses
- Maintains chat history for conversational continuity
- Handles errors gracefully with informative messages

## Code Structure

```
main.py              # Main application with AI agent implementation
config.py            # Configuration file with API keys (create from template)
config_template.py   # Template for configuration
requirements.txt     # Python dependencies
read_pdf.py         # PDF reader utility
README.md           # This file
```

## Key Components

### Weather Tool
```python
@tool
def get_weather(city: str) -> str:
    """Get current weather for a given city"""
    return weather.run(city)
```

### Search Tool
```python
tavily_search_tool = TavilySearch(
    max_results=3,
    topic="general",
)
```

### Agent Creation
```python
agent = create_react_agent(
    model=llm,
    tools=[weather_tool, search_tool],
)
```

## Example Queries

The agent can handle various types of queries:

**Weather Queries:**
- "What's the weather in Hanoi?"
- "What's the weather like in London?"

**Search Queries:**
- "Tell me about the latest news in AI"
- "Who won the last World Cup?"
- "Search for information about renewable energy trends"

## Troubleshooting

### Common Issues

1. **API Key Errors**: Ensure all API keys are correctly set in `config.py`
2. **Import Errors**: Verify all dependencies are installed with `pip install -r requirements.txt`
3. **Azure OpenAI Issues**: Check your endpoint URL and deployment name
4. **Rate Limiting**: Some APIs may have rate limits; check your API provider's documentation

### Error Messages

- **Configuration Error**: Update `config.py` with actual API keys
- **LLM Initialization Error**: Verify Azure OpenAI configuration
- **Tool Creation Error**: Check API key validity and internet connection

## Dependencies

- `langchain`: Core Langchain framework
- `langchain-openai`: Azure OpenAI integration
- `langchain-community`: Community utilities including OpenWeather wrapper
- `langchain-tavily`: Tavily search integration
- `langgraph`: Agent creation and management
- `openai`: OpenAI API client
- `requests`: HTTP library for API calls
- `tiktoken`: Token counting utility
- `pyowm`: OpenWeather API wrapper (alternative)

## Assignment Requirements Met

✅ **Langchain-based AI agent** - Implemented with tool routing  
✅ **OpenWeather API integration** - Weather tool for city queries  
✅ **Tavily Search API integration** - Web search capabilities  
✅ **Tool routing** - Automatic selection of appropriate tools  
✅ **Mock user input** - Automated conversation flow (no manual input)  
✅ **Error handling** - Robust error handling throughout  
✅ **Documentation** - Comprehensive code comments and README  

## Next Steps

To enhance this agent, consider:
- Adding more specialized tools (news, sports, etc.)
- Implementing conversation memory persistence
- Adding response formatting and styling
- Creating a web interface
- Adding user authentication and rate limiting

## Support

If you encounter issues:
1. Check the troubleshooting section above
2. Verify all API keys are correct
3. Ensure all dependencies are installed
4. Check your internet connection and API service status
