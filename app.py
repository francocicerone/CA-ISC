import streamlit as st
import pandas as pd

# Cargar estilos desde styles.css
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Título de la aplicación
st.title("📋 Formulario Personalizado con CSS")

# Campos del formulario
nombre = st.text_input("Nombre:")
correo = st.text_input("Correo Electrónico:")
respuesta = st.text_area("¿Qué opinas sobre nuestra plataforma?")

# Botón para enviar el formulario
if st.button("Enviar"):
    if nombre and correo and respuesta:
        # Guardar datos en un archivo CSV
        df = pd.DataFrame([[nombre, correo, respuesta]], columns=["Nombre", "Correo", "Respuesta"])
        df.to_csv("respuestas.csv", mode="a", index=False, header=not st.session_state.get("data_written", False))
        st.session_state["data_written"] = True
        st.success("✅ ¡Respuesta enviada con éxito!")
    else:
        st.error("⚠️ Todos los campos son obligatorios")

# Mostrar respuestas previas (opcional)
if st.checkbox("📊 Mostrar respuestas anteriores"):
    try:
        df = pd.read_csv("respuestas.csv")
        st.dataframe(df)
    except FileNotFoundError:
        st.warning("No hay respuestas registradas aún.")

