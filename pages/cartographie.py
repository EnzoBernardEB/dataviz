import streamlit as st
import folium
from database.data_loader import df
from streamlit_folium import folium_static

def display_map():
    # Création d'une carte centrée sur New York
    m = folium.Map(location=[40.730610, -73.935242], zoom_start=10)

    # Définition d'une palette de couleurs pour les groupes de quartiers
    color_map = {
        'Manhattan': 'red',
        'Brooklyn': 'blue',
        'Queens': 'green',
        'Staten Island': 'purple',
        'Bronx': 'orange'
    }

    # Ajout de chaque logement à la carte
    for _, row in df.iterrows():
        folium.CircleMarker(
            location=(row['latitude'], row['longitude']),
            radius=3,
            color=color_map[row['neighbourhood_group']],
            fill=True,
            fill_color=color_map[row['neighbourhood_group']],
            fill_opacity=0.6
        ).add_to(m)

    # Affichage de la carte dans Streamlit
    folium_static(m)

    # Affichage de la légende dans la barre latérale
    st.sidebar.title("Légende")
    for neighbourhood_group, color in color_map.items():
        st.sidebar.markdown(f"<div style='background-color: {color}; display: inline-block; width: 15px; height: 15px;'></div> {neighbourhood_group}", unsafe_allow_html=True)

def display_cartography():
    display_map()

if __name__ == "__main__":
    display_cartography()
