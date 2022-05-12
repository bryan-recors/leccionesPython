#definicion de una funcion con parametros
def crear_mensaje(nombre):
    mensaje = "hola {}, biembenido".format(nombre)
    return mensaje #retornando un valor
#llamado de una funcion
llamar_mensaje = crear_mensaje("bryan")#mandando a llamar a la funcion enviando un argumento
print(llamar_mensaje)

def obtener_curso():
    return "curso de Python", "basico", 3.6

curso, nivel, version = obtener_curso()
print(curso,nivel,version)

def crear_usuario (nombre, apellido,edad):
    return {
        'nombre': nombre,
        'apellido': apellido,
        'nombre_completo': "{}{}".format(nombre,apellido),
        'edad':edad
    }

usuario = crear_usuario("bryan", "sandoval", 26)
print(usuario)

"""
def suma(parametroFijo,*arg):
    total = 0
    for valor in arg:
        total+=valor
    total= parametroFijo+total
    return total

resultado= suma(100,10,20,30)
print(resultado)
"""
"""
#pasar un diccionario como parametros se puede pasan n
def usuarios_autenticados(**kwargs):
     print(kwargs)
usuarios_autenticados(codi= True, facilito=False)

"""
"""
#datos dispobibles en una tupla
def suma(numero1, numero2):
    suma = numero1+numero2
    return suma

datos=[100,20]
resultado =suma(*datos)
print(resultado)

"""
"""
def registro(importe, descuento):
     return importe -(importe *descuento / 100)

datos={"descuento":10, "importe":1500}
print(registro(**datos))
"""
""""
#llamada de retorno llamar una funcion dentro de otra
def funcion():
    return "Hola"

def saludar(nombre):
    saludo=funcion()
    print (saludo, nombre)

saludar("Bryan")
"""
"""
#retornar varios valores
def multiplicacion(num1, num2, num3,num4):
    resultado1=num1*num2
    resultado2=num3*num4
    return resultado1,resultado2

operacion1,operacion2=multiplicacion(3,4,5,6)
print("resultado de la operacion uno es: ",operacion1)
print("resultado de la operacion dos es: ",operacion2)
"""
def promedio(num1, num2):
    suma=num1+num2
    resultado=suma/2
    return resultado

oper=promedio(4,6)
print("el promedio es: ",oper)
#print(suma)


# funciones

def saluda():
    print("hola mundo")

#llamar la funciones
saluda()

"""
#funcion con datos de entrada
def crear_mensaje(nombre):
    mensaje = "hola {}, bienvenido al curso".format(nombre)
    return mensaje

nuevo_mensaje = crear_mensaje("eduardo")
print(nuevo_mensaje)

# dinfion de n parametros
def suma(*arg):
    total = 0
    for valor in arg:
        total+=valor
    return total
resultado= suma(10,20,30)
print(resultado)
"""

# con parametro requerido
def suma(parametro_requerido,*arg):
    total = 0
    print(parametro_requerido)
    for valor in arg:
        total+=valor
    return total
resultado= suma("este es un parametro", 10,20,30)
print(resultado)
 #otra forma de n parametros
 

def usuarios_autenticados(**kwargs):
     print(kwargs)

usuarios_autenticados("codi= True, facilito=False")

#variables globales y locales
animal = 'leon' # global

def mostrar_animal2():
    animal='ballenas' #local
    print(animal)

def mostrar_animal():
    global animal #convertir variable a global para poderla modificar
    animal='ballenas'
    print(animal)

mostrar_animal()
print(animal)
#funcion lambda
mi_funcion = lambda grados=0: grados * 1.8 +32  
#ejecutar
resultado = mi_funcion(32)
print(resultado)

def cuadrado(numero):
    return numero*numero

#funcion map
lista =[1,2,3,4,5]
resultado = map(cuadrado,lista) #funcion map
#convertir resultado objeto map a lista
lista_resultado = list(resultado)
print(lista_resultado)

#anidacion de funnciones
def comenzar_play_list(lista):
    def reproducir():
        nonlocal lista
        lista = [1,2,3]
        for val in lista:
            print(val)

    reproducir() #recien se llama a la funcion
    print(lista)

lista = ['track 1', 'track2 ', 'track3',  'track 4']
comenzar_play_list(lista) 
print(lista)

#clousures
#esta funcion sera un clousur 
# llamaremos asi cuando una funcion genere dinamicamente otra funcion
def mostrar_mensaje(mensaje):
    mensaje = mensaje.title()

    def mostrar():
        print(mensaje)
    
    return mostrar
nueva_funcion = mostrar_mensaje("bryan alejandro")
nueva_funcion()

#crear un decorador
#funcion a
def decorador(funcion):
    #funcion C
    def nueva_funcion(): 
        print("Podemos agregar codigo antes") #funciones extra antes
        funcion() 
        print("agregar codigo despues de la funcion") #funciones extra despues
    return nueva_funcion #retorno funcion c

#funcion b
@decorador #decorar la funcion
def funcion_a_decorar():
    print("este es una funcion a decorar")

#ejecutar la funcion
funcion_a_decorar()

#decorar una funcoin con n cantidad de parametros
def decorador(funcion):
    #funcion C
    def nueva_funcion(*args, **kwargs): 
        print("Podemos agregar codigo antes") #funciones extra antes
        resultado = funcion(*args,**kwargs) 
        print("agregar codigo despues de la funcion") #funciones extra despues
        return resultado
    return nueva_funcion #retorno funcion c

#funcion b
@decorador
def suma(val1,val2):
    return val1+val2

resultado = suma(10,20)
print(resultado)

#generadores
def tabla_multiplicar(numero, maximo=10):
    for posicion in range(1,maximo+1):
        #retorne un valor sin finalizar la funcion
        yield numero * posicion, numero, posicion

for resultado,numero,posicion  in tabla_multiplicar(9):
    print(numero,"*", posicion, "=", resultado)

#documentar y aprovechar la documentacion de una funcion 
def suma (a,b):
    #asi se documenta la funcion
    """Función suma""" 
    return a+b

def resta (a,b):
    #asi se documenta la funcion
    """Función resta"""
    return a-b

opciones = {'a':suma,'b':resta} #diccionario
print("ingrese la opcion deseada")

for opcion, funcion in opciones.items():
    #funcion.__doc__ #permite ver la documentacion de la funcion
    mensaje = '{}) {}'.format(opcion,funcion.__doc__)
    print(mensaje)

opcion = input("opción:")
if opcion == 'a':
    resultado = suma(3,5)
    print("3+5 es ",resultado)
elif opcion =='b':
    resultado = resta(3,5)
    print("3-5 es ",resultado)
else:
    print("opcion incorrecta")

#implementacion de anotations en python
def saludo(nombre:str) -> None:
    print("hola"+nombre)

nombre = "Eduardo"
saludo(nombre)

def suma (num1:int, num2 : int = 100) -> int:
    return num1+num2

print(suma(2.5,2.5))

