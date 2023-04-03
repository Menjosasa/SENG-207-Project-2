import PySimpleGUI as sg
import pyttsx3 as pt

layout = [
    [sg.Input(key='TEXT'),sg.Button('Speak',key='SPEAK BUTTON')],
    [sg.Text('Select Voice Type'),sg.Radio('Male','GROUP 1' ,key= 'MALE VOICE'),sg.Radio('Female','GROUP 1',key='FEMALE VOICE')]
 ]

window = sg.Window('Text To Speech App', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'SPEAK BUTTON' and values['MALE VOICE'] == True :
       engine = pt.init()
       text= values['TEXT']
       voices = engine.getProperty('voices')       
       engine.setProperty('voice', voices[0].id)
       engine.say(text)
       engine.runAndWait()
    if event == 'SPEAK BUTTON' and values['FEMALE VOICE'] == True :
       engine = pt.init()
       text= values['TEXT']
       voices = engine.getProperty('voices')       
       engine.setProperty('voice', voices[1].id)
       engine.say(text)
       engine.runAndWait()
        
   
window.close()
