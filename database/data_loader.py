# data_loader.py
import pandas as pd
import streamlit as st


@st.cache_resource
def load_data():
    data = pd.read_csv('database/AB_NYC_2019.csv', encoding='ISO-8859-1', delimiter=";")
    return data


df = load_data()
