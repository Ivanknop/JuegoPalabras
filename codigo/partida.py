class Partida ():
    '''
    Este objeto es una partida de juego. Posee una imagen, nombre, cantidad de letras
    letras adivinadas y si se adivinó o no.
    '''
    def __init__(self,imagen):
        self.imagen = imagen
        self.nombre = ''
        self.lista_letras=[]
        self.cant_letras = 0
        self.adivinadas=0
        self.correcto=False
    
    def setNombre(self):
        '''
        Setea el nombre  
        '''
        n = self.nombre.split('.png')
        n = n[0].split('\\')
        self.nombre = n

    def getNombre(self):
        return self.nombre

    def setCantLetras(self):
        self.setCantLetras=len(self.lista_letras)+1
    
    def getCantLetras(self):
        return self.cant_letras
    
    def setListaLetras (self):
        self.lista_letras = list (self.nombre)
    
    def getListaLetras(self):
        return self.lista_letras
    
    def verAdivinadas(self,letra):
        ok = False
        if letra in self.lista_letras:
            self.adivinadas += 1
            verCorrecto()
            ok = True
        return ok
    
    def verCorrecto(self):
        if self.adivinadas == self.cant_letras:
            self.correcto = True

    def getCorrecto (self):
        return self.correcto
    
