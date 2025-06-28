from dotenv import load_dotenv
import os

load_dotenv()  # Load from .env

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
TOMTOM_API_KEY = os.getenv("TOMTOM_API_KEY")
OPENWEATHERMAP_API_KEY = os.getenv("OPENWEATHERMAP_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Optional check
if not all([TAVILY_API_KEY, TOMTOM_API_KEY, OPENWEATHERMAP_API_KEY, GROQ_API_KEY]):
   raise ValueError("One or more API keys are missing in .env")
