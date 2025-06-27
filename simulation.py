# simulation.py1

import random
import datetime

def avancer_d_une_semaine(etat):
    if "semaine" not in etat:
        etat["semaine"] = 1
        etat["date"] = datetime.date(2025, 1, 1)
        etat["articles"] = []
        etat["events"] = []

    etat["semaine"] += 1
    etat["date"] += datetime.timedelta(days=7)

    # Simuler quelques événements
    nouveaux_articles = generer_evenements_presse(etat)
    etat["articles"] = nouveaux_articles

    return etat

def get_articles(etat):
    return etat.get("articles", [])

def generer_evenements_presse(etat):
    date_str = etat["date"].strftime("%d %B %Y")
    base_events = [
        "Une proposition de loi sur la fiscalité est débattue à la chambre.",
        "Le Ministre de l'Énergie annonce un plan pour les énergies renouvelables.",
        "Une manifestation a eu lieu à South Union contre le coût de la vie.",
        "Un sénateur de Clyde Islands fait une déclaration controversée.",
        "La Cour suprême rend un verdict important sur les droits syndicaux.",
        "Le Premier ministre effectue une visite officielle à l’étranger.",
        "Un journal révèle un possible scandale impliquant un député influent.",
        "Des tensions émergent entre Three River et Clyde Islands."
    ]
    random.shuffle(base_events)
    return [f"🗞️ {event} ({date_str})" for event in base_events[:random.randint(2, 4)]]
