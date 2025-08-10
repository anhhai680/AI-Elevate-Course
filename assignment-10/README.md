# Assignment 10: Using Pinecone to Retrieve Top 3 Most Similar Product Records

## Overview
This assignment demonstrates how to use Pinecone vector database to store product embeddings and perform similarity search to find the most similar products based on text descriptions.

## Features
- ✅ Initialize Pinecone client and create index
- ✅ Upsert sample product vectors with embeddings
- ✅ Perform similarity search queries
- ✅ Retrieve top 3 most similar products
- ✅ Comprehensive logging and error handling
- ✅ Auto-input queries (no manual input required)

## Prerequisites
- Python 3.8+
- Azure OpenAI API access
- Pinecone API access

## Installation

### 1. Clone and Setup
```bash
cd assignment-10
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure API Keys
1. Copy `config_template.py` to `config.py`
2. Fill in your actual API keys:
   - Azure OpenAI endpoint and API key
   - Pinecone API key

**Important**: Never commit real API keys to version control!

## Usage

### Basic Usage
```bash
python assignment_10_solution.py
```

### Expected Output
The script will:
1. Create/connect to a Pinecone index
2. Upsert 5 sample product vectors
3. Run 5 sample queries automatically
4. Display top 3 similar products for each query
5. Log all operations to `assignment_10_logs.log`

### Sample Queries (Auto-generated)
- "clothing item for summer"
- "comfortable daily wear"
- "stylish formal outfit"
- "warm winter clothing"
- "casual weekend wear"

## Sample Product Dataset
The script includes the exact product dataset from the assignment:
- **prod1**: Red T-Shirt - Comfortable cotton t-shirt in bright red
- **prod2**: Blue Jeans - Stylish denim jeans with relaxed fit
- **prod3**: Black Leather Jacket - Genuine leather jacket with classic style
- **prod4**: White Sneakers - Comfortable sneakers perfect for daily wear
- **prod5**: Green Hoodie - Warm hoodie made of organic cotton

## Architecture

### ProductSimilarityEngine Class
- **`__init__()`**: Initialize clients and environment
- **`create_index()`**: Create/connect to Pinecone index
- **`upsert_products()`**: Add product vectors to index
- **`search_similar_products()`**: Query for similar products
- **`display_results()`**: Format and display results
- **`run_demo()`**: Execute complete demonstration

### Key Components
1. **Azure OpenAI Client**: Generates text embeddings
2. **Pinecone Client**: Manages vector database operations
3. **Logging System**: Tracks all operations and errors
4. **Error Handling**: Comprehensive exception management

## Configuration Options

### Environment Variables
```bash
export AZURE_OPENAI_ENDPOINT="your-endpoint"
export AZURE_OPENAI_API_KEY="your-key"
export AZURE_DEPLOYMENT_NAME="text-embedding-3-small"
export PINECONE_API_KEY="your-pinecone-key"
```

### Index Settings
- **Dimension**: 1536 (text-embedding-3-small output size)
- **Cloud**: AWS (configurable)
- **Region**: us-east-1 (configurable)

## Troubleshooting

### Common Issues
1. **API Key Errors**: Verify your API keys are correct
2. **Index Creation Fails**: Check Pinecone account limits and permissions
3. **Embedding Generation Fails**: Verify Azure OpenAI service status
4. **Connection Timeouts**: Check network connectivity and firewall settings

### Debug Mode
Enable detailed logging by modifying the logging level in the script:
```python
logging.basicConfig(level=logging.DEBUG)
```

## Files Structure
```
assignment-10/
├── assignment_10_solution.py    # Main solution script
├── config_template.py           # Configuration template
├── requirements.txt             # Python dependencies
├── README.md                   # This file
├── assignment_10_logs.log      # Generated logs (after first run)
└── venv/                       # Virtual environment
```

## Dependencies
- `pinecone-client`: Pinecone vector database client
- `openai`: Azure OpenAI client for embeddings
- `PyPDF2`: PDF reading (for assignment document)

## Assignment Requirements Checklist
- ✅ Pinecone client initialization
- ✅ Index creation and configuration
- ✅ Sample data upserting
- ✅ Similarity search implementation
- ✅ Top 3 results retrieval
- ✅ Proper resource management
- ✅ Error handling
- ✅ Auto-input queries (no manual input)
- ✅ Console output demonstration
- ✅ Logging implementation

## Notes
- The script uses Azure OpenAI for text embeddings (as specified in assignment)
- All queries are automatically generated (no user input required)
- Comprehensive logging is implemented for debugging and demonstration
- The solution follows Python best practices and includes proper documentation

## Support
For issues or questions:
1. Check the logs in `assignment_10_logs.log`
2. Verify API keys and service status
3. Review error messages for specific guidance
