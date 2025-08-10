# Assignment 12: Satellite Image Cloud Detection via Azure OpenAI Inference

## Overview
This project implements a lightweight, user-friendly interface for satellite image cloud detection using Azure OpenAI's Large Language Model (LLM). The application automatically classifies satellite images as either "Cloudy" or "Clear" without requiring users to set up or maintain conventional deep learning models.

## Problem Statement
Manual inspection of satellite imagery to identify cloud-covered scenes is time-consuming and doesn't scale for large datasets. Traditional solutions require deploying or fine-tuning pre-trained image classification models, which can be technically challenging for many users. This application provides a simple, API-driven cloud detection solution suitable for integration into various industries such as media, agriculture, logistics, and climate analytics.

## Features
- **Automatic Image Classification**: Instantly classifies satellite images as "Cloudy" or "Clear"
- **Confidence Scoring**: Provides accuracy percentage for each prediction
- **Multimodal AI**: Leverages Azure OpenAI's vision capabilities for image understanding
- **No Manual Input Required**: Uses predefined sample images (auto-input as per assignment requirements)
- **Structured Output**: Returns results in a consistent, parseable format

## Technical Architecture

### Core Components
1. **Azure OpenAI Integration**: Uses Azure OpenAI API for multimodal inference
2. **Image Processing**: Converts images to base64 format for API transmission
3. **Structured Output**: Implements Pydantic models for consistent response formatting
4. **Error Handling**: Comprehensive error handling for network and API failures

### Key Technologies
- **LangChain**: Framework for LLM application development
- **Azure OpenAI**: Multimodal LLM service for image classification
- **Pillow (PIL)**: Image processing and validation
- **Pydantic**: Data validation and serialization
- **Requests**: HTTP library for image downloading

## Step-by-Step Solution

### 1. Environment Setup
```bash
# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configuration
1. Copy `config_template.py` to `config.py`
2. Fill in your Azure OpenAI credentials:
   - `AZURE_OPENAI_ENDPOINT`: Your Azure OpenAI endpoint URL
   - `AZURE_OPENAI_API_KEY`: Your Azure OpenAI API key
   - `AZURE_DEPLOYMENT_NAME`: Your deployment name (e.g., "GPT-4o-mini")

### 3. Running the Application
```bash
python3 main.py
```

### 4. How It Works
1. **Image Loading**: Downloads sample images from predefined URLs
2. **Preprocessing**: Converts images to base64 format for API transmission
3. **LLM Inference**: Sends images to Azure OpenAI with classification prompt
4. **Result Processing**: Extracts structured classification results
5. **Output Display**: Shows prediction, confidence score, and image metadata

## Sample Images
The application automatically processes three sample satellite images:
1. Cloudy sky image from Pexels
2. Clear sky image from Pexels  
3. Additional satellite imagery for testing

## Expected Output Format
```
============================================================
CLASSIFICATION RESULTS
============================================================
Prediction: Cloudy
Confidence: 92.4%
============================================================
Image dimensions: 1920x1080 pixels
Image mode: RGB
============================================================
```

## LangChain Integration for Multimodal Data

### Multimodal Message Structure
The application demonstrates how to pass both text and image data to LangChain:
```python
message = [
    {
        "role": "system",
        "content": "System prompt for classification..."
    },
    {
        "role": "user", 
        "content": [
            {"type": "text", "text": "Classification instruction"},
            {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{image_data}"}}
        ]
    }
]
```

### Structured Output with Pydantic
```python
class WeatherResponse(BaseModel):
    accuracy: float = Field(description="The accuracy of the result as a percentage")
    result: str = Field(description="The result of the classification")

llm_with_structured_output = llm.with_structured_output(WeatherResponse)
```

## Knowledge and Experience Gained

### 1. Azure OpenAI API Integration
- Understanding of Azure OpenAI endpoint configuration
- API key management and environment variable usage
- Deployment name configuration for different models

### 2. Multimodal AI with LangChain
- How to pass images to LLMs through LangChain
- Structured output formatting for consistent responses
- Error handling in multimodal AI applications

### 3. Image Processing for AI
- Converting images to base64 format for API transmission
- Image validation and metadata extraction
- Handling different image formats and sizes

### 4. Production-Ready Application Design
- Configuration management and security best practices
- Comprehensive error handling and logging
- Modular code structure for maintainability

### 5. Real-World AI Applications
- Understanding of satellite image analysis use cases
- Integration considerations for operational pipelines
- Performance and scalability considerations

## Troubleshooting

### Common Issues
1. **Configuration Errors**: Ensure all Azure OpenAI credentials are properly set
2. **Network Issues**: Check internet connectivity for image downloads
3. **API Limits**: Monitor Azure OpenAI rate limits and quotas
4. **Image Format**: Ensure images are in supported formats (JPEG, PNG)

### Debug Mode
The application includes comprehensive logging to help diagnose issues:
- Image loading status
- LLM setup verification
- Classification progress tracking
- Error details and stack traces

## Future Enhancements
1. **Web Interface**: Streamlit-based GUI for user uploads
2. **Batch Processing**: Handle multiple images simultaneously
3. **Model Fine-tuning**: Custom training for specific satellite imagery
4. **API Endpoint**: RESTful service for integration with other systems
5. **Confidence Thresholds**: Configurable accuracy requirements

## Conclusion
This assignment demonstrates the power of modern LLMs for computer vision tasks without requiring traditional deep learning expertise. By leveraging Azure OpenAI's multimodal capabilities through LangChain, we can build sophisticated image classification systems that are both powerful and accessible to users across various technical skill levels.

The solution showcases best practices in AI application development, including proper configuration management, error handling, and structured output formatting. This foundation can be extended to build more complex satellite image analysis systems for real-world applications in agriculture, climate science, and logistics.
