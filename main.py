import streamlit as st
from st_pages import Page, Section, add_page_title, show_pages
st.set_page_config(layout="wide")

show_pages(
        [
            Page("pages/home.py", "Accueil", "🏠"),
            Page("pages/analyse.py", "Analyse", "📈"),
            Page("pages/cartographie.py", "Prix par arrondissement", "🌍️"),
        ]
    )


