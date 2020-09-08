import PySimpleGUI as sg 
import os
import codigo.visorImagenes as vImg
from codigo.imagen import*


def armar_letras(palabra):
    botones=[]
    for i in range (len(palabra)):
        botones.append(sg.Button(button_text=palabra[i].upper(),size=(2,2),button_color=('black','#0e2'),key=i))
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

def actualizar_botones(imagen):
    for l in imagen.getLetras():
        print (l)
    ventana[i].update(value='{}').format(imagen.getLetras(
        
    ))

def inicio(img):
    layout = [[sg.Image(filename=img)],
        [sg.Button(button_text='Jugar', button_color=('#FF0','#000'),size=(50, 2), font=('Impact', 20), key='jugar')],
        [sg.Button(border_width=0,button_text='Salir', button_color=('#FF0','#000'), size=(50, 2), font=('Impact', 20), key='salir')],
    ]
    return layout

def jugar_interfaz(imagenes):
    #botones = armar_letras(verNombre(imagenes.getActualRuta()))
    imagen = Imagen (imagenes.getActualRuta())
    #botones = armar_letras(imagen.getLetras())
    #print(imagen.getLetras())
    #actualizar_botones(imagen)
    layout = [
         [sg.Column(imagenes.getAvatarLayout(),visible=False,element_justification='center',key='colAvatar')],
         [sg.Text('',key='letra')],
         #botones,
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
    print (unaImagen.getNombre(),' - ', unaImagen.getListaLetras(), ' - ',unaImagen.getCantLetras())
    print (unaImagen.verAdivinadas('a'))
    print (unaImagen.getCantAdivinadas())
    if unaImagen.getCorrecto()== True:
        print ('Listo')
        unaImagen.resetCorrecto()
    else:
        print('falta')

def juego():
    ANCHO = 400
    ALTO = 600
    titulo = os.path.join ('media','titulo.png')
    directorio = os.path.join('media','imagenes','')
    imagenes = vImg.Visor(directorio)    
    ventana = sg.Window('Palabreando', interfaz_principal(titulo,imagenes), size = (ANCHO,ALTO),background_color='#DDD' ,element_justification='center',no_titlebar=False)
    ventana.Finalize()
    while True:
        event, values = ventana.read()
        if (event in (None, 'salir')):
            break
        if (event == 'jugar'):
            actualizar_columnas(ventana, 'colJugar','colAvatar')
        if (event == 'volver'):
            actualizar_columnas(ventana,'colInicial')
        elif event in ('nombre'):
            selector_imagenes = imagenes.controles('>>>', ventana.FindElement('avatarVisor'))
            actualizarImagen(selector_imagenes)
            
    ventana.Close()       