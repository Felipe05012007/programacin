import streamlit as st

#1) crear las páginas 
txts = st.Page("paginas/textos.py", title= "Teoría", icon=":material/text_fields:")
eva = st.Page("paginas/Evaluación.py", title= "Evaluación", icon=":material/drag_indicator:")
ejs = st.Page("paginas/ejemplos.py", title= "ejemplos", icon=":material/swipe_left:")
graphs = st.Page("paginas/graficos.py", title= "graficos", icon=":material/arrow_selector_tool:")
Presentación = st.Page("paginas/Presentación.py", title= "Presentación", icon=":material/face:")
#2) crear la navegación
#pg = st.navigation([txts, imps, ejs])
pg = st.navigation({"Introducción": [Presentación], "Elementos": [txts, ejs , graphs], "aplicación": [eva]})
#3) ejecutar
pg.run()