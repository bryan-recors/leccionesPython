"""
variable = [1,2,3,4]
variable = None
print (variable)
"""
print("hola mundo")
#estructuras de control
#if normal con else
"""
color_luz = 'verde'
if color_luz == 'verde':
    print("puede continuar")
else:
    print('Alto total')
#els e anidado
color_luz = 'verde'
if color_luz == 'verde':
    print("puede continuar")
else:
    print('Alto total')
"""
"""
#semaforo
color_luz = 'verde'
if color_luz == 'verde':
    print("puede continuar")
elif color_luz == 'amarillo':
    print('Alto parcial')
elif color_luz =='rojo':
    print('Alto total')
#boleanos
variable = True
if variable:
    print("es verdadero")
else:
    print("es falso")
#python toma como falso a " ",,' ' [],(),{},0,0.0
"""
"""
#ciclo while  hasta que una condicion deje de cumplirse
numero = 123456789
contador=0
while numero >= 1:
    contador+=1
    #si quiero reducir
    #contador-=1
    numero = numero /10
print("la cantidad de digitos del numero es",contador )
"""
#uso else con el ciclo
"""
numero = 123456789
contador=0
while numero >= 1:
    contador+=1
    #si quiero reducir
    #contador-=1
    numero = numero /10
else:
    print("la cantidad de digitos del numero es",contador )
"""
"""
#ciclo for
numeros=[1,2,3,4,5,6,7,9,10]
for numero in numeros:
    print(numero)

for valor in range(10):
    print(valor)

#numeros impares
lista = [1,2,3,4,5,6]
for indice in range( len(lista)):
    print("indice:", indice, "valor", lista[indice])


#condicional en una sola linea de codigo
calificacion=5
color="verde" if calificacion >=7 else 'rojo'
print(calificacion, color)
"""

#hacer un tringulo rectangulo de *
lista = [1,2,3,4,5,6]
for valor1 in range(5):
    for valor2 in range(valor1):
        #el end indica que no se de un salto de linea como viene por defecto
        #en este caso estamos indicando que no ponga nada
        print('*',end='') 
    print('\n')

#Break
titulo = "curso de Python 3"
for caracter in titulo:
    if caracter == "P":
        break #finaliza el ciclo de forma abrupta
    print(caracter)

#continue
titulo = "curso de Python 3"
for caracter in titulo:
    if caracter == "P":
        continue #indica un salto a la siguiente iteracion
    print(caracter, end='')