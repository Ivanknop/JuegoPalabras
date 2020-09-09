class Imagen():
    def __init__(self,imagen):
        self.imagen = imagen
        self.nombre = ''
        self.lista_letras=[]
        self.cant_letras = 0
        self.adivinadas=0
        self.correcto=False
    
    def setNombre(self,nom):
        '''
        Setea el nombre  
        '''
        n = nom.split('.png')
        n = n[0].split('\\')
        self.nombre = n[-1].upper()

    def getNombre(self):
        return self.nombre

    def setCantLetras(self):
        self.cant_letras= len(self.nombre)
    
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
            self.verCorrecto()
            ok = True
        return ok
    
    def getCantAdivinadas(self):
        return self.adivinadas
    
    def verCorrecto(self):
        if self.adivinadas >= self.cant_letras:
            self.correcto = True

    def getCorrecto (self):
        return self.correcto
    
    def resetCorrecto(self):
        self.adivinadas = 0
        self.correcto = False


