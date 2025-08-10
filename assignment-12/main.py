"""
Assignment 12: Satellite Image Cloud Detection via Azure OpenAI Inference

This application classifies satellite images as either "Cloudy" or "Clear" using Azure OpenAI.
It accepts satellite images as input and returns a classification label with confidence score.
"""

import os
import base64
import requests
from PIL import Image
from langchain_openai import AzureChatOpenAI
from pydantic import BaseModel, Field
from config import (
    AZURE_OPENAI_ENDPOINT,
    AZURE_OPENAI_API_KEY,
    AZURE_DEPLOYMENT_NAME,
    AZURE_OPENAI_API_VERSION
)

# Set environment variables for Azure OpenAI
os.environ["AZURE_OPENAI_ENDPOINT"] = AZURE_OPENAI_ENDPOINT
os.environ["AZURE_OPENAI_API_KEY"] = AZURE_OPENAI_API_KEY
os.environ["AZURE_DEPLOYMENT_NAME"] = AZURE_DEPLOYMENT_NAME

# Output Schema for structured response
class WeatherResponse(BaseModel):
    accuracy: float = Field(description="The accuracy of the result as a percentage")
    result: str = Field(description="The result of the classification: either 'Clear' or 'Cloudy'")

def setup_llm():
    """Setup Azure OpenAI LLM with structured output"""
    try:
        llm = AzureChatOpenAI(
            azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
            azure_deployment=os.environ["AZURE_DEPLOYMENT_NAME"],
            api_key=os.environ["AZURE_OPENAI_API_KEY"],
            api_version=AZURE_OPENAI_API_VERSION,
        )
        
        # Enable structured output
        llm_with_structured_output = llm.with_structured_output(WeatherResponse)
        return llm_with_structured_output
    except Exception as e:
        print(f"Error setting up LLM: {e}")
        return None

def load_image_from_url(image_url):
    """Load image from URL and convert to base64"""
    try:
        print(f"Loading image from: {image_url}")
        response = requests.get(image_url)
        response.raise_for_status()
        
        image_bytes = response.content
        image_data_base64 = base64.b64encode(image_bytes).decode("utf-8")
        
        # Verify image can be opened
        image = Image.open(requests.get(image_url, stream=True).raw)
        print(f"Image loaded successfully: {image.size[0]}x{image.size[1]} pixels")
        
        return image_data_base64, image
    except Exception as e:
        print(f"Error loading image from URL: {e}")
        return None, None

def classify_image(llm, image_data_base64):
    """Classify the satellite image using Azure OpenAI"""
    try:
        # Construct the message with multimodal data
        message = [
            {
                "role": "system",
                "content": """Based on the satellite image provided, classify the scene as either:
                'Clear' (no clouds) or 'Cloudy' (with clouds).
                Respond with only one word: either 'Clear' or 'Cloudy' and Accuracy.
                Do not provide explanations."""
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Classify the scene as either: 'Clear' or 'Cloudy' and Accuracy."
                    },
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/jpeg;base64,{image_data_base64}"}
                    }
                ]
            }
        ]
        
        # Call Azure OpenAI for classification
        result = llm.invoke(message)
        return result
    except Exception as e:
        print(f"Error during classification: {e}")
        return None

def display_result(image, prediction, accuracy):
    """Display the image with prediction results"""
    print("\n" + "="*60)
    print("CLASSIFICATION RESULTS")
    print("="*60)
    print(f"Prediction: {prediction}")
    print(f"Confidence: {accuracy:.1f}%")
    print("="*60)
    
    # Display image info
    if image:
        print(f"Image dimensions: {image.size[0]}x{image.size[1]} pixels")
        print(f"Image mode: {image.mode}")
    print("="*60)

def main():
    """Main function to run the satellite image cloud detection"""
    print("Assignment 12: Satellite Image Cloud Detection via Azure OpenAI")
    print("="*70)
    
    # Check if configuration is set up
    if (AZURE_OPENAI_ENDPOINT == "your-azure-openai-endpoint-here" or 
        AZURE_OPENAI_API_KEY == "your-azure-openai-api-key-here"):
        print("ERROR: Please configure your Azure OpenAI credentials in config.py")
        print("Copy config_template.py to config.py and fill in your actual API keys")
        return
    
    # Setup LLM
    print("Setting up Azure OpenAI LLM...")
    llm = setup_llm()
    if not llm:
        print("Failed to setup LLM. Exiting.")
        return
    print("LLM setup successful!")
    
    # Sample satellite images for testing (auto-input as required)
    sample_images = [
        "https://images.pexels.com/photos/53594/blue-clouds-day-fluffy-53594.jpeg?cs=srgb&dl=pexels-pixabay-53594.jpg&fm=jpg",
        "https://images.pexels.com/photos/1287145/pexels-photo-1287145.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
        "https://images.pexels.com/photos/1287146/pexels-photo-1287146.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    ]
    
    print(f"\nProcessing {len(sample_images)} sample images...")
    
    for i, image_url in enumerate(sample_images, 1):
        print(f"\n--- Processing Image {i}/{len(sample_images)} ---")
        
        # Load image from URL
        image_data_base64, image = load_image_from_url(image_url)
        if not image_data_base64:
            print(f"Skipping image {i} due to loading error")
            continue
        
        # Classify the image
        print("Classifying image using Azure OpenAI...")
        result = classify_image(llm, image_data_base64)
        
        if result:
            # Display results
            display_result(image, result.result, result.accuracy)
        else:
            print(f"Failed to classify image {i}")
        
        print(f"--- Completed Image {i}/{len(sample_images)} ---\n")
    
    print("All images processed successfully!")
    print("="*70)

if __name__ == "__main__":
    main()
