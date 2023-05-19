import streamlit as st
import functions

st.title('My Todo App')
st.subheader('This is my to-do app')
st.write('This is the first web-app I have ever coded')

todos = functions.get_todos()

for i in todos:
    st.checkbox(i)

st.text_input(label="", placeholder="Add new todo")






