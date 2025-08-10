"""
Assignment 10: Using Pinecone to Retrieve Top 3 Most Similar Product Records

This script demonstrates:
1. Initializing Pinecone client and index
2. Upserting sample product vectors
3. Performing similarity search queries
4. Retrieving top 3 most similar products

"""

import os
import time
from pinecone import Pinecone, ServerlessSpec
from openai import AzureOpenAI
import logging

# Import configuration
try:
    from config import *
except ImportError:
    print("Error: config.py not found. Please copy config_template.py to config.py and fill in your API keys.")
    exit(1)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('assignment_10_logs.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class ProductSimilarityEngine:
    """Main class for handling product similarity operations using Pinecone"""
    
    def __init__(self):
        """Initialize the ProductSimilarityEngine with required clients"""
        self.setup_environment()
        self.setup_clients()
        self.index_name = "product-similarity-index"
        
    def setup_environment(self):
        """Set up environment variables for API keys"""
        # Load configuration from config.py
        os.environ["AZURE_OPENAI_ENDPOINT"] = AZURE_OPENAI_ENDPOINT
        os.environ["AZURE_OPENAI_API_KEY"] = AZURE_OPENAI_API_KEY
        os.environ["AZURE_DEPLOYMENT_NAME"] = AZURE_DEPLOYMENT_NAME
        os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
        
        logger.info("Configuration loaded from config.py")
        
    def setup_clients(self):
        """Initialize Azure OpenAI and Pinecone clients"""
        try:
            # Initialize Azure OpenAI client
            self.openai_client = AzureOpenAI(
                api_version="2024-07-01-preview",
                azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
                api_key=os.getenv("AZURE_OPENAI_API_KEY"),
            )
            logger.info("Azure OpenAI client initialized successfully")
            
            # Initialize Pinecone client
            self.pinecone_client = Pinecone(
                api_key=os.getenv("PINECONE_API_KEY")
            )
            logger.info("Pinecone client initialized successfully")
            
        except Exception as e:
            logger.error(f"Error initializing clients: {e}")
            raise
            
    def create_index(self):
        """Create Pinecone index if it doesn't exist"""
        try:
            # Check if index already exists
            existing_indexes = [index["name"] for index in self.pinecone_client.list_indexes()]
            
            if self.index_name not in existing_indexes:
                logger.info(f"Creating new index: {self.index_name}")
                
                self.pinecone_client.create_index(
                    name=self.index_name,
                    dimension=1536,  # text-embedding-3-small output size
                    spec=ServerlessSpec(cloud=PINECONE_CLOUD, region=PINECONE_REGION),
                )
                
                # Wait for index to be ready
                logger.info("Waiting for index to be ready...")
                time.sleep(10)
                logger.info(f"Index {self.index_name} created successfully")
            else:
                logger.info(f"Index {self.index_name} already exists")
                
            # Connect to the index
            self.index = self.pinecone_client.Index(self.index_name)
            logger.info(f"Connected to index: {self.index_name}")
            
        except Exception as e:
            logger.error(f"Error creating/connecting to index: {e}")
            raise
            
    def get_embedding(self, text):
        """Generate embedding for given text using Azure OpenAI"""
        try:
            response = self.openai_client.embeddings.create(
                input=text,
                model=os.getenv("AZURE_DEPLOYMENT_NAME")
            )
            return response.data[0].embedding
        except Exception as e:
            logger.error(f"Error generating embedding for text '{text}': {e}")
            raise
            
    def upsert_products(self):
        """Upsert sample product vectors into the index"""
        try:
            # Sample product dataset as specified in the assignment
            products = [
                {"id": "prod1", "title": "Red T-Shirt", "description": "Comfortable cotton t-shirt in bright red"},
                {"id": "prod2", "title": "Blue Jeans", "description": "Stylish denim jeans with relaxed fit"},
                {"id": "prod3", "title": "Black Leather Jacket", "description": "Genuine leather jacket with classic style"},
                {"id": "prod4", "title": "White Sneakers", "description": "Comfortable sneakers perfect for daily wear"},
                {"id": "prod5", "title": "Green Hoodie", "description": "Warm hoodie made of organic cotton"},
            ]
            
            logger.info("Generating embeddings for products...")
            vectors = []
            
            for product in products:
                # Use title and description for richer embeddings
                text_for_embedding = f"{product['title']} {product['description']}"
                embedding = self.get_embedding(text_for_embedding)
                vectors.append((product["id"], embedding))
                logger.info(f"Generated embedding for {product['title']}")
                
            # Upsert vectors to the index
            logger.info("Upserting vectors to Pinecone index...")
            self.index.upsert(vectors=vectors)
            logger.info(f"Successfully upserted {len(vectors)} product vectors")
            
            return products
            
        except Exception as e:
            logger.error(f"Error upserting products: {e}")
            raise
            
    def search_similar_products(self, query, top_k=3):
        """Search for top k most similar products"""
        try:
            logger.info(f"Searching for products similar to: '{query}'")
            
            # Generate embedding for the query
            query_embedding = self.get_embedding(query)
            logger.info("Query embedding generated successfully")
            
            # Query the index
            results = self.index.query(
                vector=query_embedding,
                top_k=top_k,
                include_metadata=False
            )
            
            logger.info(f"Query completed. Found {len(results.matches)} matches")
            return results
            
        except Exception as e:
            logger.error(f"Error searching similar products: {e}")
            raise
            
    def display_results(self, query, results, products):
        """Display search results in a formatted way"""
        print(f"\n{'='*60}")
        print(f"TOP 3 SIMILAR PRODUCTS FOR QUERY: '{query}'")
        print(f"{'='*60}")
        
        if not results.matches:
            print("No similar products found.")
            return
            
        for i, match in enumerate(results.matches, 1):
            product_id = match.id
            score = match.score
            
            # Find product details
            product = next((p for p in products if p["id"] == product_id), None)
            
            if product:
                print(f"\n{i}. {product['title']}")
                print(f"   Description: {product['description']}")
                print(f"   Similarity Score: {score:.4f}")
                print(f"   Product ID: {product_id}")
            else:
                print(f"\n{i}. Product ID: {product_id} (Similarity Score: {score:.4f})")
                
        print(f"\n{'='*60}")
        
    def run_demo(self):
        """Run the complete demonstration"""
        try:
            logger.info("Starting Assignment 10 Demo...")
            
            # Step 1: Create/connect to index
            self.create_index()
            
            # Step 2: Upsert sample products
            products = self.upsert_products()
            
            # Step 3: Define sample queries (auto input as required)
            sample_queries = [
                "clothing item for summer",
                "comfortable daily wear",
                "stylish formal outfit",
                "warm winter clothing",
                "casual weekend wear"
            ]
            
            # Step 4: Perform similarity searches for each query
            for query in sample_queries:
                logger.info(f"\nProcessing query: {query}")
                
                # Search for similar products
                results = self.search_similar_products(query, top_k=3)
                
                # Display results
                self.display_results(query, results, products)
                
                # Add delay between queries for better readability
                time.sleep(2)
                
            logger.info("Demo completed successfully!")
            
        except Exception as e:
            logger.error(f"Error running demo: {e}")
            raise
            
    def cleanup(self):
        """Clean up resources"""
        try:
            if hasattr(self, 'index'):
                logger.info("Closing Pinecone index connection...")
                # Note: Pinecone client doesn't require explicit cleanup
                
            logger.info("Cleanup completed")
            
        except Exception as e:
            logger.error(f"Error during cleanup: {e}")

def main():
    """Main function to run the assignment"""
    engine = None
    try:
        # Initialize the engine
        engine = ProductSimilarityEngine()
        
        # Run the demo
        engine.run_demo()
        
    except Exception as e:
        logger.error(f"Assignment failed: {e}")
        print(f"\nError: {e}")
        print("\nNote: Make sure to set up your API keys in the setup_environment method")
        print("or set them as environment variables before running the script.")
        
    finally:
        # Cleanup
        if engine:
            engine.cleanup()

if __name__ == "__main__":
    main()
