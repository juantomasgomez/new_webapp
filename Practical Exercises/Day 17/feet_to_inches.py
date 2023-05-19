import PySimpleGUI as sg
from fi_functions import get_result

sg.theme('Black')

label1 = sg.Text("Enter feet: ")
input1 = sg.Input(key='feet')

label2 = sg.Text("Enter inches: ")
input2 = sg.Input(key='inches')

convert_button = sg.Button("Convert")
exit_button = sg.Button("Exit")

output_label = sg.Text(key='output_label')

window = sg.Window("Convertor", layout=[[label1, input1],
                                        [label2, input2],
                                        [convert_button, exit_button, output_label]])

while True:
    event, values = window.read()
    try:
        if event == 'Convert':
            feet = float(values['feet'])
            inches = float(values['inches'])
            result = get_result(feet, inches).__round__(2)
            output_message = f'{result} m'
            window['output_label'].update(value=output_message)
        elif event == 'Exit':
            break
        elif event == sg.WIN_CLOSED:
            break
    except ValueError:
        sg.popup('Please provide two numbers')
        continue

window.close()
