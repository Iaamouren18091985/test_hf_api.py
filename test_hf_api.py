import streamlit as st
import requests

# Leer token desde Streamlit Secrets
HF_TOKEN = st.secrets["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"]

st.set_page_config(page_title="Generador de Artículos SEO", page_icon="🧠")
st.title("🧠 Generador de Artículos con Hugging Face")

keyword = st.text_input("🔑 Palabra clave principal", placeholder="Ej: inteligencia artificial")
style = st.selectbox("✍️ Estilo del artículo", ["Informativo", "Persuasivo", "Tutorial"])
length = st.slider("📏 Longitud del artículo (palabras)", 100, 1000, 300)

if st.button("🚀 Generar artículo"):

    if not keyword.strip():
        st.error("Por favor, ingresa una palabra clave.")
    else:
        with st.spinner("Generando artículo..."):
            headers = {
                "Authorization": f"Bearer {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}"
            }

            prompt = (
                f"Eres un redactor SEO experto. Escribe un artículo de aproximadamente {length} palabras, "
                f"estilo {style}, usando la palabra clave principal: '{keyword}'. Usa subtítulos y lenguaje claro."
            )

            payload = {
                "inputs": prompt,
                "parameters": {
                    "max_new_tokens": length,
                    "do_sample": True,
                    "temperature": 0.7
                }
            }

            url = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta"

            response = requests.post(url, headers=headers, json=payload)

            if response.status_code == 200:
                result = response.json()
                # El resultado puede ser una lista con 'generated_text'
                if isinstance(result, list) and "generated_text" in result[0]:
                    st.subheader("📄 Artículo generado:")
                    st.write(result[0]["generated_text"])
                else:
                    st.error("El formato de respuesta no es el esperado.")
            elif response.status_code == 401:
                st.error("Error 401: Token inválido o sin permisos para llamar a la API.")
            else:
                st.error(f"Error {response.status_code}: No se pudo generar el artículo.")
