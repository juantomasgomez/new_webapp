import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    new_todo = st.session_state["new_todo"] + '\n'
    todos.append(new_todo)
    functions.write_todos(todos)


st.title('My Todo App')
st.subheader('This is my to-do app')
st.write('This is the first web-app I have ever coded')


for i in todos:
    st.checkbox(i)

st.text_input(label="", placeholder="Add new todo",
              on_change=add_todo, key='new_todo')

st.session_state




