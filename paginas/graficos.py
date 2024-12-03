import streamlit as st
import matplotlib.pyplot as plt
import	numpy as np
	
st.title("graficas:")

x = [0,1,3,4,5,7]
y = [2,3,3,1,2,5]

fig, ax = plt.subplots()

ax.plot(x,y)
ax.grid()
st.pyplot(fig)

st.divider()

x = np.lincspace(-no.pi, np.pi, 200)
y = np.sin()
fig, ax = plt.subplots()

ax.plot(x,y)
ax.grid()
st.pyplot(fig)

xin, xfin = st.slider("")

x = np.lincspace(-3, 3, 100)
y = x**2 - 5
fig, ax = plt.subplots()

ax.plot(x,y)
ax.grid()
st.pyplot(fig)