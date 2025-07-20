# New Car Models - AI Work Instructions Generator

## 📋 Overview

This Python application generates detailed work instructions for automotive manufacturing tasks using OpenAI's GPT models. It's designed to help automotive manufacturing supervisors create comprehensive, step-by-step assembly instructions for new car model production lines.

## 🚗 Features

- **AI-Powered Instruction Generation**: Leverages OpenAI's GPT models to create detailed work instructions
- **Automotive Manufacturing Focus**: Specialized prompts for automotive assembly tasks
- **Safety-First Approach**: Generated instructions include safety precautions and requirements
- **Tool Requirements**: Automatically identifies and lists required tools for each task
- **Quality Assurance**: Includes acceptance checks and verification steps
- **Configurable Settings**: Flexible configuration through environment variables

## 🛠 Prerequisites

- Python 3.7 or higher
- OpenAI API key
- pip package manager

## 📦 Installation

1. **Clone or download the project:**
   ```bash
   cd new-car-models
   ```

2. **Install required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   Create a `.env` file in the project root and add your OpenAI API key:
   ```env
   OPENAI_API_KEY=your_actual_openai_api_key_here
   OPENAI_MODEL=gpt-4o-mini
   OPENAI_API_BASE=https://api.openai.com/v1
   ```

## 🚀 Usage

### Basic Usage

Run the application to generate work instructions for predefined automotive tasks:

```bash
python main.py
```

### Configuration Options

The application can be configured through environment variables:

- `OPENAI_API_KEY`: Your OpenAI API key (required)
- `OPENAI_MODEL`: The GPT model to use (default: gpt-4o-mini)
- `OPENAI_API_BASE`: OpenAI API base URL (default: https://api.openai.com/v1)

## 📁 Project Structure

```
new-car-models/
├── main.py              # Main application entry point
├── settings.py          # Configuration management
├── requirements.txt     # Python dependencies
├── readme.md           # Project documentation
├── .env                # Environment variables (create this)
└── __pycache__/        # Python cache files
```

## 🔧 Code Structure

### main.py
- Contains predefined automotive manufacturing tasks
- Implements the OpenAI API integration
- Generates and displays work instructions

### settings.py
- Manages application configuration
- Handles environment variable loading
- Provides default values for OpenAI settings