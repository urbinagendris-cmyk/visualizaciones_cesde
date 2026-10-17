from pathlib import Path
import sqlite3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# 1. Configuración de rutas y estilos (lo que te dio la universidad)
BASE = Path(__file__).resolve().parent
GRAFICOS = BASE / 'graficos'
GRAFICOS.mkdir(parents=True, exist_ok=True)
sns.set_theme(style='whitegrid', palette='colorblind')

# 2. Carga directa del dataset analítico ya preparado
ruta_csv = BASE / 'data' / 'processed' / 'dataset_analitico.csv'
df = pd.read_csv(ruta_csv, parse_dates=['fecha'])

# ==========================================
# 4. PRUEBA DE VISUALIZACIONES (Código de la U)
# ==========================================

# Ejemplo 1: Pandas - Gráfico rápido de los 5 cursos más populares
# (Este gráfico se mostrará rápido si usas un entorno interactivo)
print("\nGenerando vista rápida de cursos...")
df['curso'].value_counts().head(5).plot.bar()

# Ejemplo de Plotly: Gráfico interactivo de Progreso y Nota
# NOTA: Verificamos si existe la columna 'estado', si no, usamos 'aprobado'
columna_color = 'estado' if 'estado' in df.columns else 'aprobado'

print("Generando reporte interactivo en HTML...")
fig = px.scatter(df, x='progreso', y='nota', color=columna_color,
                 hover_data=['curso'] if 'nombre' not in df.columns else ['curso', 'nombre'],
                 title='Progreso y nota')

# Esto abrirá una pestaña en tu navegador web con el gráfico interactivo
fig.show()

# Esto guardará el archivo en la carpeta 'graficos' que se creó automáticamente
fig.write_html(GRAFICOS / 'reporte_interactivo.html')
print("¡Reporte guardado con éxito en la carpeta 'graficos'!")


# 3. Verificación de los datos en la terminal
print("¡Datos cargados con éxito!")
print("Dimensiones del dataset (Filas, Columnas):", df.shape)
print("\nPrimeras 5 filas del proyecto:")
print(df.head())