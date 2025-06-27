# streamlit_app.py

import streamlit as st
from simulation import avancer_d_une_semaine, get_articles
import pickle
import os

STATE_FILE = "state.pkl"

def charger_etat():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "rb") as f:
            return pickle.load(f)
    return {}

def sauvegarder_etat(etat):
    with open(STATE_FILE, "wb") as f:
        pickle.dump(etat, f)

st.title("Simulation politique d'Oran")
st.write("👁️ Mode Observateur – Appuie sur le bouton pour avancer d'une semaine et découvrir les actualités.")

etat = charger_etat()

if st.button("⏭️ Avancer d'une semaine"):
    etat = avancer_d_une_semaine(etat)
    sauvegarder_etat(etat)

articles = get_articles(etat)
for article in articles:
    st.markdown(f"- {article}")
