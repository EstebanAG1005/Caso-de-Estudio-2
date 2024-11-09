import pandas as pd
import random
import numpy as np
from datetime import datetime, timedelta

# 1. Definir las Tablas Atletas y Actividades

# Definir las columnas para las tablas Atletas y Actividades
atletas_columns = ['id', 'nombre', 'edad', 'genero', 'score_esfuerzo']
atletas_df = pd.DataFrame(columns=atletas_columns)

actividades_columns = ['id', 'atleta_id', 'tipo_actividad', 'duracion_minutos', 'distancia_km', 'fecha']
actividades_df = pd.DataFrame(columns=actividades_columns)

# 2. Generar Datos Artificiales para Atletas y Actividades

# Generar 50 atletas
num_atletas = 50
nuevos_atletas = []
for i in range(1, num_atletas + 1):
    atleta_nombre = f"Atleta_{i}"
    edad = random.randint(18, 60)  # Edad entre 18 y 60 años
    genero = random.choice(['M', 'F'])  # Género masculino o femenino
    score_esfuerzo = 0  # Se actualizará después
    nuevos_atletas.append({
        'id': i,
        'nombre': atleta_nombre,
        'edad': edad,
        'genero': genero,
        'score_esfuerzo': score_esfuerzo
    })

# Convertir la lista de atletas a DataFrame
atletas_df = pd.DataFrame(nuevos_atletas)

# Generar actividades para los atletas en un período de dos meses
actividades = ['Caminadora', 'Correr al aire libre', 'Entrenamiento de resistencia', 'Intervalos de velocidad']
fecha_inicio = datetime.now()
fecha_fin = fecha_inicio + timedelta(days=60)
delta = fecha_fin - fecha_inicio

actividad_id_counter = 1
nuevas_actividades = []

for atleta in nuevos_atletas:
    num_actividades_atleta = random.randint(20, 40)  # Cada atleta realiza entre 20 y 40 actividades
    for _ in range(num_actividades_atleta):
        tipo_actividad = random.choice(actividades)
        duracion_minutos = random.randint(30, 120)  # Duración entre 30 y 120 minutos
        distancia_km = round(duracion_minutos * random.uniform(0.08, 0.15), 2)  # Distancia proporcional a la duración
        fecha = fecha_inicio + timedelta(days=random.randint(0, delta.days))
        fecha_str = fecha.strftime('%Y-%m-%d')
        nuevas_actividades.append({
            'id': actividad_id_counter,
            'atleta_id': atleta['id'],
            'tipo_actividad': tipo_actividad,
            'duracion_minutos': duracion_minutos,
            'distancia_km': distancia_km,
            'fecha': fecha_str
        })
        # Actualizar el score de esfuerzo del atleta
        factor_distancia = 1.5
        factor_duracion = 0.5
        nuevo_score = distancia_km * factor_distancia + duracion_minutos * factor_duracion
        atleta['score_esfuerzo'] += nuevo_score

        actividad_id_counter += 1

# Convertir la lista de actividades a DataFrame
actividades_df = pd.DataFrame(nuevas_actividades)

# Actualizar el score_esfuerzo en el DataFrame de atletas
atletas_df['score_esfuerzo'] = [atleta['score_esfuerzo'] for atleta in nuevos_atletas]

# 3. Guardar los Datos en Archivos CSV

# Guardar el DataFrame de atletas en un archivo CSV
atletas_df.to_csv('./atletas.csv', index=False, encoding='utf-8-sig')
print("\nLos datos de atletas han sido guardados en 'atletas.csv'.")

# Guardar el DataFrame de actividades en un archivo CSV
actividades_df.to_csv('./actividades.csv', index=False, encoding='utf-8-sig')
print("Los datos de actividades han sido guardados en 'actividades.csv'.")
