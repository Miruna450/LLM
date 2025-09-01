
# Smart Librarian – AI cu RAG + Tool Calling

Un chatbot conversațional care recomanda carti pe baza unei intrebari tematice si ofera un rezumat detaliat al titlului ales.

---

## Functionalitate

1. Primeste o intrebare

2. Genereaza embedding pentru intrebare si cauta cele mai relevante 3 carti in `ChromaDB`.

3. Trimite catre GPT un prompt cu aceste 3 titluri si cere alegerea celui mai potrivit + explicatie.

4. Apeleaza un tool (`get_summary_by_title`) care returneaza rezumatul detaliat.

5. (Optional) Citeste recomandarea cu voce (TTS).

---

##  Structura proiectului

```
├── chatbot.py         # Interfata CLI principala
├── init_store.py      # Populeaza ChromaDB cu embedding-uri
├── vector_store.py    # Functia de cautare semantica
├── tools.py           # Dictionar + functie tool calling
├── config.py          # Incarcarea cheii OpenAI din .env
├── .gitignore
├── .env.example       # Model pentru configurare locala
├── README.md
```

---

##  Rularea proiectului


### 1. Creeaza si activeaza un mediu virtual

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/macOS:
source .venv/bin/activate
```

### 2. Instaleaza dependentele

```bash
pip install -r requirements.txt
```

---

### 3. Populeaza vector store-ul

```bash
python init_store.py
```

---

### 4. Ruleaza chatbot-ul

```bash
python chatbot.py
```

---

## Exemple de intrebari

- `Vreau o carte despre libertate si control social.`
- `Ce-mi recomanzi dacă iubesc povestile fantastice?`
- `O carte romaneasca despre maturizare?`

---

Proiectul nu foloseste vector store-ul OpenAI – toate embedding-urile sunt stocate si cautate local cu ChromaDB.


