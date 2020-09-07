import PySimpleGUI as sg 
import os

def inicio(img):
    layout = [[sg.Image(filename=img)],
        [sg.Button(button_text='Jugar', button_color=('#FF0','#000'),size=(50, 2), font=('Impact', 20), key='jugar')],
        [sg.Button(border_width=0,button_text='Salir', button_color=('#FF0','#000'), size=(50, 2), font=('Impact', 20), key='salir')],
    ]
    return layout
ANCHO = 400
ALTO = 600
img = os.path.join ('titulo.png')
ventana = sg.Window('Palabreando', inicio(img), size = (ANCHO,ALTO),element_justification='center',no_titlebar=False)
ventana.Finalize()
while True:
        event, values = ventana.read()
        if (event in (None, 'salir')):
            break
        if (event == 'jugar'):
            print ('Jugando')
ventana.Close()       