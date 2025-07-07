import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set the API key for Google Generative AI
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError("GEMINI_API_KEY environment variable is not set.")

# Configure Gemini
genai.configure(api_key=API_KEY)

# Initialize the model (assuming "gemma-3-27b-it" is available via Gemini API)
model = genai.GenerativeModel("gemma-3-27b-it")  # or "gemini-1.5-flash"

def generate_response(prompt: str) -> str:
    """
    Generate a response from the Gemini model based on the provided prompt.
    
    Args:
        prompt (str): The input prompt for the model.
        
    Returns:
        str: The generated response from the model.
    """
    response = model.generate_content(prompt)
    return response.text



