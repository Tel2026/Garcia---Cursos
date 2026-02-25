import streamlit as st
import pandas as pd

# ==============================
# CONFIGURACIÓN GENERAL
# ==============================
st.set_page_config(
    page_title="Acceso Fotocheck",
    layout="centered"
)

SHEET_ID = "1OOHc3TDqbJOEq9at_AAH8LCbnXIBZcQW"
SHEET_NAME = "Hoja1"

# ==============================
# CARGA DE BASE DE DATOS
# ==============================
SHEET_URL = (
    f"https://docs.google.com/spreadsheets/d/{SHEET_ID}"
    f"/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}"
)

@st.cache_data
def cargar_bd():
    return pd.read_csv(SHEET_URL)

df = cargar_bd()

# ==============================
# INTERFAZ
# ==============================
st.title("🔐 Acceso a Evidencias")

st.write("Ingrese su **fotocheck** para acceder a sus evidencias")

fotocheck = st.text_input(
    "Fotocheck",
    placeholder="Ej: 1353612"
)

if fotocheck:
    fotocheck = fotocheck.strip()

    resultado = df[df["Fotocheck"].astype(str) == fotocheck]

    if resultado.empty:
        st.error("❌ Fotocheck no encontrado en la base de datos")
    else:
        nombre = resultado.iloc[0]["Nombre y Apellidos"]

        st.success(f"👤 Bienvenido {nombre}")

        # 🔎 BÚSQUEDA GLOBAL EN DRIVE (PÚBLICA)
        link_drive = f"https://drive.google.com/drive/search?q={fotocheck}"

        st.link_button(
            "📂 Buscar carpeta de evidencias",
            link_drive
        )

        st.info(
            "🔍 Se abrirá Google Drive filtrado por su fotocheck.\n\n"
            "Seleccione la carpeta correspondiente."
        )
