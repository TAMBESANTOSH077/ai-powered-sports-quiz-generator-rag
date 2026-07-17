import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Gemini API Key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError(
        "❌ GEMINI_API_KEY not found. Please add it to your .env file."
    )

# ChromaDB Configuration
CHROMA_DB_PATH = "./chroma_db"
COLLECTION_NAME = "sports_history"

# Available Sports
SPORTS = [
    "Cricket",
    "Football",
    "Badminton",
    "Tennis",
    "Basketball",
    "Hockey"
]

# Difficulty Levels
DIFFICULTY = [
    "Easy",
    "Medium",
    "Hard"
]