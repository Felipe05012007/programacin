import streamlit as st


st.title("PRESENTACIÓN PERSONAL")
st.caption("**Mi nombre es Cristian Felipe Sánchez Benavides, soy estudiante de matemáticas de la Universidad Industrial de Santander (UIS), me apasiona la matemática y la programación, y en este proyecto he combinado ambas pasiones para crear una herramienta de manera interactiva que ayude a los estudiantes a aprender sobre las asintotas. El objetivo de este proyecto es proporcionar una plataforma para que los estudiantes puedan explorar y aprender sobre las asintotas ed manera interactiva.**")


st.title("ASINTOTAS")
st.header("QUE ES UNA ASINTOTA?")
st.caption("**Asíntota es un término originario ed grecia que hace referencia a algo que no tiene coincidencia. El concepto se utiliza en el ámbito de la geometría para nombrar a una recta que, a medida que se prolonga de manera indefinida, tiende a acercarse a una cierta curva o función, aunque sin alcanzar a hallarla.**")
st.caption("**Imagina que tienes una línea y una curva en un papel. La curva intenta acercarse a la línea a medida que va avanzando, pero nunca la toca, aunque parece que lo va a hacer. Eso es una asíntota: una línea a la que la curva se acerca mucho, pero siempre sigue separada de ella.**")
st.caption("**Un ejemplo sencillo es la gráfica de y = 1/ x . Esta curva tiene asíntotas en ambos ejes, en el eje de las x y en el eje de las y.**")
st.image("https://www.problemasyecuaciones.com/funciones/asintotas/g1.png")



st.subheader("ASINTOTA HORIZONTAL")
st.caption("Son rectas horizontales asociadas a la función. Se encuentran presentes únicamente en funciones racionales de la forma:")
st.latex(r"f(x) = \frac{g(x)}{h(x)}")
st.caption("Y se determinan haciendo que la variable independiente x, tienda al infinito lo que trae como consecuencia que la función cociente tienda a un valor determinado fijo, al que nunca va a llegar ni a cruzar.Dependiendo de la relación entre los grados de los dos polinomios, se tienen tres casos:")
st.caption("1. El polinomio g(x) y h(x) tienen el mismo grado.La asíntota horizontal es la recta dada por el cociente de los coeficientes de grado mayor."
"Ejemplo: Hallar la asíntota horizontal de la función:")
st.latex(r"f(x) = \frac{6x - 5}{2x + 4}")
st.caption("Solución: Se dividen los coeficientes de los términos de mayor exponente: 6/2 Así, el valor de la asíntota horizontal es: y = 3")
st.caption("2. El grado del polinomio g(x) es menor que el de h(x) en estos casos, la asíntota horizontal es la recta y = 0"
"Ejemplo: Hallar la asíntota horizontal de la función:")
st.latex(r"f(x) = \frac{5x - 2}{x^2 - 2x - 8}")
st.caption("Solución: Como el grado del polinomio del numerador es menor que el del denominador, el valor de la asíntota horizontal es: y = 0")
st.caption("3. El grado del polinomio g(x) es mayor que el de h(x)."
"En estos casos no hay asíntota horizontal."
"Ejemplo: hallar la asinota horizontal de la función:")
st.latex(r"f(x) = \frac{4x - 12}{2}")
st.caption("Solución: Como el grado del polinomio el numerador es mayor ue el del denominador, no existen asíntotas horizontales.")
st.image("https://www.funciones.xyz/wp-content/uploads/2021/04/asintota-horizontal-de-una-funcion.png")
st.subheader("ASINTOTA VERTICAL")
st.caption("Son rectas verticales asociadas a la función. Se encuentran presentes únicamente en funciones racionales de la forma:")
st.latex(r"f(x) = \frac{g(x)}{h(x)}")
st.caption("Y se determinan encontrando las raíces del denominador h(x)correspondiente. El número de raíces asociadas a una función determinan el número de asíntotas verticales que tiene tal función."
"Ejemplo: Hallar las asintotas verticales de la función: ")
st.latex(r" f(x) = \frac{1}{x^2 - 3x - 4}")
st.caption("el polinomio del denominador es de grado dos: $x^2 - 3x - 4 = 0$, que tiene dos raices:")
st.latex(r"x^2 - 3x - 4 = 0 \rightarrow (x - 4)(x + 1) = 0 \rightarrow x - 4 = 0 , x + 1 = 0")
st.caption("Así que los valores de ls asíntotas verticales son: $x = 4$ y $x = -1$")
st.subheader("CONCLUSIÓN")
st.caption("Las asíntotas son rectas a las cuales la función se va aproximando indefinidamente, cuando por lo menos una de las variables (x o y) tienden al infinito. En una función racional, las asíntotas verticales se obtienen de las raíces del polinomio del denominador, mientras que las asíntotas horizontales dependen de la relación que exista entre los grados del polinomio del numerador y del polinomio del denominador.")
st.image("https://www.funciones.xyz/wp-content/uploads/2021/04/asintota-vertical.png")
st.video("https://www.youtube.com/watch?v=VziE5Yu5RW8&pp=ygUzZXhwbGljYWNpb24gZGUgYXNpbnRvdGFzIHZlcnRpY2FsZXMgeSBob3Jpem9udGFsZXMg")

st.subheader("RETROALIMENTACIÓN")
nombre = st.text_input("Digite su nombre:")
st.markdown(f"su nombre es: {nombre}")

st.caption("**1. ¿Qué es una asíntota?**")
nombre = st.text_input("Digite su respuesta:")
st.markdown(f"respuesta: {nombre}")
st.caption("**2. ¿Cuáles son los tipos principales de asíntotas**")
nombre = st.text_input("La respuesta indicada es:")
st.markdown(f"respuesta: {nombre}")
st.caption("**3. ¿Cómo se define una asíntota horizontal?**")
nombre = st.text_input("La solución es:")
st.markdown(f"respuesta: {nombre}")
st.caption("**4. ¿Qué es una asíntota vertical y cómo se encuentra?**")
nombre = st.text_input("La información que solicita es:")
st.markdown(f"respuesta: {nombre}")
st.caption("**5. ¿Cómo se determina si una función tiene una asíntota horizontal?**")
nombre = st.text_input("El dato solicitado es:")
st.markdown(f"respuesta: {nombre}")
st.caption("**6. ¿Qué diferencia hay entre una asíntota horizontal y una vertical?**")
nombre = st.text_input("la respuesta es:")
st.markdown(f"respuesta: {nombre}")
st.caption("**7. ¿Una función puede tener más de una asíntota horizontal?**")
nombre = st.text_input("digite la información:")
st.markdown(f"respuesta: {nombre}")
st.caption("**8. ¿Cómo se identifican las asíntotas de una función en su gráfica?**")
nombre = st.text_input("Digita la información solicitda:")
st.markdown(f"respuesta: {nombre}")
st.caption("**9. ¿Una asíntota siempre se toca?**")
nombre = st.text_input("¿cual es tu respuesta?:")
st.markdown(f"respuesta: {nombre}")
st.caption("**10. ¿Qué es una asintota horizontal?**")
nombre = st.text_input("¿que vas a responder?:")
st.markdown(f"respuesta: {nombre}")

rango = st.slider("¿que puntución le das a mi página?:", min_value=0, max_value=100)
st.markdown(f"el valor que ingresó es: {rango}")



