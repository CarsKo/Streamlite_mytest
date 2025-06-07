import streamlit as st
import json
import os

# Prüfe, ob die Datei existiert
json_path = 'ki_tools.json'
if not os.path.exists(json_path):
    st.error(f"Datei nicht gefunden: {json_path}")
    st.stop()

# Load the KI tools data from the JSON file
with open('ki_tools.json', 'r') as file:
    ki_tools = json.load(file)

# Get the selected category and information classification from the session state
selected_category = st.session_state.get('selected_category', None)
selected_classification = st.session_state.get('selected_classification', None)

# Filter the KI tools based on the selected criteria
filtered_tools = [
    tool for tool in ki_tools
    if (selected_category is None or tool['Kategorie'] == selected_category) and
       (selected_classification is None or tool['Informationsklassifizierung'] == selected_classification)
]

# Display the filtered list of KI tools
st.title('Liste der KI-Tools')
if filtered_tools:
    for tool in filtered_tools:
        st.subheader(tool['Name'])
        st.write(f"Kategorie: {tool['Kategorie']}")
        st.write(f"Informationsklassifizierung: {tool['Informationsklassifizierung']}")
        st.write(f"Beschreibung: {tool['Beschreibung']}")
else:
    st.write("Keine KI-Tools gefunden, die den ausgewählten Kriterien entsprechen.")