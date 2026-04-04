# Impacto estimado de la eliminación del MEPCO en las importaciones de Chile

## Fuentes de datos

Este proyecto utiliza fuentes oficiales y abiertas para construir un análisis exploratorio del posible impacto de la eliminación del MEPCO sobre las importaciones en Chile:

- **Datos de importaciones de Chile** publicados en el portal de datos abiertos del Gobierno de Chile. Se extrajeron por `API Ckan` de datos.gov
- **Indicadores macroeconómicos del Banco Central de Chile** incluyendo series como IMACEC, IPC y M1. Se extraen usando `API BDE` del Banco Central
- **Documentación asociada a los datasets**, utilizada para entender la estructura de los archivos, su periodicidad y cobertura temporal.
   -
Las fuentes permiten combinar información de comercio exterior con variables macroeconómicas para observar posibles patrones, cambios de tendencia y relaciones temporales.

>Nota: En este repositorio no se encuentran los datos para la ejecución del proyecto, para su extracción y descarga, utilizar notebook 

## Análisis

El análisis se orienta a estimar, de forma exploratoria, cómo podría reflejarse la eliminación del MEPCO en las importaciones de Chile. Para ello se consideran, entre otros, los siguientes pasos:

1. **Recolección de datos**
   Se obtienen los datos desde las APIs o fuentes descargables disponibles, se dejan en la estructura de carpetas necesaria para el proyecto.

2. **Depuración y Normalización temporal**  
   Se consolidan registros mensuales de importaciones y series macroeconómicas en una estructura comparable por fecha. Las series se alinean a frecuencia mensual para facilitar la comparación entre variables.

3. **Exploración descriptiva**  
   Se revisan tendencias, variaciones y posibles quiebres antes y después de fechas de interés.

4. **Relación entre variables**  
   Se examina la evolución conjunta de importaciones, actividad económica e indicadores de precios y junto con el precio de los combustibles (Diesel y Gasolina).

5. **Proyección e Interpretación del impacto estimado**  
   Los resultados se interpretan como una aproximación analítica, no como una causalidad definitiva.

> Nota: este repositorio se enfoca en un ejercicio de análisis de datos; los resultados deben leerse como una estimación preliminar.

## Ejecución

Para reproducir el análisis se recomienda:

1. Abrir el notebook principal del proyecto.
2. Verificar que el entorno de Python tenga instaladas las dependencias necesarias.
3. Ejecutar las celdas en orden, desde la carga de datos hasta la construcción de las series analizadas.
4. Revisar los gráficos, tablas y salidas intermedias generadas durante la ejecución.

Si deseas correr el proyecto en un entorno limpio, asegúrate de contar con acceso a internet para descargar las fuentes públicas.

## Reproductibilidad

Para mantener la reproducibilidad del análisis:

- Usar la misma versión de Python o una compatible con el notebook.
- Mantener las mismas fuentes de datos y fechas de descarga.
- Ejecutar las transformaciones en el mismo orden.
- Evitar modificaciones manuales sobre los archivos originales.
- Guardar una copia de los datos procesados cuando se quiera comparar resultados entre ejecuciones.

Recomendaciones adicionales:

- Registrar la fecha de actualización de cada fuente.
- Documentar cualquier filtrado, imputación o ajuste aplicado a las series.
- Versionar los cambios relevantes del notebook y de los datos derivados.

---

**Autoría:** proyecto de análisis de datos sobre importaciones y variables macroeconómicas de Chile.

Osvaldo Ceballos Olivares osvaldo.ceballos@mail.udp.cl
Yerko Fuentes yerko.fuentes@mail.udp.cl 
Paloma San Martin paloma.sanmartin@mail.udp.cl 
