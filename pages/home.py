import streamlit as st
import matplotlib.pyplot as plt
from database.data_loader import df

# Affichage du titre
st.title("Analyse des données Airbnb de New York pour 2019")

# Métriques
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric(label="Nombre total de logements", value=len(df))
with col2:
    st.metric(label="Nombre d'hôtes distincts", value=df['host_id'].nunique())
with col3:
    st.metric(label="Prix moyen ($)", value=int(df['price'].mean()))
with col4:
    st.metric(label="Nombre de quartiers", value=df['neighbourhood'].nunique())
with col5:
    st.metric(label="Nombre de groupes de quartiers", value=df['neighbourhood_group'].nunique())

# Graphique
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
