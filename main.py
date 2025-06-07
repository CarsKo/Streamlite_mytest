from flask import Flask, render_template, request
import streamlit as st
import json

# Importiere die Funktion oder den Code aus 1_KI_Tools_Liste.py
import pages.1_KI_Tools_Liste as 1_KI_Tools_Liste

def load_ki_tools():
    with open('src/data/ki_tools.json') as f:
        return json.load(f)

def main():
    st.title("KI Tools Anwendung")
    st.header("Wählen Sie Ihre Kriterien")

    category = st.selectbox("Kategorie", ["Chat", "Bildgenerierung", "Videogenerierung", "API", "Codegenerierung", "Literaturreferenz"])
    classification = st.selectbox("Informationsklassifizierung", ["öffentlich", "intern", "vertraulich"])

    if st.button("KI-Tools anzeigen"):
        st.session_state.category = category
        st.session_state.classification = classification
        st.session_state.show_tools_list = True

        # Prüfe die Auswahl und zeige die Liste an
        if category == "Chat" and classification == "öffentlich":
            1_KI_Tools_Liste.show_tools_list()  # Passe den Funktionsnamen ggf. an

if __name__ == "__main__":
    main()