import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://www.aduana.cl/compendio-de-normas-anexo-51/aduana/2009-11-19/163937.html"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

response = requests.get(url, headers=headers)
response.encoding = "utf-8"

soup = BeautifulSoup(response.text, "html.parser")

# Extraer solo las tablas
tablas = pd.read_html(response.text, flavor="bs4")

print(f"Total de tablas encontradas: {len(tablas)}")
for i, tabla in enumerate(tablas):
    print(f"\n--- Tabla {i+1} ---")
    print(tabla.head())


with pd.ExcelWriter("anexo51_tablas.xlsx", engine="openpyxl") as writer:
    for i, tabla in enumerate(tablas):
        nombre_hoja = f"Tabla_{i+1}"[:31]  # Excel limita a 31 caracteres
        tabla.to_excel(writer, sheet_name=nombre_hoja, index=False)

print("Guardado en anexo51_tablas.xlsx")