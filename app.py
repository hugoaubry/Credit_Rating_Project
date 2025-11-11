import os
import streamlit as st

import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))  # ✅ ligne à ajouter

import streamlit as st
from credit_core import creer_zip_etats_financiers

from credit_core import creer_zip_etats_financiers

st.set_page_config(page_title="Données financières", page_icon="📊", layout="centered")
st.title("📊 Récupération des données financières")

nom_entreprise = st.text_input(
    "Entrer le ticker de l'entreprise (ex : AAPL, MSFT, 005930.KS)").upper().strip()
forcer_telechargement = st.checkbox(
    "Forcer le re-téléchargement si les fichiers existent déjà", value=False)

if st.button("Télécharger les données (format ZIP, à décompresser)"):
    if not nom_entreprise:
        st.warning("Merci d’indiquer un ticker.")
    else:
        with st.spinner("Téléchargement en cours…"):
            chemin_zip = creer_zip_etats_financiers(nom_entreprise, forcer=forcer_telechargement)

        if not chemin_zip:
            st.error(f"Données indisponibles pour {nom_entreprise}.")
        else:
            st.success("Fichiers prêts.")
            with open(chemin_zip, "rb") as f:
                st.download_button(
                    label=f"Télécharger {os.path.basename(chemin_zip)}",
                    data=f,
                    file_name=os.path.basename(chemin_zip),
                    mime="application/zip",)
