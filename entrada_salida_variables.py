#comentario en lineal
"""
comentario en parrafo
"""
print("hola mundo")
"""
#variables y constantes
#variables
nombre_tutor ="codi"
print(nombre_tutor)
#las constantes no se peuden definir en python por lo que se puede poner asi para que no la cambien
CONSTANTE = "SOY UNA CONSTANTE"
print(CONSTANTE)
#variables en diferentes lineas
valor_uno=10
valor_dos="codi"
valor_tres=10*20
print(valor_uno)
print(valor_dos)
print(valor_tres)
#para poner en un asola linea
valor_uno, valor_dos, valor_tres =10,"codi",10*20
print(valor_uno)
print(valor_dos)
print(valor_tres)
"""
"""
#operadores relacionales y operadores logicos
variable_uno = 10
variable_dos = 18
mayor= variable_uno > variable_dos
menor = variable_uno < variable_dos
mayor_igual= variable_uno >= variable_dos
menor_igual = variable_uno <= variable_dos
igual = variable_uno == variable_dos
diferente = variable_uno != variable_dos
print(mayor)
print(menor)
print(mayor_igual)
print(menor_igual)
print(igual)
print(diferente)
#esto nos arroja valores booleanos
#operadores logicos son 3 And Or y not salida booleana
#and comparaciones verdades = verdadero
resultado = True and True and diferente
resultado = True or mayor
resultado = not False
#comparar si dos valores enteros son iguales usamos is
igual = variable_uno is variable_dos
print(igual)
"""
"""
#entradad de datos por teclado
print ("cual es tu nombre ")
nombre = input ()
print ("cual es tu edad ")
# si nesesitamos trabajar con enteros transformamos
edad = int (input())
print ("cual es tu peso ")
# si nesesitamos trabajar con flotantes lo transformamos
peso = float(input())
print ("estas autorizado(si/no)")
# si nesesitamos trabajar con booleano  usamos operadores relacional
autorizado = input()=="si"
print("hola", nombre)
print("edad", edad)
print("peso", peso)
print("Autorizado", autorizado)
"""
"""
#si quiero reducir las lienas de codifo copie el texto dentro de los ()
nombre = input ("cual es tu nombre \n")
edad = int (input("cual es tu edad \n"))
peso = float(input("cual es tu peso \n"))
autorizado = input("estas autorizado(si/no) \n")=="si"
print("hola", nombre)
print("edad", edad)
print("peso", peso)
print("Autorizado", autorizado)
"""
# la base y altura ingresados por el usuario calcular y mostrar en pantalla el area de triangulo
base = int (input("ingresa la base \n"))
altura =int(input("ingresa la altura \n"))
area = (base*altura)/2
print("la base es", base)
print("la altura es",altura)
print("el area del triangulo es ", area)
