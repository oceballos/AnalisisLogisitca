import requests
import pandas as pd
from bs4 import BeautifulSoup
from io import StringIO

url = "https://www.aduana.cl/compendio-de-normas-anexo-51/aduana/2009-11-19/163937.html"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

response = requests.get(url, headers=headers)
response.encoding = "utf-8"
soup = BeautifulSoup(response.text, "html.parser")

# Parseo de tablas que ya funcionaba
tablas = pd.read_html(StringIO(response.text))

# Títulos por separado, sin tocar el parseo
def get_titulo(table):
    for tag in table.find_all_previous(["p", "b", "strong", "h1", "h2", "h3", "h4"]):
        texto = tag.get_text(separator=" ", strip=True)
        if texto and len(texto) > 3:
            return texto[:120]
    return "Sin título"

titulos = [get_titulo(t) for t in soup.find_all("table")]

# Exportar
indice = []
with pd.ExcelWriter("anexo51_tablas.xlsx", engine="openpyxl") as writer:
    for i, df in enumerate(tablas):
        nombre_hoja = f"Tabla_{i+1}"[:31]
        df.to_excel(writer, sheet_name=nombre_hoja, index=False)
        indice.append({"hoja": nombre_hoja, "titulo": titulos[i] if i < len(titulos) else "Sin título"})

pd.DataFrame(indice).to_csv("anexo51_indice.csv", index=False, encoding="utf-8-sig")

print(f"{len(indice)} tablas exportadas")
for item in indice:
    print(f"  {item['hoja']}: {item['titulo']}")