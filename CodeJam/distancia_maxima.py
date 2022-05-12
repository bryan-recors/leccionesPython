"""
Dado un texto y un subtexto que podría estar en el texto, 
devuelva la distancia máxima del subtexto a cualquier lado del texto. 
Si el subtexto no está en el texto, devuelve -1. 
La distancia es el número de caracteres desde el subtexto 
hasta cualquiera de los lados del texto
"""
print("ejericio de distancia máxima")
indices_de_coincidencia = []
distancias = []

texto = input("ingresa el texto \n")
subtext = input("ingresa el subtexto \n")

for indice_texto,valor in enumerate(texto):
    if valor == subtext[0]:
        nuevo = texto[indice_texto:indice_texto+len(subtext)]
        if(nuevo == subtext):
            indices_de_coincidencia.append(indice_texto)

#print(indices_de_coincidencia)
#pasar los indices de coincidencas a las distancias ya que son las distancias respecto al lado izquierdo
for valor in indices_de_coincidencia:
    distancias.append(valor)

#calcular las distancias al lado derecho
for valor in indices_de_coincidencia:
    extremo_derecho = len(texto) - (valor+len(subtext))
    distancias.append(extremo_derecho)

print(distancias)

#ya con las distancias tomo el valor mayor si no hay es porque el texto no esta en el string
if len(distancias)>0:
    #ya con las distancias tomo el valor mayor 
    mayor = max(distancias)
    print("la distancia mayor es:", mayor)
else:
    print(-1)
