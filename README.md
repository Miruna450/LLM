# Smart Librarian – AI cu RAG + Tool Calling

Un chatbot AI conversational care recomanda carti pe baza intereselor utilizatorului, folosind OpenAI + RAG (ChromaDB) + tool pentru rezumat. Implementat ca aplicatie CLI.

---

## Functionalitati

- Cautare semantica in baza de date de carti (ChromaDB + embeddings OpenAI)
- Recomandare generata de GPT-3.5 pe baza celor mai relevante carti
- Tool `get_summary_by_title()` care returneaza un rezumat detaliat
- Optiune de citire cu voce (Text-to-Speech, TTS)
- Suport pentru carti in limba romana si engleza

---

## Structura fisierelor

```
ChatBot/
├── chatbot.py         # Chatbotul principal (CLI)
├── init_store.py      # Populeaza ChromaDB cu embedding-uri
├── tools.py           # Rezumate + tool de extragere
├── vector_store.py    # Modul de cautare semantica
├── chroma_data/       # Folderul creat de ChromaDB (vector store local)
└── .venv/             # Mediu virtual (exclus din git)
```

---

## Cum rulezi aplicatia

1. **Cloneaza proiectul** si creeaza mediu virtual (daca nu exista deja):

```bash
python -m venv .venv
source .venv/Scripts/activate   # Windows
```

2. **Instaleaza dependintele**:

```bash
pip install -r requirements.txt
```

3. **Populeaza vector store-ul cu carti**:

```bash
python init_store.py
```

4. **Lanseaza chatbot-ul**:

```bash
python chatbot.py
```

---

## 💡 Exemple de intrebari pentru testare

- `Vreau o carte despre magie`
- `Ce imi recomanzi daca imi plac povestile fantastice?`
- `Ce carte are teme despre libertate si control politic?`
- `Imi doresc o carte despre satul romanesc`

---

## Despre vector store

Proiectul foloseste **ChromaDB** ca vector store local, care permite cautare semantica dupa embeddings. Nu s-a folosit `openai.vector_store` sau alte servicii cloud interzise.

---

## Observatii

- Pentru ca sistemul sa functioneze corect, intrebarile si rezumatele trebuie sa fie in aceeasi limba (preferabil romana).
- Recomandarea GPT se bazeaza pe cele mai apropiate 3 carti, selectate semantic.

---

## Final

Proiectul este 100% functional si pregatit pentru livrare sau extindere (ex: Streamlit, Speech-to-Text, filtrare etc).