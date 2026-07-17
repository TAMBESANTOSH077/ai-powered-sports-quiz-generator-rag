import json
import os
import chromadb
from chromadb.utils import embedding_functions

from src.config import CHROMA_DB_PATH, COLLECTION_NAME


embedding_function = embedding_functions.DefaultEmbeddingFunction()


def get_client():
    """Create or connect to ChromaDB."""
    return chromadb.PersistentClient(path=CHROMA_DB_PATH)


def get_collection():
    """Create collection if it doesn't exist."""
    client = get_client()

    return client.get_or_create_collection(
        name=COLLECTION_NAME,
        embedding_function=embedding_function
    )


def load_data(json_path="data/sports_facts.json"):
    """Load sports facts from JSON."""

    if not os.path.exists(json_path):
        raise FileNotFoundError(f"{json_path} not found.")

    with open(json_path, "r", encoding="utf-8") as file:
        return json.load(file)


def initialize_database():
    """
    Populate database only once.
    """

    collection = get_collection()

    if collection.count() > 0:
        print("✅ ChromaDB already initialized.")
        return

    facts = load_data()

    documents = []
    metadatas = []
    ids = []

    for index, item in enumerate(facts):
        documents.append(item["fact"])
        metadatas.append(
            {
                "sport": item["sport"]
            }
        )
        ids.append(f"fact_{index}")

    collection.add(
        documents=documents,
        metadatas=metadatas,
        ids=ids
    )

    print(f"✅ Added {len(documents)} sports facts.")


def search_historical_facts(sport, query, n_results=3):
    """
    Retrieve relevant historical facts.
    """

    collection = get_collection()

    results = collection.query(
        query_texts=[query],
        n_results=n_results,
        where={"sport": sport}
    )

    if results["documents"]:
        return results["documents"][0]

    return []