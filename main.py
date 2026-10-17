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


# 3. Verificación de los datos en la terminal
print("¡Datos cargados con éxito!")
print("Dimensiones del dataset (Filas, Columnas):", df.shape)
print("\nPrimeras 5 filas del proyecto:")
print(df.head())