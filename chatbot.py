from openai import OpenAI
from vector_store import search_books
from tools import get_summary_by_title
from config import OPENAI_API_KEY
import pyttsx3

client = OpenAI(api_key=OPENAI_API_KEY)

def read_out_loud(text: str):
    engine = pyttsx3.init()
    engine.setProperty("rate", 160)
    engine.say(text)
    engine.runAndWait()

def ask_chatgpt(user_question: str, candidate_titles: list[str]) -> str:
    summaries = [f"{title}: {get_summary_by_title(title)}" for title in candidate_titles]
    prompt = (
        f"The user asked for a book recommendation based on the topic:\n"
        f"\"{user_question}\"\n\n"
        f"Here are 3 book summaries:\n\n" +
        "\n\n".join(summaries) +
        "\n\nWhich of these books best fits the requested topic? "
        "Select only one book and explain your choice. Do not invent details."
    )

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

def extract_title_from_response(response: str, candidate_titles: list[str]) -> str:
    for title in candidate_titles:
        if title.lower() in response.lower():
            return title
    return candidate_titles[0]  # fallback

# 🎯 Logica principală
def main():
    print(" Smart Librarian CLI\nScrie o intrebare (ex: Vreau o carte despre magie):")
    question = input(" Tu: ")

    titles = search_books(question, top_k=3)
    if not titles:
        print("Bot: Nu am gasit nicio potrivire.")
        return

    print("\n🔍 Titluri analizate:")
    for i, t in enumerate(titles, 1):
        print(f"{i}. {t}")

    gpt_response = ask_chatgpt(question, titles)
    selected_title = extract_title_from_response(gpt_response, titles)
    full_summary = get_summary_by_title(selected_title)

    print(f"\n Recomandare: {selected_title}")
    print(f"\n {gpt_response}")
    print(f"\n Rezumat complet:\n{full_summary}")

    # 🔊 TTS – opțional
    tts_choice = input("\n Vrei sa-ti citesc cu voce recomandarea si rezumatul? (da/nu): ").strip().lower()
    if tts_choice in ["da", "d", "yes", "y"]:
        read_out_loud(f"Recomandarea mea este: {selected_title}. {gpt_response}. Rezumat: {full_summary}")

if __name__ == "__main__":
    main()
