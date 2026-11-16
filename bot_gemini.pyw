import os
import sqlite3
import tkinter as tk

# Trova la cartella esatta in cui si trova questo file
cartella_corrente = os.path.dirname(os.path.abspath(__file__))
percorso_db = os.path.join(cartella_corrente, "chatbot.db")


# 1. FUNZIONI (Logica del Chatbot con ricerca elastica)
def cerca_risposta_db(testo_utente):
    # Connessione al database tramite il percorso sicuro
    connessione = sqlite3.connect(percorso_db)
    cursore = connessione.cursor()

    # Ricerca elastica: controlla se la parola chiave è contenuta nella frase dell'utente
    query = (
        "SELECT risposta FROM faq WHERE ? LIKE '%' || parola_chiave || '%'"
    )
    cursore.execute(query, (testo_utente,))
    risultato = cursore.fetchone()

    connessione.close()

    if risultato:
        return risultato[0]
    else:
        return (
            "Non ho capito bene la domanda. Prova a chiedermi gli orari,"
            " l'indirizzo, il nome o i servizi!"
        )


def rispondi():
    testo_utente = entrata_testo.get().lower().strip()
    if testo_utente:
        risposta = cerca_risposta_db(testo_utente)
        etichetta_risposta.config(text=risposta)


def reset():
    entrata_testo.delete(0, tk.END)
    etichetta_risposta.config(text="")


# 2. INTERFACCIA GRAFICA (Tkinter)
finestra = tk.Tk()
finestra.title("Chatbot Intelligente con SQLite")
finestra.geometry("450x320")

# Elementi della finestra
tk.Label(
    finestra, text="Scrivi un messaggio o una domanda:", font=("Arial", 10)
).pack(pady=5)
entrata_testo = tk.Entry(finestra, width=40)
entrata_testo.pack(pady=5)

tk.Button(finestra, text="Invia", command=rispondi, width=10).pack(pady=5)
tk.Button(finestra, text="Reset", command=reset, width=10).pack(pady=5)

etichetta_risposta = tk.Label(
    finestra, text="", font=("Arial", 10, "bold"), wraplength=400, fg="blue"
)
etichetta_risposta.pack(pady=10)

# Avvio dell'applicazione
finestra.mainloop()