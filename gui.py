import functions
import PySimpleGUI as sg

# creating the input box and label
label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="Enter a todo", key='todo')

# creating the buttons
add_button = sg.Button("Add")
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

# creating the to-do list widget
list_box = sg.Listbox(values=functions.get_todos(), key='items',
                      enable_events=True, size=[45, 10])

# creating and displaying the window
window = sg.Window('My To-Do App',
                   layout=[[label], [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]], font=('Helvetica', 12))

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
        window['todo'].update(value='')

    elif event == "Complete":
        selected_todo = value['items'][0]

        todos = functions.get_todos()
        todos.remove(selected_todo)
        functions.write_todos(todos)
        window['items'].update(values=todos)
        window['todo'].update(value='')

    elif event == 'items':
        window['todo'].update(value=value['items'][0])

    elif event == 'Exit':
        exit()

    elif event == sg.WINDOW_CLOSED:
        break

window.close()