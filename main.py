import streamlit as st
st.set_page_config(layout="wide")

from st_pages import Page, Section, add_page_title, show_pages
import pages

show_pages(
    [
        Page("pages/home.py", "Accueil", "🏠"),
        Page("pages/analyse.py", "Analyse", "📈"),
        Page("pages/cartographie.py", "Cartographie", "🌍️"),
    ]
)
