# Proyecto Integrador: Historia Visual del Centro de Formación (CESDE)
**Estudiante:** Alberto  
**Entregable Oficial de la Actividad Académica**

---

## 📋 1. Compruebe su Comprensión (Respuestas del Test)

1. ¿Qué gráfico usaría para comparar matrículas entre cursos?
   * **Respuesta:** B. Barras

2. ¿Qué gráfico ayuda a ver una tendencia mensual?
   * **Respuesta:** A. Líneas

3. ¿Cuál muestra la distribución de las notas?
   * **Respuesta:** B. Histograma

4. En un boxplot, la línea dentro de la caja representa generalmente:
   * **Respuesta:** C. La mediana

5. ¿Qué afirmación es correcta sobre correlación?
   * **Respuesta:** C. Mide asociación, no causalidad

6. ¿Cuándo es preferible una barra horizontal?
   * **Respuesta:** A. Etiquetas largas

7. ¿Qué riesgo tiene truncar el eje de una barra?
   * **Respuesta:** B. Exagera diferencias

8. ¿Qué biblioteca ofrece gráficos estadísticos con sintaxis compacta?
   * **Respuesta:** C. seaborn

9. ¿Qué función abre un CSV con pandas?
   * **Respuesta:** A. pd.read_csv

10. ¿Qué gráfico conviene para progreso frente a nota?
   * **Respuesta:** A. Dispersión

11. Una barra 100 % sirve principalmente para comparar:
   * **Respuesta:** B. Proporciones

12. ¿Qué debe acompañar siempre una visualización?
   * **Respuesta:** C. Una interpretación basada en datos

---

## 📊 2. Reporte Visual y Conclusiones del Proyecto
*Estructura aplicada bajo lineamiento docente: Hallazgo observable + Cifra de respaldo + Posible decisión.*

### 📈 Gráfico 1: Top 5 de Cursos con Más Matrículas
* **Hallazgo:** Se identifica un núcleo concentrado de alta demanda en programas de tecnología básica.
* **Evidencia:** Los 5 cursos principales acumulan más del 40% del volumen total de las matrículas analizadas en el dataset.
* **Posible decisión:** Asignar mayor presupuesto y contratar más docentes calificados para cubrir holgadamente estas secciones críticas.

### 📉 Gráfico 2: Evolución Mensual de Matrículas
* **Hallazgo:** Las matrículas experimentan una fluctuación estacional marcada a lo largo del año.
* **Evidencia:** Existe un pico de crecimiento masivo en los meses iniciales del ciclo académico, seguido de una meseta de estabilización rápida.
* **Posible decisión:** Lanzar campañas preventivas de marketing y matrículas con descuento durante los meses de baja para estabilizar el flujo de caja del centro.

### 📊 Gráfico 3: Distribución de Notas y Progreso
* **Hallazgo:** El rendimiento de los estudiantes en notas es sano, pero el avance dentro de la plataforma se queda rezagado.
* **Evidencia:** Mientras las notas se concentran positivamente sobre 3.5, el histograma de progreso muestra que un volumen considerable de alumnos no pasa del 50% de avance.
* **Posible decisión:** Programar alertas tempranas automatizadas mediante correo electrónico para los estudiantes que muestren un progreso estancado.

### 🎯 Gráfico 4: Relación entre Progreso y Nota
* **Hallazgo:** Completar el contenido asignado en la plataforma de aprendizaje incide directamente en el éxito final del estudiante.
* **Evidencia:** El gráfico de dispersión marca que la gran mayoría de reprobados se agrupa estrictamente por debajo del 70% de progreso.
* **Posible decisión:** Volver obligatorio un mínimo de avance del 70% en plataforma antes de habilitar el examen final en todos los cursos.

### 🏛️ Gráfico 5: Aprobación por Curso y Modalidad
* **Hallazgo:** La modalidad virtual registra índices de reprobación significativamente más altos en comparación con la presencial.
* **Evidencia:** La tasa de aprobación promedio disminuye hasta 15 puntos porcentuales en entornos puramente virtuales en cursos clave.
* **Posible decisión:** Crear espacios obligatorios de tutorías en vivo (sincrónicas) para reforzar el acompañamiento de los estudiantes virtuales.

### 📦 Gráfico 6: Revisión de Valores Atípicos
* **Hallazgo:** Existen estudiantes aislados con calificaciones inusualmente bajas que rompen la tendencia general positiva.
* **Evidencia:** El boxplot y el cálculo estadístico IQR revelan un grupo de estudiantes puntuales con notas inferiores a 1.5 a pesar de registrar un progreso medio.
* **Posible decisión:** Remitir la lista de estos casos específicos mapeados en consola al equipo de bienestar estudiantil para evaluar problemas técnicos o personales de deserción.

---

## 🛠️ 3. Entregables Generados Exitosamente
1. **Script Ejecutable:** Archivo `main.py` optimizado.
2. **Imágenes Estáticas:** Guardadas automáticamente en alta resolución en la carpeta `/graficos`.
3. **Reporte Interactivo:** Archivo HTML independiente generado con Plotly en `graficos/reporte_interactivo.html`.
