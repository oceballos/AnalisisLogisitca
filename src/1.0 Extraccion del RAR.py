from pathlib import Path
import pandas as pd
import rarfile

RUTA = r"X:\ProyectoLogística-20260403T171349Z-3-002\ProyectoLogística\data\aduanas\faltantes-20260405T211610Z-3-001\faltantes"
SALIDA = r"X:\ProyectoLogística-20260403T171349Z-3-002\ProyectoLogística\data\aduanas\Entradas_Faltantes"
aduanas_dir = Path(RUTA)
extract_dir = Path(SALIDA)

rarfile.UNRAR_TOOL = r"C:\Program Files\WinRAR\UnRAR.exe"  # comentar si se trabaja con linux/unix

df_list = []
archivos_ignorados = []  # Lista para registrar los archivos defectuosos
archivos_defectuosos = []

part01_files = sorted(aduanas_dir.glob("*.part01.rar"))

for rar_file in part01_files:
    try:
        print(f"Procesando: {rar_file.name}...")
        with rarfile.RarFile(rar_file) as rf:
            # Validar integridad antes de extraer
            error_check = rf.testrar()
            if error_check is None:
                rf.extractall(path=extract_dir)
                print(f"✅ Extraído: {rar_file.name}")
            else:
                print(f"❌ Error interno en volumen: {rar_file.name}")
                archivos_defectuosos.append(rar_file.name)

    except (rarfile.BadRarFile, rarfile.Error) as e:
        print(f"⚠️ Archivo corrupto o incompleto: {rar_file.name}. Error: {e}")
        archivos_defectuosos.append(rar_file.name)
    except Exception as e:
        print(f"🔥 Error inesperado en {rar_file.name}: {e}")

print(f"\nProceso finalizado. Archivos fallidos: {len(archivos_defectuosos)}")
