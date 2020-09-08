def verNombre(direccion):
    '''
    Devuelve el nombre del archivo
    '''
    n = direccion.split('.png')
    n = n[0].split('\\')            
    return n[-1]

n = verNombre('la\\la\\pala.png')
letras = listar (n)
letras2 = list(letras)
print (letras2)