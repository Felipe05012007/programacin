import  streamlit as st

st.title("Página de inputs")

st.slider("")

nombre = st.text_input("Digite su nombre:")
st.markdown(f"el nombre que ingresó es: {nombre}")

edad = st.number_input("digite su edad:", min_value=0, max_value=120)
st.markdown(f"la edad que ingresó es: {edad}")
if edad>18:
    st.markdown("eres mayor de edad")
else:
    st.markdown("eres menor de edad")


rango = st.slider("digite un valor:", min_value=0, max_value=10)
st.markdown(f"el valor que ingresó es: {rango}")

ini, final = st.slider("Seleccione rangos:", min_value=0, max_value=10, value=(2,5))
st.markdown(f"el valor inicial es: {ini} y el valor final es: {final}")




#selección 
x = st.number_input("x:")
y = st.number_input("y:")

opc = st.selectbox("operación:", options=["sumar", "restar", "multiplicar", "dividir"])

if opc == "sumar":
    st.markdown(f"la suma es: {x+y}")
elif opc == "restar":
    st.markdown(f"la resta es: {x-y}")
elif opc == "multiplicar":
    st.markdown(f"la multiplicación es: {x*y}")
elif opc == "dividir":
    st.markdown(f"la división es: {x/y}")