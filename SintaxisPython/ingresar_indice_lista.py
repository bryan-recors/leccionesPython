print("\ningreseo de elementos segun el indice de la lista \n")
#guardo mi enunciado en una variable
enunciado = """
enunciado:
hacer un programa que me permita
leer la posición y el dato
que deseo insertar en la lista\n
"""
#funcion para imprimir valores de la lista
def imprimirLista(lista):
    for i in range(len(lista)):
        print("indice [",i,"] = ",lista[i])
#funcion para sumar la lista
def sumarLista(lista):
    total=0
    for i in range(len(lista)):
        total = total+lista[i]
    return total
#validar que la entrada sea un numero entero
def ingresarEntero():
   while True:
       entrada = input()
       try:
           entrada = int(entrada)
           return entrada
       except:
           print ("La entrada es incorrecta debes ingresar un numero entero")

print(enunciado)
#pregunto el tamaño de la lista
print("De que tamaño quieres la lista")
tamanoLista = ingresarEntero()
#defino una lista vacia
datos = []
#ingreso de valores en la lista
for i in range(tamanoLista):
    print("ingresa el elemento",i+1)
    elementos = ingresarEntero()
    datos.append(elementos)
#imprimo valores de la lista llamando a la funcion imprimir lista
print("\nLos valores de la lista actual son: \n")
imprimirLista(datos)
#***********insertar un valor en la lista***************
print("\nEn que indice desear insertar un valor: ")
#recibo el indice en el que se quiere insertar
indice= ingresarEntero()
#reviso si esta disponible ya que no se puede insertar en un indice que no existe
valorDisponible = len(datos)
while indice > len(datos):
    print("\nEse indice no se encuetra disponible")
    print("utilice un valor entre 0 y {}".format(valorDisponible))
    indice= ingresarEntero()
#pido el valor a ingresar
print("Ingresa el valor entero que quieres insertar: ")
valor = ingresarEntero()
#inserto el valor en la lista mandandole el indice y el valor
datos.insert(indice,valor)
#imprimo la lista nuevamente
print("\nLos valores de la lista actual son: \n")
imprimirLista(datos)
#sumo los valores de la lista llamando a la funcion sumarLista
suma = sumarLista(datos)
print("\n La suma de la lista completa es: ",suma)
