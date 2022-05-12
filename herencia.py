#clas padre
class Operaciones:
    def __init__(self, elemento1, elemento2):
        self.elemento1= elemento1
        self.elemento2= elemento2

#clase hija
class opBasicas(Operaciones):
    def suma(self):
        s=self.elemento1 + self.elemento2
        print("la suma es: ",s)
        
#clase hija
class exponente(Operaciones):
    def potencia(self):
        import math
        d=math.pow(self.elemento1,self.elemento2)
        print("el resultado es: ",d)

#instanciar un objetos
generar=opBasicas(2,3)
generar.suma()
generar=exponente(2,3)
generar.potencia()
