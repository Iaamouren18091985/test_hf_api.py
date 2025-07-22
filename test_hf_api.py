import streamlit as st
import requests

# Tu token de Hugging Face — no lo compartas públicamente en producción
HF_TOKEN = "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"

st.set_page_config(page_title="Generador de Artículos SEO", page_icon="🧠")
st.title("🧠 Generador de Artículos con Hugging Face")

keyword = st.text_input("🔑 Palabra clave principal", placeholder="Ej: inteligencia artificial")
style = st.selectbox("✍️ Estilo del artículo", ["Informativo", "Persuasivo", "Tutorial"])
length = st.slider("📏 Longitud del artículo (palabras)", 100, 1000, 300)

if st.button("🚀 Generar artículo"):
    if not keyword.strip():
        st.error("Por favor ingresa una palabra clave.")
    else:
        with st.spinner("Generando artículo..."):
            headers = {
                "Authorization": f"Bearer {HF_TOKEN}"
            }

            prompt = (
                f"Eres un redactor SEO experto. Escribe un artículo de aproximadamente {length} palabras, estilo {style}, "
                f"usando la palabra clave principal: '{keyword}'. Usa subtítulos y lenguaje claro."
            )

            payload = {
                "inputs": prompt,
                "parameters": {
                    "max_new_tokens": length // 2  # Controla longitud, aunque no exacto
                }
            }

           import requests

HF_TOKEN = "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"

headers = {
    "Authorization": f"Bearer {HF_TOKEN}"
}

response = requests.get("https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta", headers=headers)

print(response.status_code)
print(response.json())

