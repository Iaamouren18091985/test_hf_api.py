import requests

HF_TOKEN = "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"  # Pon aquí tu token real

headers = {
    "Authorization": f"Bearer {HF_TOKEN}"
}

payload = {
    "inputs": "Escribe un artículo corto sobre inteligencia artificial."
}

response = requests.post(
    "https://api-inference.huggingface.co/models/gpt2",
    headers=headers,
    json=payload
)

print("Status code:", response.status_code)
print("Respuesta JSON:", response.json())
