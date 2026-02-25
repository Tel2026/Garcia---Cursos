import streamlit as st
import pandas as pd

st.set_page_config(page_title="Acceso Fotocheck", layout="centered")

SHEET_ID = "1OOHc3TDqbJOEq9at_AAH8LCbnXIBZcQW"
SHEET_NAME = "Hoja1"

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

fotocheck = st.text_input("Fotocheck", placeholder="Ej: 1353612")

if fotocheck:
    fotocheck = fotocheck.strip()
    resultado = df[df["Fotocheck"].astype(str) == fotocheck]

    if resultado.empty:
        st.error("❌ Fotocheck no encontrado")
    else:
        fila = resultado.iloc[0]

        zona = fila["Zona"]
        guardia = fila["Guardia"]

        st.success(f"👤 Bienvenido {fila['Nombre y Apellidos']}")
        st.write(f"📍 Zona: **{zona}**")
        st.write(f"🕒 Guardia: **{guardia}**")

        # 🔗 ABRIR CARPETA BASE (NO BÚSQUEDA)
        link_drive = f"https://drive.google.com/drive/folders/{CARPETA_RAIZ_ID}"

        st.link_button(
            "📂 Abrir carpeta de evidencias",
            link_drive
        )

        st.info(
            "➡️ Ingrese a su **Zona** y luego a su **Guardia** para ver sus evidencias."
        )
