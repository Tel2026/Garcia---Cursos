import streamlit as st
import pandas as pd

# ==============================
# CONFIGURACIÓN
# ==============================
st.set_page_config(page_title="Acceso Fotocheck", layout="centered")

SHEET_ID = "1OOHc3TDqbJOEq9at_AAH8LCbnXIBZcQW"
SHEET_NAME = "Hoja1"

# Carpeta RAÍZ pública (la que contiene todas las carpetas de personas)
CARPETA_RAIZ_ID = "1a_bkWkTuBXki2h764PloetZ8SI_3aYB5"

# ==============================
# CARGA DE DATOS
# ==============================
url = (
    f"https://docs.google.com/spreadsheets/d/{SHEET_ID}"
    f"/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}"
)

@st.cache_data
def cargar_bd():
    return pd.read_csv(url)

df = cargar_bd()

# ==============================
# INTERFAZ
# ==============================
st.title("🔐 Acceso a Evidencias")

fotocheck = st.text_input("Ingrese su Fotocheck", placeholder="Ej: 1314870")

if fotocheck:
    resultado = df[df["Fotocheck"].astype(str) == fotocheck.strip()]

    if not resultado.empty:
        nombre = resultado.iloc[0]["Nombre y Apellidos"]

        st.success(f"👤 Bienvenido {nombre}")

        # Preparar búsqueda en Drive
        nombre_busqueda = nombre.replace(" ", "%20")

        link_drive = (
            "https://drive.google.com/drive/search?q="
            + nombre_busqueda
            + "%20in%3Aparents%20"
            + CARPETA_RAIZ_ID
        )

        st.link_button("📂 Abrir carpeta del trabajador", link_drive)

    else:
        st.error("❌ Fotocheck no válido")
