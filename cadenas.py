#TRucos Atom
#duplicar lineas de codigo bien rapido
#me pongo en la linea y con
#control+shift+d se ira copiando solo
"""
#mover un linea de codigo
asemos click en el lugar exacto donde queremos los
y con control+alt+flechas
"""
"""
señalar una palabra y cambiar a todas las que tengan ese nombres
con control+d otra ves contol+d y voy marcando las
palabras que quiero cambiar
"""
#cadenas
#el texto se trabaja con string
#los string no son mas que cadenas de caracteres con un orden establecido
#al igual con las tuplas y listas podemos usar los indices
print("para definir cadenas podemos usar comillas dobles o simples")
#si uso " " dentro puedo usar comillas '' y viceversa
curso="curso de python 3"
#cuantos caracteres tiene
resultado = len(curso)
print(resultado)
#obtener la primera letra
resultado = curso[0]
print(resultado)
# si coloco un numero negatico comiensa desde el final del string
resultado = curso[-1]
print(resultado)
#si coloco un indice que no existe sale error
#puedo generar subestring
#para ello indico la posicion inicial, final y si quiero saltos
resultado = curso[1:16]
print(resultado)
resultado = curso[1:16:2]
print(resultado)
#si quiero modificar un caracter de mi string
"""
curso[0] = "k"
print(curso)
"""
#me sale error ya que el string igual que las tuplas son inmutables
#no puedo modificar un string que ya a sido declarado
# lo que puedo hacer es generar un nuevo a partir del existente
#uso del metodo Split
lenguajes ="Python; Java; Ruby; PHP; Swift; JavaScript; C#; C; C++"
#deparados por un ; Y ESPACIO
resultado = lenguajes.split()
print(resultado)
# nos devolvera una nueva lista dentro de la lista esta
#cada string que es un lenguae de progra con el ;
#el metodo split retorna una nueva lista a partir del texto utilizado
#el texto es dividido mediante un separador el separador por default es un ESPACIO
#si no quiero dividir el texto mediante el espacio entre los parentesis indico
#cual sera mi separador split(";")
resultado = lenguajes.split(";")
print(resultado)
#observo los lenguajes con un espacio al inicio
#puedo ser mas especifico
separador = "; "
resultado = lenguajes.split(separador)
print(resultado)
# me devuelve sin espacio mi;
#metodo inverso
#con el metodo yoing pudo hacer un string a partir de una listas
# por el momento resultado es una lista
nuevoString = " ".join(resultado)
print(nuevoString)
# si yo quiero separar con otra cosa lo pongo en donde esta los " "
nuevoString = "_".join(resultado)
print(nuevoString)
#si quiero volver a como estaba antes
nuevoString = separador.join(resultado)
print(nuevoString)
# cuando nuestro string tiene saltos de linea
texto = """ Este es un texto
con
saltos

linea"""
print(texto)
 #usamos el metodo splitlines
resultado = texto.splitlines()
print(resultado)
#observamos una lista
#Formato para el texto para consola web o pdf
escrito = "curso de Python 3"
# metodo capitalize retorna un nuevo string
resultado = escrito.capitalize()
print(resultado)
#lo que hace es generar un nuevo string con la primera letra en mayuscula
#metodo swapcase
resultado = escrito.swapcase()
print(resultado)
#nos da un nuevo string donde todas las letras en minuscula
#las transforma a mayusculas y todas las minusculas a mayusculas
#si quiero solo mayusculas uso el metodo upper
resultado = escrito.upper()
print(resultado)
# todas a minusculas
resultado = escrito.lower()
print(resultado)
# si quiero saber si mi string esta en mayuscula uso isupper
print(resultado.isupper())
print(resultado.islower())
#metodo title
resultado = escrito.title()
#nos devolvera un nuevo string con un formato de titulo
print(resultado)
#metodo replace reemplazara un string por otro
#necesita por valores obligatoriamente
#("valor a reemplazar", "valor por el cual va a ser reemplazado")
resultado = escrito.replace("Python","ruby")
print(resultado)
#todos los string q tengas ese nombre seran reemplazados
#con metodo replace podemos especificar cuantas veces uestro string sea reemplazados
#para ello colocamos un tercer valor pero entero
escritura = "  Curso de Python 3, Python básico  "
resultado = escritura.replace("Python", "ruby",1)
print(resultado)
#como vimos solo reemplazo una vez
#metodo Strip retorna un nuevo string
#sin los espacios que se pudieran encontrar al principio o final
# escritura tiene dos espacios al inicio y final
resultado=escritura.strip()
print(resultado)
print("falta formatos parte 2")
#otra forma de dar formato a un string sin un metodo
curso= "Python"
version = "3"
resultado = "Curso de %s %s" %(curso,version)
print(resultado)
#% resive las variables
#usando format
resultado="Curso de {} {}".format(curso, version)
print(resultado)
#las llaves van a ser reemplazadas por el contenido de las variables
#podemos dar nombrea los valores que hemos colocado dentro
resultado="Curso de {a} {b}".format(b=curso, a=version)
print(resultado)
#******Concatenacion******************************
# que pasa si quiero modificar uno o mas caracteres dentro de mi string
curso = "Curso de python"
#quiero cambiar la C por c pero los string son inmutables
#generamos un nuevo string con uso de la Concatenacion
curso= "c"+ curso[1:] #concaneto la c con un substring
print(curso)
#si quiero concatenar otro tipo de dato q no es string
#no lo podremos hacer
#podemos usar la funcion str para convertir el valor entre () y nos retorna
curso =curso[:] +" "+str(3) #str convierte todo tipo de dato a string
print(curso)
#************* busqueda de cadenas
#nos permite saber si un string esta dentro de otro
mensaje="Este es un texto un poco grande en cuanto a longitud de caracteres"
resultado = mensaje.count("texto") #con esto busco texto dentro del string
#nos devuelve un entero y corresponde a cuantas veces se encuantra esa palabra
print("texto se repite",resultado)
resultado = mensaje.count("e")
print("e se repite",resultado)
# si no hay ninguna saldra 0
#otra forma es usar in
resultado = "texto" in mensaje
print(resultado) #devuelve un booleano
resultado = "texto" not in mensaje #podemos negarlo
print(resultado) #devuelve un booleano
#otra forma es hacer unso del metodo find
resultado = mensaje.find("texto")
print(resultado) #devuelve un entero cuyo valor hace referencia
#a la posicion donde se encuentra nuestro string
resultado = mensaje[resultado: resultado + len("texto")] #le digo q empiese en la posisicon 11 hasta el tamaño del len nos entrega
# hemos extraido texto de nuestro string original
print(resultado)
#si el string q no existe no hay retorna -1
#*******metodo starwit para saber si un string comiensa o termina con otro
resultado=mensaje.startswith("Este")#retorna un booleano
print(resultado) # el resultado es verdadero porq si esta al inicio
resultado=mensaje.endswith("Este")
print(resultado)#falso porq no esta al final
