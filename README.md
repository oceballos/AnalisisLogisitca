# Evolución de las importaciones de equipos e insumos de aire acondicionado en Chile

## Fuentes de datos

Este proyecto utiliza fuentes oficiales y abiertas para construir un análisis exploratorio de las importaciones de equipos de Aire Acondicionado en Chile:

- **Datos de importaciones de Chile** publicados en el portal de datos abiertos del Gobierno de Chile. Se extrajeron por `API Ckan` de datos.gov
- **Indicadores macroeconómicos del Banco Central de Chile** incluyendo series como IMACEC, IPC y M1. Se extraen usando `API BDE` del Banco Central
- **Documentación asociada a los datasets**, utilizada para entender la estructura de los archivos, su periodicidad y cobertura temporal.
   
Las fuentes permiten combinar información de comercio exterior con variables macroeconómicas para observar posibles patrones, cambios de tendencia y relaciones temporales.

>Nota: En este repositorio no se encuentran los datos para la ejecución del proyecto, para su extracción y descarga, utilizar notebook

## Análisis

El análisis se orienta a estimar, de forma exploratoria, la evolución histórica de las imoportaciones de aire acondicionado 
con un foco geográfico y de costos.

El análisis se encuentra en `informe` con el nombre **Informe trabajo logística final.docx**

## Ejecución

Para reproducir el análisis se recomienda:

1. **Opcional** Descarga de datos (ya están archivos consolidados en el directorio `data`)
   - Ejecutar el notebook **ExtraccionDataSoloAduanasyCentral.ipynb** 
   - Ejecutar en consola: `python ExtraccionAPI_pendientes.py`
   - Ejecutar en consola: `python scrapperCodigosAduanas.py`
   - Ejecutar en consola: `python "1.0 Extracción del RAR.py"`
   - Ejecutar en consola: `python "2.0 Acumulacion del TXT.py"`
   - Ejecutar en consola: `python "Modeificar Nombre.py"`
2. Entrar a drive carpeta `src` y abrir el notebook **Analisis_completo.ipynb**.
   - Ejecutar las celdas en orden, desde la carga de datos hasta la construcción de las series analizadas.
3. Revisar los gráficos, tablas y salidas intermedias generadas durante la ejecución.

Si deseas correr el proyecto en un entorno limpio, asegúrate de contar con acceso a internet para descargar las fuentes públicas.

## Reproductibilidad

Para mantener la reproducibilidad del análisis:

- Usar la misma versión de Python o una compatible con el notebook.
- Mantener las mismas fuentes de datos y fechas de descarga.
- Ejecutar las transformaciones en el mismo orden.
- Evitar modificaciones manuales sobre los archivos originales.
- Guardar una copia de los datos procesados cuando se quiera comparar resultados entre ejecuciones.



**Autoría:** proyecto de análisis de datos sobre importaciones de equipos e insumos de aires acondicionado en Chile.

Osvaldo Ceballos Olivares osvaldo.ceballos@mail.udp.cl
Yerko Fuentes yerko.fuentes@mail.udp.cl 
Paloma San Martin paloma.sanmartin@mail.udp.cl 
