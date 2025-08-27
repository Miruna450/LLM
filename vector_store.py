from openai import OpenAI
import chromadb
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

chroma_client = chromadb.PersistentClient(path="./chroma_data")
collection = chroma_client.get_or_create_collection(name="book_summaries")

def search_books(query: str, top_k=3):
    embedding = client.embeddings.create(
        input=query,
        model="text-embedding-3-small"
    ).data[0].embedding

    results = collection.query(query_embeddings=[embedding], n_results=top_k)
    titles = [m["title"] for m in results["metadatas"][0]]
    return titles
