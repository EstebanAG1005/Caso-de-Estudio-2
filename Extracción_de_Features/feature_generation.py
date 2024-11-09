import pandas as pd
from datetime import datetime

# 1. Leer los datos generados desde 'actividades.csv'
actividades_df = pd.read_csv('./actividades.csv')

# 2. Convertir la columna 'fecha' a tipo datetime, y manejar errores en fechas no válidas
actividades_df['fecha'] = pd.to_datetime(actividades_df['fecha'], errors='coerce')

# 3. Eliminar filas con fechas nulas (fechas inválidas)
actividades_df.dropna(subset=['fecha'], inplace=True)

# 4. Rellenar valores faltantes en columnas relevantes, como 'distancia_km' y 'duracion_minutos', con 0 o valores adecuados
actividades_df['distancia_km'] = actividades_df['distancia_km'].fillna(0)
actividades_df['duracion_minutos'] = actividades_df['duracion_minutos'].fillna(0)

# 5. Filtrar datos para eliminar filas con duraciones o distancias negativas, que son inválidas
actividades_df = actividades_df[(actividades_df['distancia_km'] >= 0) & (actividades_df['duracion_minutos'] >= 0)]

# 6. Convertir columnas de distancia y duración a tipo numérico para evitar errores de cálculo
actividades_df['distancia_km'] = pd.to_numeric(actividades_df['distancia_km'], errors='coerce')
actividades_df['duracion_minutos'] = pd.to_numeric(actividades_df['duracion_minutos'], errors='coerce')

# 7. Eliminar filas que aún tengan valores nulos en distancia o duración después de convertir a numérico
actividades_df.dropna(subset=['distancia_km', 'duracion_minutos'], inplace=True)

# 8. Agregar columnas de año y semana para agrupar
actividades_df['año'] = actividades_df['fecha'].dt.isocalendar().year
actividades_df['semana'] = actividades_df['fecha'].dt.isocalendar().week

# 9. Calcular la velocidad en cada actividad (km/h), manejar posibles divisiones por cero
actividades_df['velocidad_kmh'] = actividades_df.apply(
    lambda row: row['distancia_km'] / (row['duracion_minutos'] / 60) if row['duracion_minutos'] > 0 else 0, axis=1
)

# 10. Agrupar por atleta, año y semana, y calcular los totales y promedios
resumen_semanal = actividades_df.groupby(['atleta_id', 'año', 'semana']).agg({
    'distancia_km': 'sum',
    'duracion_minutos': 'sum',
    'velocidad_kmh': 'mean'
}).reset_index()

# 11. Renombrar columnas para mayor claridad
resumen_semanal.rename(columns={
    'distancia_km': 'total_distancia_km',
    'duracion_minutos': 'total_duracion_minutos',
    'velocidad_kmh': 'velocidad_promedio_kmh'
}, inplace=True)

# 12. Guardar el resumen semanal en un archivo CSV
resumen_semanal.to_csv('./resumen_semanal.csv', index=False, encoding='utf-8-sig')
print("\nEl resumen semanal ha sido guardado en 'resumen_semanal.csv'.")
