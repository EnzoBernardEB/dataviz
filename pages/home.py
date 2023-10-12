import streamlit as st
import matplotlib.pyplot as plt
import plotly.graph_objects as go
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
<<<<<<< HEAD

=======
st.title("Analyse des données Airbnb de New York pour 2019")
>>>>>>> b088e9a204b2f7864ae3fbe0ea6dd46283fc49ae
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











# TEST
def create_gauge_chart(value, title, color='green'):
    """Créer un graphique jauge avec Plotly."""
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=value,
        title={'text': title, 'font': {'color': 'black'}},
        number={'font': {'color': color}},
        gauge={'axis': {'range': [None, 100]}, 'bar': {'color': color}}
    ))
    return fig

# Simuler un KPI - Taux d'occupation moyen (en pourcentage)
occupancy_rate = 72.5
fig = create_gauge_chart(occupancy_rate, "Taux d'occupation (%)", color='green')

st.plotly_chart(fig)
# TEST




fig, ax = plt.subplots(figsize=(8, 4))
colors = ['#0173B2', '#DE8F05', '#029E73', '#D55E00', '#CC78BC']
sorted_neighbourhoods = df.groupby('neighbourhood_group')['neighbourhood'].nunique().sort_values()

sorted_neighbourhoods.plot(kind='barh', ax=ax, color=colors)

for index, value in enumerate(sorted_neighbourhoods):
    ax.text(value, index, ' ' + str(value), va='center', color='black', fontweight='bold')

ax.set_title("Nombre de quartiers par groupe")
ax.set_xlabel("Nombre de quartiers")
ax.set_ylabel("Groupe de quartiers")

st.pyplot(fig)
