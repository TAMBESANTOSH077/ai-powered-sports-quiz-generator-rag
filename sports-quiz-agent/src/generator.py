from google import genai

from src.config import GEMINI_API_KEY
from src.database import search_historical_facts
from src.search import get_live_news

client = genai.Client(api_key=GEMINI_API_KEY)


def generate_quiz(sport, difficulty):
    history = search_historical_facts(
        sport,
        f"{sport} history records championships rules",
        3
    )

    history_context = "\n".join(history)

    news_context = get_live_news(sport)

    prompt = f"""
You are an expert Sports Quiz Generator.

Use ONLY the information below.

Historical Facts:
{history_context}

Latest News:
{news_context}

Generate exactly 4 multiple-choice questions.

Sport: {sport}
Difficulty: {difficulty}

Format:

Question:
A)
B)
C)
D)

Correct Answer:

Explanation:
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    return response.text, history_context + "\n\n" + news_context