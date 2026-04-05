import os
import urllib
import requests
from ckanapi import RemoteCKAN

ckan = RemoteCKAN('https://datos.gob.cl')

recursos = {
    2018: "c2f1008d-b84f-49cd-ba27-16cb7e842f38",
    2020:  "6ed59525-1ff2-44d9-a26f-0e9078ca45d0",
    2023: "d1a42e81-b874-4964-9b3d-74dc0f813eae",
    2024: "096c3946-657e-420f-ae74-2337c00b5ba2",
    2025: "385fb63b-c898-4690-aa3f-d59d933fc30c",
}

carpeta_destino = os.path.abspath(os.path.join(os.getcwd(), "..", "data","aduanas","faltantes"))
os.makedirs(carpeta_destino, exist_ok=True)


def sanitizar_nombre_archivo(nombre: str) -> str:
    """Reemplaza caracteres inválidos en nombres de archivo de Windows."""
    caracteres_invalidos = r'<>:"/\|?*'
    for char in caracteres_invalidos:
        nombre = nombre.replace(char, '_')
    return nombre


def descargar_archivo(url: str, destino: str, chunk_size: int = 1024 * 1024):
    response = requests.get(url, stream=True)
    response.raise_for_status()

    total = int(response.headers.get('content-length', 0))
    descargado = 0

    with open(destino, 'wb') as f:
        for chunk in response.iter_content(chunk_size=chunk_size):
            if chunk:
                f.write(chunk)
                descargado += len(chunk)
                if total:
                    pct = descargado / total * 100
                    print(f"  {os.path.basename(destino)}: {pct:.1f}% ({descargado/1e6:.1f} MB / {total/1e6:.1f} MB)", end='\r')
    print(f"\n  ✓ {os.path.basename(destino)} descargado")


for año, dataset_id in recursos.items():
    print(f"\n{'='*50}")
    print(f"Procesando año {año}...")

    dataset = ckan.action.package_show(id=dataset_id)
    print(f"  Dataset: {dataset['title']}")
    print(f"  Recursos encontrados: {len(dataset['resources'])}")

    for resource in dataset['resources']:
        url    = resource['url']
        nombre = resource['name']
        # Sanitizar el nombre del recurso para evitar caracteres inválidos
        nombre_sanitizado = sanitizar_nombre_archivo(nombre)
        # Extraer extensión desde la url o usar el formato del recurso
        ext    = os.path.splitext(url)[-1] or f".{resource['format'].lower()}"
        nombre_archivo = f"{año}_{nombre_sanitizado}{ext}"
        destino = os.path.join(carpeta_destino, nombre_archivo)

        print(f"\n  Descargando: {nombre} ({resource['format']})")

        if os.path.exists(destino):
            print(f"  ⚠ Ya existe, saltando...")
            continue

        descargar_archivo(url, destino)

print(f"\n✓ Todo descargado en '{carpeta_destino}'")