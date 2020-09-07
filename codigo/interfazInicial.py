import PySimpleGUI as sg 
import os
import codigo.visorImagenes as vImg

def actualizar_columnas(ventana, *columna):
    '''Vuelve visible la columna que recibe como parámetro e invisible
    el resto de las columnas. Se utiliza para actualizar la interfaz principal
    según la opción elegida'''
    #Busca en la lista de elementos hasta encontrar una columna
    for e in ventana.element_list():
        if e.Type == 'column':
            #Si la columna está invisible y tiene la key que busco, la hace visible
            if e.Visible == False and e.Key in columna:
                ventana.FindElement(e.Key).update(visible=True)
            elif e.Key in columna:
                ventana.FindElement(e.Key).update(visible=True)
            #Si no, la oculta
            else:
                ventana.FindElement(e.Key).update(visible=False)

def inicio(img):
    layout = [[sg.Image(filename=img)],
        [sg.Button(button_text='Jugar', button_color=('#FF0','#000'),size=(50, 2), font=('Impact', 20), key='jugar')],
        [sg.Button(border_width=0,button_text='Salir', button_color=('#FF0','#000'), size=(50, 2), font=('Impact', 20), key='salir')],
    ]
    return layout

def jugar_interfaz(imagenes):
    layout = [
         [sg.Column(imagenes.getAvatarLayout(),visible=False,key='colAvatar')],
        [sg.Button(border_width=0,button_text='VOLVER', button_color=('#FF0','#000'), size=(50, 2), font=('Impact', 20), key='volver')],
    ]
    return layout

def interfaz_principal(titulo, img_juego,imagenes):
    colInicial = inicio(titulo)
    layout = [
        [sg.Column(colInicial,justification='center',element_justification='center',key= 'colInicial'),

         sg.Column(jugar_interfaz(imagenes),visible=False,justification='center',element_justification='center',key='colJugar'),
        ]
    ]
    return layout

def juego():
    ANCHO = 400
    ALTO = 600
    titulo = os.path.join ('media','titulo.png')
    img_juego = os.path.join('media','imagenes','leon.png')
    directorio = os.path.join('media','imagenes','')
    imagenes = vImg.Visor(directorio)
    ventana = sg.Window('Palabreando', interfaz_principal(titulo,img_juego,imagenes), size = (ANCHO,ALTO),background_color='#DDD' ,element_justification='center',no_titlebar=False)
    ventana.Finalize()
    while True:
        event, values = ventana.read()
        if (event in (None, 'salir')):
            break
        if (event == 'jugar'):
            actualizar_columnas(ventana, 'colJugar','colAvatar')
        if (event == 'volver'):
            actualizar_columnas(ventana,'colInicial')
        elif event in ('<<<', '>>>'):
            avatarSelec = imagenes.controles(event, ventana.FindElement('avatarVisor'))
    ventana.Close()       