import PySimpleGUI as sg 
import os
import codigo.visorImagenes as vImg
from codigo.imagen import*


def armar_botones(palabra):  
    botones=[]
    for i in range(len(palabra)):
        botones.append(sg.Button(button_text=palabra[i].upper(),size=(2,2),button_color=('black','#0e2'),key=str(i),visible=True))
    return botones


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

def ocultarBotones (ventana,nom):
    for i in range(len(nom)):
        ventana[str(i)].Update(visible=False)

def actualizar_botones(ventana,nom):    
    ventana['nombre'].Update(nom)
    for i in range(len(nom)):           
        ventana[str(i)].Update(nom[i],visible=True)
        print (i)

def inicio(img):
    layout = [[sg.Image(filename=img)],
        [sg.Button(button_text='Jugar', button_color=('#FF0','#000'),size=(50, 2), font=('Impact', 20), key='jugar')],
        [sg.Button(border_width=0,button_text='Salir', button_color=('#FF0','#000'), size=(50, 2), font=('Impact', 20), key='salir')],
    ]
    return layout

def jugar_interfaz(imagenes):
    imagen = Imagen (imagenes.getActualRuta())
    nom = imagenes.getActualRuta()
    imagen.setNombre(nom)
    imagen.setListaLetras()
    botones = armar_botones(imagen.getNombre())
    layout = [
         [sg.Column(imagenes.getAvatarLayout(),visible=False,element_justification='center',key='colAvatar')],
         [sg.Text('',key='letra')],
         botones,
         [sg.Button('Nombre',key='nombre')],
        [sg.Button(border_width=0,button_text='VOLVER', button_color=('#FF0','#000'), size=(50, 2), font=('Impact', 20), key='volver')],
    ]
    return layout

def interfaz_principal(titulo,imagenes):
    colInicial = inicio(titulo)
    layout = [
        [sg.Column(colInicial,justification='center',element_justification='center',key= 'colInicial'),
         sg.Column(jugar_interfaz(imagenes),visible=False,justification='center',element_justification='center',key='colJugar'),
        ]
    ]
    return layout

def actualizarImagen(imagenes):
    unaImagen = Imagen (imagenes)
    unaImagen.setNombre(imagenes)
    unaImagen.setListaLetras()
    unaImagen.setCantLetras()
    if unaImagen.getCorrecto()== True:
        print ('Listo')
        unaImagen.resetCorrecto()
    else:
        print('falta')
    return unaImagen

def juego():
    ANCHO = 400
    ALTO = 600
    titulo = os.path.join ('media','titulo.png')
    dirImagenes = os.path.join('media','imagenes','')
    imagenes = vImg.Visor(dirImagenes)
    imagenPrevia = imagenes.getActualRuta()
    img = actualizarImagen (imagenPrevia)
    nomPrevio = img.getNombre()
    ventana = sg.Window('Palabreando', interfaz_principal(titulo,imagenes), size = (ANCHO,ALTO),background_color='#DDD' ,element_justification='center',return_keyboard_events=True)
    ventana.Finalize()
    while True:
        event, values = ventana.read()
        if (event in (None, 'salir')):
            break
        if (event == 'jugar'):
            actualizar_columnas(ventana, 'colJugar','colAvatar')
        if (event == 'volver'):
            actualizar_columnas(ventana,'colInicial')
        elif event == 'nombre':
            #permite cambiar las imagenes a usar,Todavia falta que los botones esten en una sola fila
            selector_imagenes = imagenes.controles('>>>', ventana.FindElement('avatarVisor'))
            img = actualizarImagen(selector_imagenes)
            ocultarBotones(ventana,nomPrevio)
            actualizar_botones(ventana,img.getNombre().upper())
        letras = [chr(i) for i in range(ord('a'),ord('z')+1)]
        if event in letras:
            print (event)
            print ('Letra:',img.verAdivinadas(event.upper()))
            print ('Palabra adivinada: ',img.getCorrecto())
                
            #falta relacionarlo con las letras en juego
    ventana.Close()       