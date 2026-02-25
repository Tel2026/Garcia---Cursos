import streamlit as st
import pandas as pd

st.set_page_config(page_title="Acceso Fotocheck")

st.title("🔐 Acceso")

fotocheck = st.text_input("Ingrese su Fotocheck")

if fotocheck:
    st.info("Validando...")
