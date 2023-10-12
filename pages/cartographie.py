import streamlit as st
import folium
from database.data_loader import df
from streamlit_folium import folium_static
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

# Titre de la page
st.title("Carte des logements Airbnb à New York par tranche de prix")

# Description
st.write(
    "Cette carte affiche les logements Airbnb à New York en fonction de leur tranche de prix. Vous pouvez sélectionner un quartier dans la barre latérale pour afficher les logements de cette zone."
)

def display_map(neighbourhood_group=None):
    # Création d'une carte centrée sur New York
    m = folium.Map(location=[40.730610, -73.935242], zoom_start=10)

    # Filtrage des données par quartier si un quartier est sélectionné
    if neighbourhood_group:
        filtered_df = df[df['neighbourhood_group'] == neighbourhood_group]
    else:
        filtered_df = df

    # Définition des tranches de prix
    price_bins = [0, 500, 1000, 1500, 2500, 5000, 7500, 10000, np.inf]

    # Création d'une palette de couleurs évoluant du vert (bas prix) au rouge (prix élevés)
    colormap = plt.get_cmap('YlOrRd')

    # Légende des prix et leurs couleurs correspondantes
    price_legend = []

    # Ajout de chaque logement à la carte avec la couleur correspondant à sa tranche de prix
    for i in range(len(price_bins) - 1):
        min_price, max_price = price_bins[i], price_bins[i + 1]
        color = colormap(i / (len(price_bins) - 2))  # Échelle de couleurs de 0 à 1

        # Filtrage des logements dans la tranche de prix actuelle
        filtered_price_df = filtered_df[(filtered_df['price'] >= min_price) & (filtered_df['price'] < max_price)]

        # Ajout des logements sur la carte avec la couleur correspondante
        for _, row in filtered_price_df.iterrows():
            folium.CircleMarker(
                location=(row['latitude'], row['longitude']),
                radius=3,
                color=mpl.colors.to_hex(color),
                fill=True,
                fill_color=mpl.colors.to_hex(color),
                fill_opacity=0.6
            ).add_to(m)

        # Ajout de la tranche de prix à la légende
        price_legend.append((min_price, max_price, color))

    # Affichage de la carte dans Streamlit
    folium_static(m)

    # Affichage de la légende dans la barre latérale
    st.sidebar.title("Légende des prix")
    for min_price, max_price, color in price_legend:
        st.sidebar.markdown(
            f"Prix entre ${min_price} et ${max_price}: <div style='background-color: {mpl.colors.to_hex(color)}; display: inline-block; width: 15px; height: 15px;'></div>",
            unsafe_allow_html=True)

# Widget de sélection du quartier
selected_neighbourhood_group = st.sidebar.selectbox("Sélectionnez un quartier", df['neighbourhood_group'].unique())

# Affichage de la carte avec le quartier sélectionné
display_map(selected_neighbourhood_group)
