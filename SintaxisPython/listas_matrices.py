#******************listas en python*************
cursos = ["python", "django", "fask", "c", "c++", "c#", "java", "php"]
#si quiero el 2 elemento
curso = cursos[1]
print(curso)
# si coloco -a tendre el ultimo elemento estos negativos me sirven para recorrer a la inversa
curso = cursos[-1]
print(curso)
#********************sublitas*****************
#se puede generear sublistas a partir de estas
sub = cursos[0:3]
# se me imprimira una sublista con los elementos en las posiciones de la 0 a la 3
print(sub)
# si quiero partir desde el 0 pongo
sub=cursos[:4]
print(sub)
#python entendera que quiero desde el 0 al 4
#si quiero todos los valores a partir del indice 5 pongo
sub=cursos[5:]
print(sub)
#y entendera q quiero desde el 5 hasta el final
#si no ponemos indice de partida ni de final asumora que queremos la lista completa
sub=cursos[:]
print(sub)
# con las sublistas podemos obtener elementos mediante saltos
sub=cursos[1:7:2]
print(sub)
#le estoy diciendo quiero una lista desde el 1 hasta el 7 con saltos de dos en todos
sub=cursos[::-1]
print(sub)
# le estoy diciendo que nos de el inverso de la lista php estara en el indice 0

#**********************operaciones con listas estas tambien se aplican para cuando tienen string***************
#ordenamiento , se puede hacer con algoritmo booblesorft o quicksort
#la segunta es haciendo uso del metodo sort ahora lo veremos
#lista de enteros y flotantes
lista = [8.17,90,1,5,44,1.32]
#para ordenar
lista.sort()
print(lista)
#esto me ordena la lista de froma ascendente
lista.sort(reverse=True)
print(lista)
#si quiero tener el numero mas grande
#con la lista ya ordenada cogeria el primero
#si quiero el menor cogeria el primero ordenando descendente
#o podemos usar la funcion min y max
menor = min(lista)
print(menor)
#para el mayor
mayor = max(lista)
print(mayor)
# si queremos saber la longitud de la lista usamos elemento
longitud =len(lista)
print(longitud)
#*****#buscar elementos en la lista
resultado = 8 in lista
print(resultado)
#nos dara faso ya que no existe el 8 en la listas
resultado = 8.17 in lista
print(resultado)
#nos dara True a que enla lista si existe ese numero
#si quiero obtener el indice en el que se encuentra
indice=lista.index(8.17)
print(indice)
#index nos dara un entero q es el indice en este caso el 2
#si deseamos saber cuantas veces se repite un elemento en la lista usamos count
contador =lista.count(5)
print(contador)
#el metodo count tambien nos indicara si existe o no en la lista si no existe saldra 0
#*****************insertar un elemento en la lista *************
print("insertar un valor en una lista ya establecida")
valor=[1,2,3]
valor.insert(4,10) #el metodo insert inserta un valor en la posicion q le especifique
#recib dos parametros (la pisicion, el valor a insertar )
print(valor)
#otro ejemplo en la posicion 1 agrege el 5
valor.insert(1,5)
print(valor)
#format para recibir datos ingresados *****************************
n=int(input("De cuantos datos quiere su lista: "))
datos=[] #indico una lista vacia
for i in range(1,n):#que comiense en la pocicion 1 hasta el n (osea en realidad sera n-1)
    elementos = int(input("ingrese el lemento: ".format(i))) #format recibe datos pero en este caso no es necesario pero el ing puso asi q dejemosle
    #uso de append nos permite ingresar un valor al final de la lista
    #como lis lista esta vacia comensara ingresando en la posicion 0
    datos.append(elementos) #indico la lista.el_metodo(orgumentos en este caso los elementos)
print(datos)
#imprimir la lista por medio de un ciclo for **********************
for i in range(0,n-1): #que comiense en 0 pero como mi lista un valor menos toca restarle
    print("indice [",i,"] = ",datos[i])


#***********************  matrices ******************+++
#con las listas podremos crear matrices, las listas nos permiten cualquier valor incluso otras sublistas
#creamos las filas
fila_uno=[10,20]
fila_dos=[30,40]
#creamos la lista matriz que contendra las dos listas anteriores formando una matriz
matriz=[fila_uno,fila_dos]
#obtener o modificar elementos

primer_elemento =matriz[0][0]
print(primer_elemento)
#se imprime 10 que estara en la posision 0,0
# para crear las listas con n dimensiones  vasta con anidarlas
