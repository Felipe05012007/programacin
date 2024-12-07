
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
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

# Graficar la función con la asíntota oblicua
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