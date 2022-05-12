#********tuplas*********
"""
las tuplas son muy parecidas a las listas nos permiten almacenar
almacenar diferentes tipos de datos string esteros flotantes e  otras tuplas
la diferencia con las listas s que las tuplas son inmutables
no podemos modificar los elementos que almacenan
no se puede agregar o quitar elementos una ves definida la tupla esta se quedara
asi el resto del programa
ejplo: si definimos una tupla que almacene 10 num + estos estaran presente en
todo el programa y solo los podemos consultar.
como se crea ??
tupla =()
para que almacenen diferentes tipos de datos los colocamos dentro de los parentesis
y separarlos mediante una ,
mi_tupla =('Eduardo',2,4.5, True)
la ventaja de usar tuplas n ves de lista es que son mucho mas rapidas en cuanto a
obtener elementos.
con las tuplas tambien se puede usar los indices
"""
tupla=(1,2,3,4,5,6,7,8,9,0)
#obtener un elemento con el indice
elemento=tupla[4]
print(elemento)
#podemos trabajar con negativos
elemento=tupla[-1]
print(elemento)
#podemos generar subtuplas al igual q las listas
sub_tupla=tupla[0:5:2]
print(sub_tupla)
sub_tupla=tupla[:9:2]
print(sub_tupla)
#si quiero modificar no se puede porq son inmutables
#n cantidad de variables en una linea
print("tupla2")
tupla2=(1,2,3,4)
uno, dos, tres, cuatro = tupla2[0], tupla2[1], tupla2[2], tupla2[3]
print(uno)
print(dos)
print(tres)
print(cuatro)
#se imprime gracias a q uso el indice de la tupla para asignar a cada valor
#simploficado
print("tupla3")
tupla3=(1,2,3,4)
unos, doss, tress, cuatros = tupla3
print(unos)
print(doss)
print(tress)
print(cuatros)
#obtendremos la misma salida a cada variable
#si tengo una tupla con 6 elementos y declaro solo 4 variables
#me saldra error lo q se puede hacer es almacenar los ultimos como una lista
#asi
print("tupla4")
tupla4=(1,2,3,4,8,9)
unoss, dosss, tresss, *cuatross = tupla4
print(unoss)
print(dosss)
print(tresss)
print(cuatross)
#la variable cuatross es ahora una lista con los elelentos  que no pudieron ser asignados a una variables
#el uso del * se puede colocar en cualquier variables python sabra asignar los valores a las variables

#******generar nuevas tuplas a partir de listas o de tuplas
print("tupla5")
tupla5=(1 ,2 ,3 ,4 ,5 ,6)
#genero una listas
lista =[10,20,30,10]
#genero una nueva tupla a traves de zip
resultado = zip(tupla5, lista)
#la funcion zip nos regresa un objeto del tipo zip
print(resultado)
#nos botara un objeto
#debemos convertir el objeto a una tupla
resultado =tuple(resultado)
print(resultado)
#esta tupla contienen los elementos de la lista y de la tupla
#sino quiero trabajarle como tupla la convierto en lista en ves de tupla
#list(resultado)
#la funcion zip puede recibir n cantidad de listas, ncantidad de tuplas, ncantidad de listas y tuplas
#añadire una nueva tupla
tupla_dos=(100,200,300,400)
resultado2 =zip(tupla5,lista,tupla_dos)
resultado2 =list(resultado2)
print(resultado2)

#*******desempaquetado de tuplas*****
print("tupla 6")
tupla6 =(10,20,30,40,50)
 #necesitamos obtener el primero, segundo y ultimo
 #usando indices podemos hacerlo
primero1 =tupla6[0]
segundo1=tupla6[1]
ultimo1=tupla6[-1]
 #o podemos dejarlo enuna sola linea
 #primero1, segundo1, ultimo1 =tupla6[0], tupla6[1] tupla6[-1]
 #la segunda opcion es dejar de trabajar con los indices
 #y utilizar el guion bajo
 #primero1, segundo1, _, _, ultimo =tupla
 #los guiones bajos hacen referencia a los elelentos q estan enla tupla
 #pero solo son ignorados
 #puedo usar tambien *_para ognorar el esto de la tupla
print("de listas a tuplas y viceversa")
#convertir de una lista a una tupla y viceversa
lista7 =["Curso", "Python","CodigoFacilito"]
tupla7=("Introduccion", "basico", "listas", "tuplas")
print("esta es una lista",lista7)
print("esta es una tupla",tupla7)
#de tupla a lista
nueva_lista = list(tupla7)
print("ahora la tupla es una lista",nueva_lista)
#de lista a tupla
nueva_tupla = tuple(lista7)
print("ahora la lista es una tupla", nueva_tupla)
#los string tambien pueden ser trandformados a listas o tupla_dos
mensaje = "este es el curso de python"
nueva_listaString = list(mensaje)
print("ahora el string es una lista",nueva_listaString)
nueva_tuplaString = tuple(mensaje)
print("ahora el string es una tupla", nueva_tuplaString)
