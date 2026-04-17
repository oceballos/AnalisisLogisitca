from pathlib import Path
import pandas as pd
import rarfile
import gc  # Garbage collector para liberar memoria
import os

RUTA = r"X:\ProyectoLogística-20260403T171349Z-3-002\ProyectoLogística\data\aduanas"
SALIDA = r"X:\ProyectoLogística-20260403T171349Z-3-002\ProyectoLogística\data\aduanas\Entradas_Faltantes"
aduanas_dir = Path(RUTA)
extract_dir = Path(SALIDA)

#revisamos las cabeceras
PATH_CABECERA = r"X:\ProyectoLogística-20260403T171349Z-3-002\ProyectoLogística\data"
CABECERA = "descripcion-y-estructura-de-datos-din.xlsx"
df_cabeceras =pd.read_excel(os.path.join(PATH_CABECERA,CABECERA), sheet_name='Títulos')
column_names = [col.strip() for col in list(df_cabeceras.iloc[0,:])]


rarfile.UNRAR_TOOL = r"C:\Program Files\WinRAR\UnRAR.exe"

archivo_salida_final = aduanas_dir / "aduanas_df_faltante.csv"
archivos_ignorados = []
archivos_procesados = 0

txt_files = sorted(extract_dir.rglob("*.txt"))

# Bandera para saber si escribimos los encabezados del CSV o si solo adjuntamos datos
es_primer_archivo = True
contador = 0

for txt_file in txt_files:
    df_tmp = None
    df_tmp_f = None
    ultimo_error = ""
    contador = contador + 1
    print(f"Revisando el Archivo '{txt_file.name}': {contador}/{len(txt_files)}")
    for separador in [";", ","]:
        try:
            # engine='c' suele ser más rápido para archivos grandes y estrictos
            df_tmp = pd.read_csv(txt_file, sep=separador, low_memory=False, encoding="latin-1", on_bad_lines='skip',
                                 engine='c')
            df_tmp.columns = column_names
            columns_to_combine = ['DNOMBRE', 'DMARCA', 'DVARIEDAD', 'DOTRO1', 'DOTRO2', 'ATR-5', 'ATR-6']
            df_tmp['var'] = df_tmp[columns_to_combine].fillna('').astype(str).agg(' '.join, axis=1)
            df_tmp_f=df_tmp[df_tmp['var'].str.contains('AIRE ACONDICIONADO', na=False, case=False)]
            del df_tmp
            gc.collect()


            break
        except Exception as e:
            ultimo_error = str(e)
            continue

    if df_tmp_f is None:
        print(f"❌ Error al procesar '{txt_file.name}': {ultimo_error}")
        archivos_ignorados.append(txt_file.name)
        continue

    # Añadimos la columna de origen
    df_tmp_f = df_tmp_f.copy()
    df_tmp_f["archivo_origen"] = txt_file.name
    #df_tmp = df_tmp.assign(archivo_origen=txt_file.name)

    # ¡LA MAGIA OCURRE AQUÍ!
    # En lugar de guardar df_tmp en una lista, lo escribimos inmediatamente al disco
    modo_escritura = 'w' if es_primer_archivo else 'a'  # 'w' (write) para el primero, 'a' (append) para los demás

    df_tmp_f.to_csv(archivo_salida_final, sep=';', index=False, encoding="utf-8",
                  mode=modo_escritura, header=es_primer_archivo)

    es_primer_archivo = False  # A partir de ahora, solo adjuntamos (append)
    archivos_procesados += 1

    # Liberamos memoria explícitamente
    del df_tmp_f
    gc.collect()


print(f"\n✅ Proceso completado. Se combinaron {archivos_procesados} archivos directamente en disco.")

if archivos_ignorados:
    print("\n--- ARCHIVOS IGNORADOS ---")
    for ignorado in archivos_ignorados:
        print(f"- {ignorado}")

