import PySimpleGUI as sg
from zip_creator import make_archive

sg.theme('Black')

label1 = sg.Text('Select files to compress')
input1 = sg.Input()
# This is a button
file_select = sg.FilesBrowse('Select a file', key='selected_file')

label2 = sg.Text('Select destination folder')
input2 = sg.Input()
# This is a button
file_path = sg.FolderBrowse('Select a folder', key='selected_folder')

compress_button = sg.Button("Compress")
output_label = sg.Text(key='output_label')

window = sg.Window('File Compressor',
                   layout=[[label1, input1, file_select],
                           [label2, input2, file_path],
                           [compress_button, output_label]])

while True:
    event, values = window.read()
    files = values['selected_file'].split(";")
    folderpath = values['selected_folder']
    make_archive(files, folderpath)
    window['output_label'].update(value='Compression completed')

window.read()
window.close()