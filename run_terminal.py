# run_terminal.py

from simulation import avancer_d_une_semaine, get_articles
import pickle
import os
import time

STATE_FILE = "state.pkl"

def charger_etat():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "rb") as f:
            return pickle.load(f)
    return {}

def sauvegarder_etat(etat):
    with open(STATE_FILE, "wb") as f:
        pickle.dump(etat, f)

def main():
    etat = charger_etat()
    print("=== Simulation politique d'Oran – Mode Terminal ===")
    while True:
        input("\n⏭️ Appuie sur Entrée pour avancer d'une semaine...")
        etat = avancer_d_une_semaine(etat)
        sauvegarder_etat(etat)
        print(f"📅 Semaine {etat['semaine']} – {etat['date'].strftime('%d %B %Y')}")
        for article in get_articles(etat):
            print(f" - {article}")

if __name__ == "__main__":
    main()
