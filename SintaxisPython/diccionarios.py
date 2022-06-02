"""
Los diccionario al igual que las listas y las tuplas
nos permiten amacenar diferentes tipos de datos
String enteros flotantes boleanos
tuplas listas e inclusive otros diccionarios
Los diccionario son mutables esdecir podemos modificar
su longitud podemos agregar o quitar elementos de el
al igual que los valores que contienen pueden ser modificados
a diferencia que las listas y las tuplas los diccionarios no se riguen
a las reglas de los indices, los valores que se almacenan dentro del diccionario
no correconde a un indice sino a una llave, todos los valores necesitan tener una llave
y cada llave necesita tener un valor.
una llave puede ser cualquier tipo, cualquier tipo inmutable en python
ya sea un string un flotante un entero una tupla etc
para definir un diccionario uso
diccionario ={}
o la funcion dict
diccionario = dict()
ambas me permiten declarar un diccionario
Para almacenar un valor seguimos la siguinte estructura
la llave : y el valor que queremos azociar
ejemplo
diccionario = {"total":55}
diccionario2 ={"total":55, "descuento":True, "subtotal":15}
#si queremos agegar mas valores los separamos con una,
#otro ejemplo
diccionario3={"total":55, 10: "curso de python",(1,2,3): True}
total es un strig es la llave del primer elemento
10 es un entero es la lalve del segundo elemento
(1,2,3) es una tupla es la llave del tercer elemento
todas las llaves son tipos de datos inmutables.
regularmente se hace uso de una llave conmunmente de un mismo tipo conmunmente String
por si se quiere otro tipo de llave si se puede hacerlo
podemos utilizar clases como llaves
usuario= {
    'nombre': 'nombre del usuario',
    'edad': 23,
    'curso':'curso de python',
    'skills':{
        'programacion':True,
        'base_de_datos':False
        },
    'medallas':['basico','intermedio']
}
para poder agegar obtener o modificar algun valor dentro
del diccionario se usa []
#creacion del diccionario
diccionario = dict()
#agregar nueva llave valor
diccionario['usuario']='eduardo_gpg'
#obtener valor mediante una llave
print(diccionario['usuario'])
#podemos obtener todas las llaves de nuestro diccionario
usando el metodo keys
>>> diccionario ={'Eduardo':1, 'fernando':2, 'uriel':3, 'rafael':4}
>>> diccionario.keys() #podemos obtener todas las llaves del diccionario
dict_keys(['Eduardo','fernando', 'uriel', 'rafael'])

>>> diccionario.values() #podemos obtener todos los valores del diccionario
dict_values([1,2,3,4])
>>> for key, value un diccionario.items(): #recorrer llaver y valores
    print(key,value)

#resultado
Eduardo 1
Fernando 2
Uriel 3
Rafael 4

metodo get nos permite obtener el valor de un diccionario respecto a una llave
si la llave no existe.
si intento acceder a un metodo cuya llave no existe obtendremos error
key error,
con el metodo get podremos obtener un valor por default si la llave no existe
evitamos asi el error
ejemplo:
si intento ingresar  a las calificaciones de un usuario enparticular
este usuaro no posee la llave calificaciones asi que mandamos una lista vacia
para evitar el error si la lista esta vacia no recorremos e imprimimos los valores
usuario={
    'name':'eduardo ismarl',
    'age':26,
    'job':'codigo facilito'
}
calificaciones=usuario.get('calificaciones',[])
if calificaciones:

    for calificaciones in calificacines:
        print(calificacion)

al igual que con las listas es posible implementar el comparjeshion utilizando diccionarios

usuarios=['eduardo','fernando','uriel','rafael']
diccionario={usuario:position+1}
    for position, usuario in enumerate(usuarios)
print(diccionario)
"""
#obtener elelmento del diccionario con get
diccionario = {"a":1, "b":2, "c":3, "a":4}
resultado = diccionario.get("Z","no se encontro esa llave")
print(resultado)
 #metodo setdefault
diccionario = {"a":1, "b":2, "c":3, "a":4}
#si no existe la llave creara la llave z y su valor sera un diccionario vacio
resultado = diccionario.setdefault("Z", {}) 
print(resultado)
#imprimo como queda el diccionario
print (diccionario)