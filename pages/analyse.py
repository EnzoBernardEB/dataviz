import streamlit as st
from streamlit_folium import folium_static
import folium
from folium.plugins import MarkerCluster
import pandas as pd

from database.data_loader import df

# Importation des données
data = df
data['occupation_time'] = 365 - data['availability_365']

# Création d'une carte centrée sur New York
m = folium.Map(location=[40.7128, -74.0060], zoom_start=11)

# Ajout d'un regroupement de marqueurs à la carte
marker_cluster = MarkerCluster().add_to(m)

# Boucle sur les données pour ajouter chaque logement à la carte
for idx, row in data.iterrows():
    # Choix de la couleur en fonction du temps d'occupation
    if row['occupation_time'] < 120:
        color = 'green'
    elif row['occupation_time'] < 240:
        color = 'orange'
    else:
        color = 'red'
    # Ajout du marqueur à la carte
    folium.CircleMarker(
        location=(row['latitude'], row['longitude']),
        radius=5,
        color=color,
        fill=True,
        fill_color=color,
    ).add_to(marker_cluster)

# Affichage de la carte dans Streamlit
st.title("Trafic par quartier")
folium_static(m)

# Ajout de la légende dans la sidebar
legend = '''
    <style>
    .legend {
        border:2px solid black;
        padding:10px;
        background-color:white;
        border-radius:5px;
    }
    .legend-label {
        display:block;
        margin-bottom:5px;
    }
    </style>
    <div class="legend">
        <div class="legend-label" style="color:green;">&#9679; Occupation < 120 jours</div>
        <div class="legend-label" style="color:orange;">&#9679; Occupation entre 120 et 240 jours</div>
        <div class="legend-label" style="color:red;">&#9679; Occupation > 240 jours</div>
    </div>
'''
st.sidebar.markdown(legend, unsafe_allow_html=True)
