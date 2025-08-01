
# CÓDIGO PARA MAPEAR CARRERAS - LISTO PARA USAR
# =============================================

import pandas as pd
import matplotlib.pyplot as plt

# Diccionario de mapeo
mapeo_carreras = {
    'Ingeniería Comercial': 'Ingeniería Comercial y Empresarial',
    'Auditoría y Control de Gestión FCSH': 'Auditoría y Control de Gestión',
    'Auditoría y Control de Gestión FCNM': 'Auditoría y Control de Gestión',
    'Logística y Transporte': 'Logistica y Transporte',
    'Tesis de Turismo': 'Turismo',
    'Ingenieria Agropecuaria': 'Ingeniería Agrícola y Biológica',
    'Ingeniería de Gestión Empresarial Internacional': 'Ingeniería en Negocios Internacionales',
    'Ingeniería en Marketing': 'Administración de Empresas',
    'Licenciatura en Web y Aplicaciones Multimedia': 'Licenciatura en Diseño Web y Aplicaciones Multimedia',
    'Licenciatura en Administración Tecnológica': 'Administración de Empresas',
    'Análisis de Sistemas': 'Licenciatura en Sistemas de Información',
    'Ingeniería en Ciencias Computacionales Orientación Sistemas Multimedia': 'Computación',
    'Ingeniería en Ciencias Computacionales Orientación Sistemas de Información': 'Ingeniería en Ciencias Computacionales',
    'Economía Con Mención en Gestión Empresarial Esp. Marketing': 'Economía con Mención en Gestión Empresarial',
    'Diplomado Superior en Contaduría Pública y Finanzas con aplicación a la Informática': 'Ingeniería en Auditoría y Contaduría Pública Autorizada',
    'Ingeniería en Auditoría y Control de Gestión. Calidad de Procesos': 'Auditoría y Control de Gestión',
    'Diplomado en Evaluación y Dirección de Proyectos de Inversión': 'Administración de Empresas',
    'Ciencias Biológicas': 'Biología',
    'Programador de Sistemas': 'Computación'
}

# PASO 1: Aplicar el mapeo
df_projects_complete_no_activas_mapped = df_projects_complete_no_activas.copy()
df_projects_complete_no_activas_mapped['CARRERA'] = df_projects_complete_no_activas_mapped['CARRERA'].replace(mapeo_carreras)

# PASO 2: Verificar resultados
print("CARRERAS DESPUÉS DEL MAPEO:")
print("="*40)
print(df_projects_complete_no_activas_mapped["CARRERA"].value_counts())

# PASO 3: Combinar dataframes (opcional)
df_activas_copy = df_projects_complete_activas.copy()
df_no_activas_copy = df_projects_complete_no_activas_mapped.copy()

df_activas_copy['ESTADO'] = 'Activa'
df_no_activas_copy['ESTADO'] = 'No Activa'

df_projects_combined = pd.concat([df_activas_copy, df_no_activas_copy], ignore_index=True)

# PASO 4: Crear visualizaciones
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 8))

# Gráfico de carreras activas
df_projects_complete_activas["CARRERA"].value_counts().head(15).plot(
    kind='bar', ax=ax1, title='Top 15 Carreras - Proyectos Activos', color='skyblue'
)
ax1.tick_params(axis='x', rotation=45)
ax1.set_ylabel('Número de Proyectos')

# Gráfico de carreras no activas (después del mapeo)
df_projects_complete_no_activas_mapped["CARRERA"].value_counts().head(15).plot(
    kind='bar', ax=ax2, title='Top 15 Carreras - Proyectos No Activos (Mapeadas)', color='lightcoral'
)
ax2.tick_params(axis='x', rotation=45)
ax2.set_ylabel('Número de Proyectos')

plt.tight_layout()
plt.show()

# PASO 5: Estadísticas comparativas
print("\nESTADÍSTICAS COMPARATIVAS:")
print("="*40)
print(f"Carreras únicas en activas: {df_projects_complete_activas['CARRERA'].nunique()}")
print(f"Carreras únicas en no activas (original): {df_projects_complete_no_activas['CARRERA'].nunique()}")
print(f"Carreras únicas en no activas (mapeadas): {df_projects_complete_no_activas_mapped['CARRERA'].nunique()}")
print(f"Total de proyectos activos: {len(df_projects_complete_activas)}")
print(f"Total de proyectos no activos: {len(df_projects_complete_no_activas_mapped)}")
print(f"Total de proyectos combinados: {len(df_projects_combined)}")
