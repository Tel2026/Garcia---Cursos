import streamlit as st
import pandas as pd

st.set_page_config(page_title="Acceso Fotocheck")

SHEET_ID = "1OOHc3TDqbJOEq9at_AAH8LCbnXIBZcQW"
SHEET_NAME = "Hoja1"
LINK_CARPETA = "https://drive.google.com/drive/folders/1a_bkWkTuBXki2h764PloetZ8SI_3aYB5"

url = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}"

@st.cache_data
def cargar_bd():
    return pd.read_csv(url)

df = cargar_bd()

st.title("🔐 Acceso")

fotocheck = st.text_input("Ingrese su Fotocheck")

if fotocheck:
    resultado = df[df["Fotocheck"].astype(str) == fotocheck]

    if not resultado.empty:
        nombre = resultado.iloc[0]["Nombre y Apellidos"]

        st.success(f"👤 Bienvenido {nombre}")
        st.link_button("📂 Abrir carpeta de evidencias", LINK_CARPETA)

    else:
        st.error("❌ Fotocheck no válido")
