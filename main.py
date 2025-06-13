import streamlit as st

st.title("Evaluación de Habilidades Académicas")
st.markdown("Alan Cervantes, Joel Sánchez, Rodrigo Delgadillo, Saúl Padilla")
st.markdown("**Instrucciones:** Lee cada afirmación y selecciona el número que mejor refleje tu nivel de acuerdo. La escala es la siguiente:")
st.markdown("""
- 1 = Totalmente en desacuerdo  
- 2 = Parcialmente en desacuerdo  
- 3 = Indiferente  
- 4 = Parcialmente de acuerdo  
- 5 = Totalmente de acuerdo
""")

# Función para mostrar ítems y guardar respuestas
def mostrar_items(nombre, items):
    st.subheader(nombre)
    respuestas = []
    for item in items:
        respuesta = st.radio(item, [1, 2, 3, 4, 5], key=item)
        respuestas.append(respuesta)
    return respuestas

# Ítems por dimensión
trabajo_equipo = [
    "Cuando trabajo en equipo, me esfuerzo por escuchar y respetar las ideas de mis compañeros.",
    "Participo activamente en las actividades grupales y cumplo con mis responsabilidades.",
    "Puedo comunicar claramente mis ideas hacia mis compañeros de equipo.",
    "Suelo intervenir de manera asertiva en los conflictos dentro del equipo para resolverlos."
]

trabajo_autonomo = [
    "Completo las tareas escolares en tiempo y forma.",
    "Busco recursos o soluciones por mi cuenta para resolver las dudas que tengo antes de pedir ayuda.",
    "Estudio material de clase constantemente."
]

comprension_lectora = [
    "Puedo identificar las ideas principales y los detalles importantes en los textos que leo.",
    "Comprendo instrucciones escritas sin necesidad de explicaciones adicionales.",
    "Después de leer un texto, puedo resumirlo con mis propias palabras de forma clara."
]

# Identificador del estudiante
nombre = st.text_input("Nombre del estudiante")

# Mostrar ítems y obtener respuestas
respuestas_equipo = mostrar_items("Trabajo en equipo", trabajo_equipo)
respuestas_autonomo = mostrar_items("Trabajo autónomo en casa", trabajo_autonomo)
respuestas_lectora = mostrar_items("Comprensión lectora", comprension_lectora)

# Calcular resultados y guardar
if st.button("Enviar respuestas"):
    total_equipo = sum(respuestas_equipo)
    total_autonomo = sum(respuestas_autonomo)
    total_lectora = sum(respuestas_lectora)
    total_general = total_equipo + total_autonomo + total_lectora

    if total_general >= 41:
        nivel = "Destacado"
    elif total_general >= 31:
        nivel = "Adecuado"
    elif total_general >= 21:
        nivel = "En desarrollo"
    else:
        nivel = "Crítico / Requiere intervención"

    # Construir diccionario de datos
    data = {
        "Nombre": nombre,
        "Trabajo en equipo": total_equipo,
        "Trabajo autónomo en casa": total_autonomo,
        "Comprensión lectora": total_lectora,
        "Total": total_general,
        "Nivel de desempeño": nivel
    }

    df = pd.DataFrame([data])

    archivo = "resultados_evaluacion.xlsx"

    if os.path.exists(archivo):
        df_existente = pd.read_excel(archivo)
        df_final = pd.concat([df_existente, df], ignore_index=True)
    else:
        df_final = df

    df_final.to_excel(archivo, index=False)

    st.success("Respuestas guardadas exitosamente.")
    st.write("Resumen de tus resultados:")
    st.dataframe(df)
