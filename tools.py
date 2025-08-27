# tools.py
book_summaries_dict = {
    "The Hobbit": (
        "Bilbo Baggins, a peaceful hobbit, is swept into an adventure with dwarves to reclaim a treasure from the dragon Smaug. "
        "Along the journey, he discovers bravery and makes unexpected friendships. "
        "Themes: adventure, courage, and self-discovery."
    ),
    "1984": (
        "A dystopian story about a totalitarian society controlled by surveillance and propaganda. "
        "Winston Smith secretly rebels against the regime in search of truth and freedom. "
        "Themes include government control, censorship, and individuality."
    ),
    "To Kill a Mockingbird":(
        "A powerful story set in the racially segregated American South. "
        "Scout Finch witnesses her father defend a black man wrongly accused of a crime. "
        "Themes: justice, innocence, and moral growth."
    ),
    "The Great Gatsby":(
        "A tale of love, ambition, and the American Dream. "
        "Jay Gatsby tries to win back Daisy Buchanan, but is destroyed by illusions and the corrupt society around him. "
        "Themes: wealth, identity, and loss."
    ),
    "Harry Potter and the Philosopher's Stone": (
        "Harry discovers he's a wizard and attends Hogwarts. "
        "He makes friends, faces dangers, and uncovers the mystery of the Philosopher’s Stone. "
        "Themes: friendship, bravery, magic, wizardry, spells, fantasy, supernatural adventure."
    ),
    "Enigma Otiliei":(
      "Felix, un tânăr orfan, se mută în casa unchiului său din București și o cunoaște pe Otilia, o fată misterioasă. "
      "Relația lor este marcată de ambiguități și lupte pentru moștenire. "
      "Teme: iubire, familie, maturizare."
    ),
    "Baltagul":(
        "Vitoria Lipan pornește într-o călătorie prin munți pentru a-și găsi soțul dispărut. "
        "Inteligența și intuiția ei o conduc spre adevăr. "
        "Teme: credință, destin, justiție."
    ),
    "Amintiri din copilărie":(
        "Ion Creangă povestește cu umor și nostalgie întâmplări din copilăria sa în satul Humulești. "
        "O frescă vie a lumii rurale românești. "
        "Teme: copilărie, familie, tradiție."
    ),
    "Moromeții":(
        "Ilie Moromete, un țăran filozof, încearcă să-și păstreze familia unită în fața schimbărilor sociale. "
        "Romanul surprinde viața satului românesc interbelic. "
        "Teme: familie, tradiție, schimbare."
    ),
    "Ion":(
        "Ion al Glanetașului dorește cu ardoare pământ și recunoaștere socială, sacrificând dragostea adevărată. "
        "Un roman despre obsesie și lupta pentru statut. "
        "Teme: iubire, posesie, destin."
    )
}

def get_summary_by_title(title: str) -> str:
    return book_summaries_dict.get(title, "Nu am gasit rezumatul complet pentru aceasta carte.")
