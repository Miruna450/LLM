from openai import OpenAI
import chromadb
from config import OPENAI_API_KEY
from tools import book_summaries_dict

client = OpenAI(api_key=OPENAI_API_KEY)

chroma_client = chromadb.PersistentClient(path="./chroma_data")

chroma_client.delete_collection(name="book_summaries")
collection = chroma_client.get_or_create_collection(name="book_summaries")

for i, (title, summary) in enumerate(book_summaries_dict.items()):
    embedding = client.embeddings.create(
        input=summary,
        model="text-embedding-3-small"
    ).data[0].embedding

    collection.add(
        documents=[summary],
        ids=[str(i)],
        embeddings=[embedding],
        metadatas=[{"title": title}]
    )

print("ChromaDB populat cu embedding-urile din book_summaries_dict.")
