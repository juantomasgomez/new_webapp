import PySimpleGUI as sg
from fi_functions import get_result

label1 = sg.Text("Enter feet: ")
input1 = sg.Input(key='feet')

label2 = sg.Text("Enter inches: ")
input2 = sg.Input(key='inches')

convert_button = sg.Button("Convert")

output_label = sg.Text(key='output_label')

window = sg.Window("Convertor", layout=[[label1, input1],
                                        [label2, input2],
                                        [convert_button, output_label]])

while True:
    event, values = window.read()
    feet = float(values['feet'])
    inches = float(values['inches'])
    result = get_result(feet, inches).__round__(2)
    output_message = f'{result} m'
    window['output_label'].update(value=output_message)

window.close()
