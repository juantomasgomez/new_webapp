import functions
import PySimpleGUI as sg

# creating the widgets
label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="Enter a todo", key='todo')
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key='items',
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")

# creating and displaying the window
window = sg.Window('My To-Do App',
                   layout=[[label], [input_box, add_button],
                           [list_box, edit_button]], font=('Helvetica', 12))

while True:
    event, value = window.read()
    print(1, event)
    print(2, value['items'])
    print(3, value['todo'])
    if event == "Add":
        todos = functions.get_todos()
        new_todo = value['todo'] + "\n"
        todos.append(new_todo)
        functions.write_todos(todos)
        window['items'].update(values=todos)

    elif event == "Edit":
        existing_todo = value['items'][0]
        new_todo = value['todo']

        todos = functions.get_todos()
        index = todos.index(existing_todo)
        todos[index] = new_todo + '\n'
        functions.write_todos(todos)
        window['items'].update(values=todos)
    elif event == 'items':
        window['todo'].update(value=value['items'][0])

    elif event == sg.WINDOW_CLOSED:
        break

window.close()