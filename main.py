from pathlib import Path
import sqlite3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# ==========================================
# 1. CONFIGURACIÓN DE RUTAS Y ESTILOS
# ==========================================
BASE = Path(__file__).resolve().parent
GRAFICOS = BASE / 'graficos'
GRAFICOS.mkdir(parents=True, exist_ok=True)

# Paleta legible, accesible y limpia
sns.set_theme(style='whitegrid', palette='colorblind')

# ==========================================
# 2. CARGA DIRECTA DEL DATASET ANALÍTICO
# ==========================================
ruta_csv = BASE / 'data' / 'processed' / 'dataset_analitico.csv'

try:
    df = pd.read_csv(ruta_csv, parse_dates=['fecha'])
    print("¡Estructura inicial verificada!")
    print(f"Dataset cargado con {df.shape[0]} filas y {df.shape[1]} columnas.\n")
except FileNotFoundError:
    print(f"Error: No se encontró el archivo en {ruta_csv}. Verifica las carpetas.")
    exit()

# Asegurar que existan variables de apoyo para graficar
columna_hue = 'estado' if 'estado' in df.columns else 'aprobado'

# ==========================================
# 3. CONSTRUCCIÓN DE LA HISTORIA VISUAL
# ==========================================

print("Generando Gráfico 1: Top 5 Cursos (Familia: Barras horizontales)...")
top5 = df['curso'].value_counts().nlargest(5).sort_values()
fig, ax = plt.subplots(figsize=(8, 4))
top5.plot.barh(color='#17365D', ax=ax)
ax.set_title('Cinco Cursos con Mayor Volumen de Matrículas', pad=15, fontweight='bold')
ax.set_xlabel('Cantidad Total de Matrículas')
ax.set_ylabel('Nombre del Curso')
plt.annotate('Fuente: Registro Interno CESDE', xy=(0.5, -0.2), xycoords='axes fraction', ha='center', fontsize=9, color='gray')
plt.tight_layout()
plt.savefig(GRAFICOS / '01_top5_cursos.png', dpi=150)
plt.close()

print("Generando Gráfico 2: Evolución Mensual (Familia: Líneas)...")
mensual = df.groupby(df['fecha'].dt.to_period('M')).size()
mensual.index = mensual.index.astype(str)
fig, ax = plt.subplots(figsize=(8, 4))
mensual.plot(marker='o', color='#E91E75', linewidth=2, ax=ax)
ax.set_title('Evolución Mensual de Matrículas', pad=15, fontweight='bold')
ax.set_xlabel('Período de Tiempo (Año-Mes)')
ax.set_ylabel('Cantidad de Matrículas')
plt.annotate('Fuente: Registro Interno CESDE', xy=(0.5, -0.2), xycoords='axes fraction', ha='center', fontsize=9, color='gray')
plt.tight_layout()
plt.savefig(GRAFICOS / '02_evolucion_mensual.png', dpi=150)
plt.close()

print("Generando Gráfico 3: Distribución (Familia: Histograma Estadístico)...")
fig, ejes = plt.subplots(1, 2, figsize=(11, 4.5))
sns.histplot(data=df, x='nota', bins=12, color='#2ca02c', kde=True, ax=ejes[0])
sns.histplot(data=df, x='progreso', bins=12, color='#1f77b4', kde=True, ax=ejes[1])
ejes[0].set_title('Distribución de Notas Obtenidas', fontweight='bold')
ejes[0].set_xlabel('Nota Final')
ejes[0].set_ylabel('Frecuencia Absoluta')
ejes[1].set_title('Distribución del Progreso en Plataforma', fontweight='bold')
ejes[1].set_xlabel('Porcentaje de Progreso (%)')
ejes[1].set_ylabel('Frecuencia Absoluta')
plt.suptitle('Análisis de Distribuciones Académicas', fontsize=14, fontweight='bold', y=0.98)
plt.tight_layout()
plt.savefig(GRAFICOS / '03_distribucion_notas_progreso.png', dpi=150)
plt.close()

print("Generando Gráfico 4: Relación (Familia: Dispersión / Scatter)...")
fig, ax = plt.subplots(figsize=(8, 4.5))
sns.scatterplot(data=df, x='progreso', y='nota', hue=columna_hue, alpha=0.75, ax=ax)
ax.set_title('Relación entre el Progreso en Plataforma y la Nota Final', pad=15, fontweight='bold')
ax.set_xlabel('Progreso del Estudiante (%)')
ax.set_ylabel('Nota Obtenida')
plt.tight_layout()
plt.savefig(GRAFICOS / '04_relacion_progreso_nota.png', dpi=150)
plt.close()

print("Generando Gráfico 5: Aprobación (Familia: Barras Agrupadas)...")
aprobacion = (df.groupby(['curso', 'modalidad'])['aprobado']
             .mean().mul(100).reset_index(name='tasa_aprobacion'))
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(data=aprobacion, x='curso', y='tasa_aprobacion', hue='modalidad', ax=ax)
ax.set_title('Tasa de Aprobación por Curso y Modalidad de Aprendizaje', pad=15, fontweight='bold')
ax.set_xlabel('Curso Dictado')
ax.set_ylabel('Tasa de Aprobación (%)')
plt.xticks(rotation=25, ha='right')
plt.tight_layout()
plt.savefig(GRAFICOS / '05_aprobacion_curso_modalidad.png', dpi=150)
plt.close()

print("Generando Gráfico 6 y Filtro: Valores Atípicos (Familia: Caja y Bigotes / Boxplot)...")
q1, q3 = df['nota'].quantile([0.25, 0.75])
iqr = q3 - q1
atipicos = df[(df['nota'] < q1 - 1.5*iqr) | (df['nota'] > q3 + 1.5*iqr)]
print("\n--- Alertas de Estudiantes con Valores Atípicos Detectados ---")
if not atipicos.empty:
    columnas_disponibles = [col for col in ['nombre', 'curso', 'nota', 'progreso'] if col in df.columns]
    print(atipicos[columnas_disponibles].head())
else:
    print("No se registran anomalías severas bajo el criterio estadístico IQR.")

fig, ax = plt.subplots(figsize=(7, 3))
sns.boxplot(data=df, x='nota', color='#ff7f0e', ax=ax)
ax.set_title('Identificación de Anomalías en Distribución de Notas (Boxplot)', pad=12, fontweight='bold')
ax.set_xlabel('Calificación')
plt.tight_layout()
plt.savefig(GRAFICOS / '06_revision_atipicos.png', dpi=150)
plt.close()

print("\nGenerando Reporte Interactivo Final (Familia: Interactivos HTML)...")
fig_html = px.scatter(df, x='progreso', y='nota', color=columna_hue,
                 hover_data=['curso', 'modalidad'] if 'nombre' not in df.columns else ['nombre', 'curso', 'modalidad'],
                 title='Reporte de Progreso y Nota por Estudiante (Interactividad Plena)')
fig_html.write_html(GRAFICOS / 'reporte_interactivo.html')

print("\n========================================================")
print("¡PROYECTO COMPILADO CON ÉXITO!")
print("Revisa tu panel de archivos; las imágenes se guardaron en la carpeta 'graficos/'.")
print("========================================================")
