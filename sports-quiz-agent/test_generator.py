from src.database import initialize_database
from src.generator import generate_quiz

initialize_database()

quiz, context = generate_quiz(
    "Cricket",
    "Medium"
)

print(quiz)