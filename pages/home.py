import streamlit as st
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
from database.data_loader import df


# Affichage du titre
st.markdown("""
<style>
    .reportview-container .main .block-container {
        max-width: 100%;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>Statistiques Airbnb concernant la ville de New York pour l’année 2019</h1>", unsafe_allow_html=True)
# Affichage du titre

# Métriques
col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
logement_reserves = (df['availability_365'] <= 15).sum()
# Calcul de la somme totale
total_depensee = (df['price'] * (365 - df['availability_365'])).sum()
# Formatage du résultat
formatted_total = "{:,.0f}$".format(total_depensee).replace(',', ' ')  # Utilisez un espace au lieu d'une virgule pour la séparation


with col1:
    st.metric(label="Nombre total de logements", value=len(df))
with col2:
    st.metric(label="Logement réservés l'année complète", value=logement_reserves)
with col3:
    st.metric(label="Nombre d'hôtes distincts", value=df['host_id'].nunique())
with col4:
    st.metric(label="Somme totale dépensée", value=formatted_total)


# Graphique
# Affichage du titre
st.markdown("""
<style>
    .reportview-container .main .block-container {
        max-width: 100%;
    }
    .header-margin {
        margin-top: 5rem;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h2 class='header-margin' style='text-align: center;'>Type de logements par arrondissement</h2>", unsafe_allow_html=True)
# Affichage du titre

# Group by 'neighbourhood_group', 'neighbourhood', and 'room_type' 
# Calculate the average price and count the number of occurrences for each group
grouped = df.groupby(['neighbourhood_group', 'neighbourhood', 'room_type']).agg(avg_price=('price', 'mean'), count=('room_type', 'size')).reset_index()

fig = px.treemap(grouped, 
                path=['neighbourhood_group', 'neighbourhood', 'room_type'], 
                values='count',
                hover_data=['avg_price'])

# Customizing hover template
fig.update_traces(hovertemplate='<b>%{label}</b><br>Count: %{value}<br>Avg Price: %{customdata[0]:.1f}$')

st.plotly_chart(fig, use_container_width=True)




