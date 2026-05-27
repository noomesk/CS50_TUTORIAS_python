#Tutioria 1: Cambiando modelo OPENAI por Ollama: 
import os
import requests
from dotenv import load_dotenv

load_dotenv()

prompt = input("Prompt: ")

# Usa una variable de entorno `OLLAMA_MODEL` para escoger el modelo
model = os.getenv("OLLAMA_MODEL", "qwen2.5-coder:1.5b")
print(f"Usando modelo: {model}")

try:
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": model, "prompt": prompt, "stream": False},
        timeout=60
    )
    result = response.json()
    if "response" in result:
        print(result["response"])
    else:
        print("Error:", result)
except requests.ConnectionError:
    print("ERROR: No se puede conectar a Ollama en localhost:11434")
    print("¿Está Ollama corriendo? Ejecuta: ollama serve")
except Exception as exc:
    print(f"Error: {exc}")


#profesora: A.Plazas