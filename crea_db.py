import os
import sqlite3

# Trova la cartella corrente in modo sicuro
cartella_corrente = os.path.dirname(os.path.abspath(__file__))
percorso_db = os.path.join(cartella_corrente, "chatbot.db")

# Connessione al database
connessione = sqlite3.connect(percorso_db)
cursore = connessione.cursor()

# Elimina la tabella precedente per ricrearla pulita con la nuova struttura
cursore.execute("DROP TABLE IF EXISTS faq")

# Crea la tabella faq
cursore.execute("""
CREATE TABLE faq (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parola_chiave TEXT NOT NULL,
    risposta TEXT NOT NULL
)
""")

# Lista delle 12 domande/risposte intelligenti con parole chiave multiple
dati_faq = [
    (
        "ciao",
        "Ciao, ChatGPT, come va?",
    ),
    (
        "nome",
        "Mi chiamo ChatGPT e sono il tuo assistente virtuale intelligente.",
    ),
    (
        "orari",
        (
            "Siamo aperti dal lunedì al sabato, dalle 09:00 alle 20:00 orario"
            " continuato."
        ),
    ),
    (
        "indirizzo",
        (
            "La nostra sede principale si trova in Via Roma 15, a due passi dal"
            " centro."
        ),
    ),
    (
        "prenotazion",
        (
            "Puoi prenotare direttamente qui in chat indicando data, orario e"
            " il servizio desiderato!"
        ),
    ),
    (
        "prezz",
        (
            "I nostri prezzi variano in base al servizio scelto. Vuoi"
            " ricevere il listino dettagliato?"
        ),
    ),
    (
        "servizi",
        (
            "Offriamo consulenza dedicata, assistenza rapida e servizi su"
            " misura per le PMI."
        ),
    ),
    (
        "contatt",
        (
            "Puoi chiamarci al numero 0123-456789 o scriverci via email a"
            " info@chatbotpmi.it."
        ),
    ),
    (
        "pagament",
        (
            "Accettiamo tutti i principali circuiti di carte di credito,"
            " bancomat, contanti e bonifico."
        ),
    ),
    (
        "parcheggi",
        (
            "Sì, c'è un comodo parcheggio riservato ai clienti proprio di"
            " fronte all'ingresso."
        ),
    ),
    (
        "offert",
        (
            "Al momento abbiamo promozioni attive per i nuovi clienti. Chiedi"
            " i dettagli in base al servizio!"
        ),
    ),
    (
        "grazie",
        "Di nulla! È un piacere aiutarti. Hai bisogno di altro?",
    ),
]

# Inserimento dei dati nel database
cursore.executemany(
    "INSERT INTO faq (parola_chiave, risposta) VALUES (?, ?)", dati_faq
)

# Salva le modifiche e chiudi
connessione.commit()
connessione.close()

print(
    "Database 'chatbot.db' creato e popolato con successo con le 12 risposte!"
)