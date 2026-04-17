import os





def iterar_nombre(buscar,reemplazar,folder):
    for filename in os.listdir(folder):
        if buscar in filename:
            # Crear la nueva ruta
            nuevo_nombre = filename.replace(buscar, reemplazar)

            # Renombrar usando os.rename()
            os.rename(
                os.path.join(folder, filename),
                os.path.join(folder, nuevo_nombre)
            )
            print(f"Renombrado: {filename} a {nuevo_nombre}")

ruta = r"X:\ProyectoLogística-20260403T171349Z-3-002\ProyectoLogística\data\aduanas\faltantes-20260405T211610Z-3-001\faltantes"
reemplazo = ''
busco = ''
for i in range(3,7):

    for a in range(1,i+1):
        busco = str(a)+"_"+str(i)
        reemplazo = '.part0'+str(a)
        iterar_nombre(busco,reemplazo,ruta)

