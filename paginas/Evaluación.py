import streamlit as st
import streamlit as st

# Título de la aplicación
st.title("Retroalimentación Interactiva sobre Asíntotas")

# Introducción y nombre
st.subheader("¡Bienvenido! Completa las preguntas para poner a prueba lo aprendido.")
nombre = st.text_input("Digite su nombre:")
if nombre:
    st.markdown(f"Hola, {nombre}, gracias por participar en esta retroalimentación interactiva.")

# Pregunta 1: ¿Qué es una asíntota?
st.caption("**1. ¿Qué es una asíntota?**")
respuesta_1 = st.text_input("Digite su respuesta:")
if respuesta_1:
    st.markdown(f"Su respuesta fue: {respuesta_1}")
    # Retroalimentación
    if "línea" in respuesta_1.lower() and "recta" in respuesta_1.lower():
        st.success("¡Correcto! Una asíntota es una recta a la que se acerca la gráfica de una función.")
    else:
        st.error("¡Incorrecto! Una asíntota es una línea recta que describe el comportamiento de la función a medida que \( x \to \infty \) o \( x \to -\infty \).")

# Pregunta 2: Tipos principales de asíntotas
st.caption("**2. ¿Cuáles son los tipos principales de asíntotas?**")
respuesta_2 = st.text_input("Digita tu respuesta:")
if respuesta_2:
    st.markdown(f"Su respuesta es: {respuesta_2}")
    # Retroalimentación
    if "vertical" in respuesta_2.lower() and "horizontal" in respuesta_2.lower() and "oblicua" in respuesta_2.lower():
        st.success("¡Correcto! Los tipos principales de asíntotas son verticales, horizontales y oblicuas.")
    else:
        st.error("¡Incorrecto! Los tipos principales de asíntotas son verticales, horizontales y oblicuas.")

# Pregunta 3: ¿Cómo se define una asíntota horizontal?
st.caption("**3. ¿Cómo se define una asíntota horizontal?**")
respuesta_3 = st.text_input("Escriba su respuesta:")
if respuesta_3:
    st.markdown(f"Su respuesta fue: {respuesta_3}")
    # Retroalimentación
    if "línea" in respuesta_3.lower() and "y = L" in respuesta_3.lower():
        st.success("¡Correcto! Una asíntota horizontal es una recta \( y = L \) a la que se aproxima la gráfica de la función cuando \( x \to \infty \).")
    else:
        st.error("¡Incorrecto! Una asíntota horizontal es una recta a la que la gráfica de una función se aproxima cuando \( x \to \infty \) o \( x \to -\infty \).")

# Pregunta 4: ¿Qué es una asíntota vertical y cómo se encuentra?
st.caption("**4. ¿Qué es una asíntota vertical y cómo se encuentra?**")
respuesta_4 = st.text_input("Escribe tu respuesta:")
if respuesta_4:
    st.markdown(f"Su respuesta fue: {respuesta_4}")
    # Retroalimentación
    if "denominador" in respuesta_4.lower() and "cero" in respuesta_4.lower():
        st.success("¡Correcto! Una asíntota vertical ocurre cuando el denominador de una fracción se hace cero y el numerador no lo hace.")
    else:
        st.error("¡Incorrecto! Una asíntota vertical se encuentra cuando el denominador de una fracción tiende a cero mientras que el numerador no tiende a cero.")

# Pregunta 5: ¿Cómo se determina si una función tiene una asíntota horizontal?
st.caption("**5. ¿Cómo se determina si una función tiene una asíntota horizontal?**")
respuesta_5 = st.text_input("Su respuesta es:")
if respuesta_5:
    st.markdown(f"Su respuesta fue: {respuesta_5}")
    # Retroalimentación
    if "grado" in respuesta_5.lower() and "denominador" in respuesta_5.lower():
        st.success("¡Correcto! Una función tiene una asíntota horizontal si el grado del numerador es menor o igual al grado del denominador.")
    else:
        st.error("¡Incorrecto! Se determina por la comparación de los grados del numerador y el denominador.")

# Pregunta 6: Diferencia entre asíntota horizontal y vertical
st.caption("**6. ¿Qué diferencia hay entre una asíntota horizontal y una vertical?**")
respuesta_6 = st.text_input("digite su respuesta:")
if respuesta_6:
    st.markdown(f"Su respuesta fue: {respuesta_6}")
    # Retroalimentación
    if "horizontal" in respuesta_6.lower() and "vertical" in respuesta_6.lower() and "dirección" in respuesta_6.lower():
        st.success("¡Correcto! La diferencia es que la asíntota horizontal es paralela al eje \( x \), mientras que la vertical es paralela al eje \( y \).")
    else:
        st.error("¡Incorrecto! La diferencia principal es que la asíntota horizontal es paralela al eje \( x \), mientras que la vertical es paralela al eje \( y \).")

# Pregunta 7: ¿Una función puede tener más de una asíntota horizontal?
st.caption("**7. ¿Una función puede tener más de una asíntota horizontal?**")
respuesta_7 = st.text_input("digita tu respuesta:")
if respuesta_7:
    st.markdown(f"Su respuesta fue: {respuesta_7}")
    # Retroalimentación
    if "no" in respuesta_7.lower():
        st.success("¡Correcto! Una función no puede tener más de una asíntota horizontal.")
    else:
        st.error("¡Incorrecto! Una función solo puede tener una asíntota horizontal.")

# Pregunta 8: ¿Cómo se identifican las asíntotas de una función en su gráfica?
st.caption("**8. ¿Cómo se identifican las asíntotas de una función en su gráfica?**")
respuesta_8 = st.text_input("Tu respuesta fue:")
if respuesta_8:
    st.markdown(f"Su respuesta fue: {respuesta_8}")
    # Retroalimentación
    if "se acercan" in respuesta_8.lower():
        st.success("¡Correcto! Las asíntotas se identifican observando cómo la gráfica de la función se acerca a una recta sin tocarla.")
    else:
        st.error("¡Incorrecto! Las asíntotas se identifican al observar cómo la gráfica se acerca a una recta pero nunca la toca.")

# Pregunta 9: ¿Una asíntota siempre se toca?
st.caption("**9. ¿Una asíntota siempre se toca?**")
respuesta_9 = st.text_input("tu respuesta fue:")
if respuesta_9:
    st.markdown(f"Su respuesta fue: {respuesta_9}")
    # Retroalimentación
    if "no" in respuesta_9.lower():
        st.success("¡Correcto! Las asíntotas nunca se tocan, son solo rectas a las que la función se aproxima.")
    else:
        st.error("¡Incorrecto! Las asíntotas no se tocan, solo las funciones se acercan a ellas a medida que \( x \to \infty \).")

# Pregunta 10: ¿Qué es una asíntota horizontal?
st.caption("**10. ¿Qué es una asíntota horizontal?**")
respuesta_10 = st.text_input("su respuesta es:")
if respuesta_10:
    st.markdown(f"Su respuesta fue: {respuesta_10}")
    # Retroalimentación
    if "línea" in respuesta_10.lower() and "horizontal" in respuesta_10.lower():
        st.success("¡Correcto! Una asíntota horizontal es una recta \( y = L \) a la que la gráfica de la función se aproxima cuando \( x \to \infty \).")
    else:
        st.error("¡Incorrecto! Una asíntota horizontal es una recta a la que se acerca la gráfica de la función a medida que \( x \to \infty \).")

# Rango de puntuación de la página
rango = st.slider("¿Qué puntuación le das a esta página?", min_value=0, max_value=100)
st.markdown(f"El valor que ingresó es: {rango}")

