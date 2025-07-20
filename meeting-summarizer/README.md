# Meeting Summarizer

A Python application that uses OpenAI's GPT models to automatically summarize meeting transcripts, extracting key points, decisions, and action items.

## Features

- 🤖 **AI-Powered Summarization**: Leverages OpenAI's GPT models for intelligent meeting summary generation
- 📝 **Key Information Extraction**: Automatically identifies key points, decisions, and action items
- ⚙️ **Configurable Settings**: Support for environment variables and custom model selection
- 📄 **File-Based Input**: Reads meeting transcripts from text files
- 🔧 **Simple Setup**: Minimal configuration required to get started

## Project Structure

```
meeting-summarizer/
├── main.py                    # Main application entry point
├── settings.py               # Configuration management
├── requirements.txt          # Python dependencies
├── README.md                # Project documentation
├── data/
│   └── meeting_transcript.txt # Sample meeting transcript
```

## Prerequisites

- Python 3.7 or higher
- OpenAI API key

## Installation

1. **Clone or download the project**
   ```bash
   cd meeting-summarizer
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   
   Create a `.env` file in the project root:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   OPENAI_MODEL=gpt-4o-mini
   ```

   Or export the variables directly:
   ```bash
   export OPENAI_API_KEY="your_openai_api_key_here"
   export OPENAI_MODEL="gpt-4o-mini"
   ```

## Usage

### Basic Usage

1. **Place your meeting transcript** in the `data/meeting_transcript.txt` file

2. **Run the summarizer**
   ```bash
   python main.py
   ```

3. **View the generated summary** in the console output

### Example Output

```
Meeting Summary: 

**Key Points:**
- Project Alpha MVP deadline confirmed for Friday
- Design handoff completed with all screens finalized in Figma
- Development is 80% complete with API integration pending

**Decisions:**
- Deployment scheduled for Friday 3 PM
- QA testing to begin Wednesday afternoon
- Animation assets to be delivered by EOD today

**Action Items:**
- Jamie: Send animation assets by EOD today
- Taylor: Continue API integration, flag high-risk areas for QA
- Morgan: Prioritize testing of high-risk areas starting Wednesday
- Alex: Send test cases to Morgan by tomorrow
```

## Configuration

The application uses a settings system that supports both environment variables and default values:

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `OPENAI_API_KEY` | Your OpenAI API key | Required |
| `OPENAI_MODEL` | OpenAI model to use | `gpt-4o-mini` |