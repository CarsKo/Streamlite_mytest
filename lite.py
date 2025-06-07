import streamlit as st
import json
import os

# st.write("Aktuelles Arbeitsverzeichnis:", os.getcwd())
# st.write("Datei existiert:", os.path.exists('ki_tools.json'))

# Lade die KI-Tools aus der JSON-Datei
with open('ki_tools.json', 'r') as file:
    ki_tools = json.load(file)

# Auswahllisten
category = st.selectbox(
    "Kategorie",
    ["Chat", "Bildgenerierung", "Videogenerierung", "API-Nutzung", "Codegenerierung", "Literaturrecherche"]
)
classification = st.selectbox(
    "Informationsklassifizierung",
    ["öffentlich", "intern", "vertraulich"]
)

# Filtere die Tools nach Auswahl
filtered_tools = [
    tool for tool in ki_tools
    if tool['category'] == category and tool['classification'] == classification
]

st.write("Gefilterte Tools:", filtered_tools)

# Zeige die gefilterte Liste an
st.title('Liste der KI-Tools')
if filtered_tools:
    for tool in filtered_tools:
        st.subheader(tool['name'])
        st.write(f"Kategorie: {tool['category']}")
        st.write(f"Informationsklassifizierung: {tool['classification']}")
        st.write(f"Beschreibung: {tool['description']}")
else:
    st.write("Keine KI-Tools gefunden, die den ausgewählten Kriterien entsprechen.")