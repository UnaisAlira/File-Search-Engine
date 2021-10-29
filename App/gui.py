#We are using PySimpleGUI for user interface
import PySimpleGUI as sg
class Gui:
    def __init__(self) :
        self.layout=[[sg.Text('search term'),
        sg.Input(key='term'),
        sg.Radio('Contains',group_id='choice',key='contains'),sg.Radio('Beginswith',group_id='choice',key='beginswith'),sg.Radio('Endswith',group_id='choice',key='endswith'),sg.Radio('File',group_id='choice',key='file')],
        [sg.Text('Root path'),
        sg.Input(key='path',default_text='C://'),
        sg.FolderBrowse('Browse'),
        sg.Button('Re-Index'),
        sg.Button('search',bind_return_key=True,key='search')],
        [sg.Output(size=(100,30))]]
        self.window=sg.Window('file search engine').Layout(self.layout)


