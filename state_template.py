# state_template.py

import datetime
import random

def creer_etat_initial():
    return {
        "semaine": 1,
        "date": datetime.date(2025, 1, 1),
        "articles": [],
        "popularite_gouvernement": 52.0,
        "popularite_pm": 55.0,
        "premier_ministre": "Elena Harrington",
        "president_republique": "Martin Caldewood",
        "president_senat": "Fiona Broadley",
        "president_chambre": "Graham Twiss",
        "gouverneur_banque": "John Feldwick",
        "president_cour_supreme": "Amira Solani",
        "gouvernement": {
            "Intérieur": "Karen McDowell",
            "Affaires Étrangères": "Marc Hollister",
            "Défense": "Richard Quince",
            "Justice": "Claire Bennett",
            "Finances": "Thomas Rhee",
            "Santé": "Leila Armitage",
            "Industrie": "Simon Drew",
            "Travail": "Darren Malik",
            "Transports": "Susan Bhatt",
            "Énergie": "Paul Okonkwo",
            "Éducation": "Sarah N’Guyen",
            "Logement": "Natalie Fischer",
            "Mer": "Frederik Larsson",
            "Agriculture": "Ingrid Boone",
            "Culture": "Oscar Brant",
            "Sciences": "Nina Patel",
            "Environnement": "Hugo Riis"
        },
        "chambre_representants": {
            "Progressistes": 312,
            "Réformistes": 198,
            "Union Régionale": 91,
            "National Démocrate": 57,
            "Verts": 43
        },
        "senat": {
            "Progressistes": 41,
            "Réformistes": 28,
            "Union Régionale": 17,
            "National Démocrate": 10,
            "Verts": 4
        }
    }
