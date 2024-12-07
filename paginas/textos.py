import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("ASINTOTAS")
st.header("QUE ES UNA ASINTOTA?")
st.markdown("**Asíntota es un término originario ed grecia que hace referencia a algo que no tiene coincidencia. El concepto se utiliza en el ámbito de la geometría para nombrar a una recta que, a medida que se prolonga de manera indefinida, tiende a acercarse a una cierta curva o función, aunque sin alcanzar a hallarla.**")
st.markdown("**Imagina que tienes una línea y una curva en un papel. La curva intenta acercarse a la línea a medida que va avanzando, pero nunca la toca, aunque parece que lo va a hacer. Eso es una asíntota: una línea a la que la curva se acerca mucho, pero siempre sigue separada de ella.**")
st.markdown("**Un ejemplo sencillo es la gráfica de y = 1/ x . Esta curva tiene asíntotas en ambos ejes, en el eje de las x y en el eje de las y.**")
st.image("https://www.problemasyecuaciones.com/funciones/asintotas/g1.png")



st.subheader("ASINTOTA HORIZONTAL")
st.markdown("Son rectas horizontales asociadas a la función. Se encuentran presentes únicamente en funciones racionales de la forma:")
st.latex(r"f(x) = \frac{g(x)}{h(x)}")
st.markdown("Y se determinan haciendo que la variable independiente x, tienda al infinito lo que trae como consecuencia que la función cociente tienda a un valor determinado fijo, al que nunca va a llegar ni a cruzar.Dependiendo de la relación entre los grados de los dos polinomios, se tienen tres casos:")
st.markdown("1. El polinomio g(x) y h(x) tienen el mismo grado.La asíntota horizontal es la recta dada por el cociente de los coeficientes de grado mayor."
"Ejemplo: Hallar la asíntota horizontal de la función:")
st.latex(r"f(x) = \frac{6x - 5}{2x + 4}")
st.markdown("Solución: Se dividen los coeficientes de los términos de mayor exponente: 6/2 Así, el valor de la asíntota horizontal es: y = 3")
st.markdown("2. El grado del polinomio g(x) es menor que el de h(x) en estos casos, la asíntota horizontal es la recta y = 0"
"Ejemplo: Hallar la asíntota horizontal de la función:")
st.latex(r"f(x) = \frac{5x - 2}{x^2 - 2x - 8}")
st.markdown("Solución: Como el grado del polinomio del numerador es menor que el del denominador, el valor de la asíntota horizontal es: y = 0")
st.markdown("3. El grado del polinomio g(x) es mayor que el de h(x)."
"En estos casos no hay asíntota horizontal."
"Ejemplo: hallar la asinota horizontal de la función:")
st.latex(r"f(x) = \frac{4x - 12}{2}")
st.markdown("Solución: Como el grado del polinomio el numerador es mayor ue el del denominador, no existen asíntotas horizontales.")
st.image("https://www.funciones.xyz/wp-content/uploads/2021/04/asintota-horizontal-de-una-funcion.png")
# Graficar la función con la asíntota horizontal

x = np.linspace(-10, 10, 400)
x = x[x != 0]  # Evitar división por cero

def f(x):
    return 1 / x

plt.figure(figsize=(8, 6))
plt.plot(x, f(x), label=r'$f(x) = \frac{1}{x}$', color='blue')
plt.axhline(0, color='red', linestyle='--', label="Asíntota horizontal $y = 0$")

# Etiquetas y título del gráfico
plt.title("Gráfico de la función con asíntota horizontal")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.legend()

# Mostrar el gráfico
st.pyplot(plt)
st.subheader("ASINTOTA VERTICAL")
st.markdown("Son rectas verticales asociadas a la función. Se encuentran presentes únicamente en funciones racionales de la forma:")
st.latex(r"f(x) = \frac{g(x)}{h(x)}")
st.markdown("Y se determinan encontrando las raíces del denominador h(x)correspondiente. El número de raíces asociadas a una función determinan el número de asíntotas verticales que tiene tal función."
"Ejemplo: Hallar las asintotas verticales de la función: ")
st.latex(r" f(x) = \frac{1}{x^2 - 3x - 4}")
st.markdown("el polinomio del denominador es de grado dos: $x^2 - 3x - 4 = 0$, que tiene dos raices:")
st.latex(r"x^2 - 3x - 4 = 0 \rightarrow (x - 4)(x + 1) = 0 \rightarrow x - 4 = 0 , x + 1 = 0")
st.markdown("Así que los valores de ls asíntotas verticales son: $x = 4$ y $x = -1$")
st.subheader("CONCLUSIÓN")
st.markdown("Las asíntotas son rectas a las cuales la función se va aproximando indefinidamente, cuando por lo menos una de las variables (x o y) tienden al infinito. En una función racional, las asíntotas verticales se obtienen de las raíces del polinomio del denominador, mientras que las asíntotas horizontales dependen de la relación que exista entre los grados del polinomio del numerador y del polinomio del denominador.")
st.image("https://www.funciones.xyz/wp-content/uploads/2021/04/asintota-vertical.png")

# Graficar la función con la asíntota vertical
x = np.linspace(-10, 10, 400)
x = x[x != 0]  # Evitar división por cero

def f(x):
    return 1 / x

plt.figure(figsize=(8, 6))
plt.plot(x, f(x), label=r'$f(x) = \frac{1}{x}$', color='blue')
plt.axvline(0, color='red', linestyle='--', label="Asíntota vertical $x = 0$")

# Etiquetas y título del gráfico
plt.title("Gráfico de la función con asíntota vertical")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.legend()

# Mostrar el gráfico
st.pyplot(plt)

st.video("https://www.youtube.com/watch?v=VziE5Yu5RW8&pp=ygUzZXhwbGljYWNpb24gZGUgYXNpbnRvdGFzIHZlcnRpY2FsZXMgeSBob3Jpem9udGFsZXMg")
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Título de la aplicación
st.title("ASÍNTOTAS OBLICUAS")

# Sección de Introducción
st.header("¿Qué es una Asíntota Oblicua?")
st.markdown("""
Una **asíntota oblicua** o **asíntota inclinada** es una recta que la gráfica de una función racional 
se aproxima a medida que \( x \) tiende a (infinito) o ( -infinito ). Este tipo de asíntota ocurre cuando 
el grado del numerador de una función racional es uno mayor que el grado de su denominador. 

En términos más simples, las asíntotas oblicuas son rectas que no son horizontales ni verticales, 
pero que son una aproximación para la función cuando \( x \) es muy grande o muy pequeño. 
Estas rectas son particularmente importantes para funciones que no tienen límites finitos cuando 
\( x \) tiende a \( infinito\), pero que aún así se aproximan a una recta a medida que \( x \) crece.

### Características clave de las asíntotas oblicuas:
- Aparecen cuando el **grado del numerador es uno mayor** que el grado del denominador.
- Son rectas inclinadas, a diferencia de las asíntotas horizontales (que son paralelas al eje \( x \)) y las verticales (que son paralelas al eje \( y \)).
- Se pueden encontrar mediante **división polinómica** entre el numerador y el denominador, lo que produce el cociente que es la ecuación de la recta oblicua.

""")

# Fórmula de ejemplo
st.header("Ejemplo de una Función con Asíntota Oblicua")
st.markdown("""
Consideremos la siguiente función racional:""")

st.latex(r"""
f(x) = \frac{x^2 + 1}{x}""")

st.markdown("""En este caso, el **numerador** tiene grado 2 y el **denominador** tiene grado 1. 
Por lo tanto, el grado del numerador es uno mayor que el grado del denominador, lo que sugiere que la función tiene una asíntota oblicua.

Al dividir el numerador entre el denominador, obtenemos el cociente que representa la ecuación de la asíntota oblicua:""")

st.latex(r"""f(x) = x + \frac{1}{x}""")


st.markdown("""A medida que x tiende a infinito o -infinito, la función se aproxima a la recta:

$$
y = x
$$

Por lo tanto, la función tiene una asíntota oblicua en \( y = x \).
""")

# Graficar la función con la asíntota oblicua
st.header("Gráfico de la Función con Asíntota Oblicua")
x = np.linspace(-10, 10, 400)
y = (x**2 + 1) / x  # La función f(x) = (x^2 + 1) / x
asintota_oblicua = x  # La asíntota oblicua es y = x

plt.figure(figsize=(8, 6))
plt.plot(x, y, label=r'$f(x) = \frac{x^2 + 1}{x}$', color='blue')
plt.plot(x, asintota_oblicua, label=r'Asíntota oblicua $y = x$', color='red', linestyle='--')

# Etiquetas y título del gráfico
plt.title("Gráfico de la función con asíntota oblicua")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.legend()

# Mostrar el gráfico
st.pyplot(plt)

# Explicación sobre cómo calcular la asíntota oblicua
st.header("¿Cómo calcular una Asíntota Oblicua?")
st.markdown("""
Para encontrar la asíntota oblicua de una función racional:""")
st.latex(r"""  f(x) = \frac{P(x)}{Q(x)} """)
st.markdown(""" con **P(x)** y **Q(x)** como polinomios, 
debemos seguir estos pasos:

1. **División de polinomios**: Dividir el polinomio del numerador \( P(x) \) entre el polinomio del denominador \( Q(x) \). 
   La división produce un cociente de la forma \( y = mx + b \), donde \( m \) es la pendiente de la recta oblicua y \( b \) es la intersección en \( y \).

2. **Despreciar los términos de menor grado**: El cociente resultante de la división es la ecuación de la recta oblicua. El residuo de la división tiende a cero a medida que \( x tiende a infinito \), por lo que no afecta la asíntota oblicua.

### Ejemplo:
Tomemos la función:""")
st.latex(r""" f(x) = \frac{x^2 + 1}{x} """)

st.markdown("""1. Dividimos \( x^2 + 1 \) entre \( x \), lo que da como resultado:""")
st.latex(r"""
f(x) = x + \frac{1}{x}
""")
   
st.markdown("""2. La recta oblicua es \( y = x \), ya que el término:""")
st.latex(r""" \frac{1}{x} """)
st.markdown(""" tiende a cero a medida que ( x tiende a infinito).
   
Por lo tanto, la asíntota oblicua de esta función es la recta \( y = x \).
""")



# Video explicativo
st.header("Explicación en Video")
st.video("https://www.youtube.com/watch?v=cwldFcuQ8GY&pp=ygUqdmlkZW8gY29ydG8gZGUgcXVlIGVzIHVuYSBhc2ludG90YSBvYmxpY3Vh")

# Conclusión
st.header("Conclusión sobre las Asíntotas Oblicuas")
st.markdown("""
Las **asíntotas oblicuas** son una característica interesante de las funciones racionales, que ocurren cuando el grado del numerador es uno mayor que el grado del denominador. 
Al estudiar estas asíntotas, es importante comprender que se aproximan a una recta inclinada, y no a una horizontal ni vertical. 

Estas rectas son útiles para describir el comportamiento de las funciones a medida que \( x \) crece o decrece mucho, especialmente en casos donde las funciones no tienden a un valor constante. 

Las asíntotas oblicuas son fundamentales en el análisis de funciones racionales y se pueden determinar fácilmente mediante la división polinómica. 
¡Estudiarlas nos permite obtener una comprensión más profunda del comportamiento de las funciones en los límites!
""")





