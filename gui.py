import functions
import PySimpleGUI as sg
import time

# theme
sg.theme("DarkBlue9")

# creating the input box and labels
date_time = sg.Text('', key='date_time')
label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="Enter a todo", key='todo')

# creating the buttons
add_button = sg.Button(image_source="add.png", image_size=(100,30), tooltip='Add a todo', key='Add')
edit_button = sg.Button("Edit")
complete_button = sg.Button(image_size=(100,100), image_source="complete.png", tooltip="Mark selected item as complete",
                            key="Complete")
exit_button = sg.Button("Exit")

# creating the to-do list widget
list_box = sg.Listbox(values=functions.get_todos(), key='items',
                      enable_events=True, size=(45, 10))

# creating and displaying the window
window = sg.Window('My To-Do App',
                   layout=[[date_time],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]], font=('Helvetica', 12))

# execution
while True:
    event, value = window.read(timeout=200)
    window['date_time'].update(time.strftime("%b %d, %Y %H:%M:%S"))
    print(1, event)
    print(2, value['items'])
    print(3, value['todo'])

    if event == 'Add':
        todos = functions.get_todos()
        new_todo = value['todo'] + "\n"
        todos.append(new_todo)
        functions.write_todos(todos)
        window['items'].update(values=todos)

    elif event == "Edit":
        try:
            existing_todo = value['items'][0]
            new_todo = value['todo']

            todos = functions.get_todos()
            index = todos.index(existing_todo)
            todos[index] = new_todo + '\n'
            functions.write_todos(todos)
            window['items'].update(values=todos)
            window['todo'].update(value='')
        except IndexError:
            sg.popup('You must select an item to edit', font=('Helvetica', 12))
            continue

    elif event == "Complete":
        try:
            selected_todo = value['items'][0]

            todos = functions.get_todos()
            todos.remove(selected_todo)
            functions.write_todos(todos)
            window['items'].update(values=todos)
            window['todo'].update(value='')
        except IndexError:
            sg.popup('You must select an item to complete', font=('Helvetica', 12))

    elif event == 'items':
        window['todo'].update(value=value['items'][0])

    elif event == 'Exit':
        break

    elif event == sg.WINDOW_CLOSED:
        break

window.close()
