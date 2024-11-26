import streamlit as st

st.title("Felipe Sánchez")
st.caption("soy estudiante de la carrera de matmáticas")

#titulos
st.title("titulo de nivel 1")
st.header("titulo nivel 2")
st.subheader("titulo nivel 3")


#textos
st.markdown("""
es una etiqueta tipo markdown pueden poner cualquier texto en el ormato markdown. Podemos poner el texto **negrilla**, en *itálca* o en ***ambos***

esto es otra linea

enumeraciones:
1. primer item
2. segundo item
3. tercer item

+ item 1
+ item 2
+ item 3

podemos darle olor al texto :red[rojo], :blue[azul], :green[verde], :rainbow[felipe sanchez] así...
""")

st.latex("a^2 + b^2 = c^2")

st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcROJgRfYcAXuTCAh_IBBZidEC38WlzEGDLYpQ&s")

st.video("https://www.youtube.com/watch?v=2UbdPiqAiHY&pp=ygUVdGVvcmVtYSBkZSBwaXRhZ29yYXMg")