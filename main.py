import streamlit as st

#1) crear las páginas 
txts = st.Page("paginas/textos.py", title= "textos", icon=":material/text_fields:")
inps = st.Page("paginas/inputs.py", title= "inputs", icon=":material/drag_indicator:")
ejs = st.Page("paginas/ejemplos.py", title= "ejemplos", icon=":material/swipe_left:")
graphs = st.Page("paginas/graficos.py", title= "graficos", icon=":material/arrow_selector_tool:")
#2) crear la navegación
#pg = st.navigation([txts, imps, ejs])
pg = st.navigation({"Elementos": [txts, inps], "aplicación": [ejs,graphs]})
#3) ejecutar
pg.run()