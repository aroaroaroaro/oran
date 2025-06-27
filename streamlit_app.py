# streamlit_app.py (version mise à jour)

import streamlit as st
from simulation import avancer_d_une_semaine, get_articles
from state_template import creer_etat_initial
import pickle
import os

STATE_FILE = "state.pkl"

def charger_etat():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "rb") as f:
            return pickle.load(f)
    return creer_etat_initial()

def sauvegarder_etat(etat):
    with open(STATE_FILE, "wb") as f:
        pickle.dump(etat, f)

st.set_page_config(page_title="Simulation Oran", layout="wide")
st.title("🇴🇷 Simulation politique d'Oran")
st.write("👁️ Mode Observateur – Avance dans le temps et suis l'évolution du pays.")

etat = charger_etat()

if st.button("⏭️ Avancer d'une semaine"):
    etat = avancer_d_une_semaine(etat)
    sauvegarder_etat(etat)

col1, col2 = st.columns(2)

with col1:
    st.subheader("👤 Dirigeants")
    st.write(f"**Président de la République :** {etat['president_republique']}")
    st.write(f"**Premier Ministre :** {etat['premier_ministre']} ({etat['popularite_pm']}% de popularité)")
    st.write(f"**Président du Sénat :** {etat['president_senat']}")
    st.write(f"**Président de la Chambre :** {etat['president_chambre']}")
    st.write(f"**Gouverneur de la Banque :** {etat['gouverneur_banque']}")
    st.write(f"**Président Cour Suprême :** {etat['president_cour_supreme']}")
    st.write(f"**Popularité du gouvernement :** {etat['popularite_gouvernement']}%")

with col2:
    st.subheader("🏛️ Gouvernement")
    for min, nom in etat["gouvernement"].items():
        st.write(f"- **Ministre de {min}** : {nom}")

st.subheader("🏛️ Parlement")
col3, col4 = st.columns(2)

with col3:
    st.markdown("### Chambre des Représentants")
    for parti, nb in etat["chambre_representants"].items():
        st.write(f"- {parti} : {nb} sièges")

with col4:
    st.markdown("### Sénat")
    for parti, nb in etat["senat"].items():
        st.write(f"- {parti} : {nb} sièges")

st.subheader("📰 Actualités")
for article in get_articles(etat):
    st.markdown(f"- {article}")
