# CSV Processing Script

## Descripcion General
El script de procesamiento CSV es una herramienta de Python diseñada para analizar archivos CSV que contienen datos relacionados con las métricas de desempeño de los agentes. Lee archivos CSV de un directorio específico, extrae datos relevantes y genera una tabla de resumen con las métricas de desempeño de los agentes para un mes determinado.

## Caracteristicas
- Procesar multiples archivos de CSV
- Extraer agentes y valores de total handled and callback handled y los asigna a su respectiva casilla dependiendo del dia.
- Genera una tabla de resumen de la metrica de los agentes.
- Soporta formatos de fecha y meses para futuras tablas.

## Usage
1. **Instalar Python**: Asegurate de tener Python3 descargado. Si no lo tienes puedes descargarlo de su pagina [official website](https://www.python.org/downloads/).

2. **Clonar o descargar el repositorio**: Clonar o Descargar el repositorio.

3. **Instalar las dependencias**: Instalar los paquetes requeridos para poder correr el programa en la terminal de python.:
   ```bash
   pip install pandas openpyxl

4. **Correr el Script (Run)**: Ejecutar `script.py` para poder correr el script.

5. **Seleccionar la carpeta**: Click en "Browse" selecciona la carpeta que contiene el template y todos los archivos CSV que quieres que se procesen.

6. **Generar los resultados**: Click en "Generate Result" para que procese todos los CSV y te genere la tabla.

7. **Guardar la tabla de salida**: Selecciona una ubicacion para exportar la tabla de Excel que va a contener la tabla generada.

## Estructura de los Archivos
- `script.py`: Script de Python para procesar los archivos CSV y generar el resumen de en una tabla.
- `README.md`: Pequeña documentacion del programa.
- `template.xlsx`: Esta seria la tabla que sirve como "template" ejemplo para que el programa escriba los valores.
- `LICENSE`: License information for the script (optional).

## Requerimientos
- Python 3.x
- pandas
- openpyxl

## Licencia
Este proyecto esta bajo la licencia de libre uso de GNU - Mirar [LICENSE](LICENSE) para mas informacion.
