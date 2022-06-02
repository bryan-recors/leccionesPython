"""primera forma de trabajar con los modulos"""
"""
#usando funciones de otro archivo
import calculadora

#usaremos la funcon suma del modulo calculadora
resultado = calculadora.suma(10,20)
print(resultado)

"""
"""segunda forma de trabajar con los modulos"""
# si importamos asi ya no debemos especificar a que modulo pertenece la funcion
#from calculadora import * 
#resultado = suma(10,20)
#print(resultado)

"""tercera forma de trabajar con los modulos"""
"""
# si ya sabemos puntualmente lo que queremos del modulo indicamos en vex del *
from calculadora import (
    suma,
    resta,
    multiplicacion
)

resultado = suma(10,20)
print(resultado)

resultado2 = resta(20,10)
print(resultado2)

resultado3 = multiplicacion(20,10)
print(resultado3)
"""

"""cuarta forma de trabajar con los modulos"""
# podemos renombrar a funciones o objetos que nesetitamos
#from calculadora import suma as nueva_suma

#resultado = nueva_suma(10,20)
#print(resultado)

"""comportamiento de __name__"""
"""
import calculadora 
print(calculadora.__name__)
print(__name__)
"""

"""paquetes"""
"""
from animales.aves import Pinguino

pinguino = Pinguino()
pinguino.nadar()
"""
from animales import Pinguino, mi_jaguar, mi_funcion

pinguino = Pinguino()
pinguino.nadar()

mi_jaguar.cazar()
mi_funcion()