
#crear una clase
#nomenclatura CamelCase primera letra en mayuscula
class Usuario1:
    pass #es una sentencia nulla

#instanciar objetos es crear un objeto
codi=Usuario1()
facilito=Usuario1()

#saber de que tupo de clase es un objeto
print(type(facilito))
#nos dira q es de Usuario

#metodos son funciones q estan dentro de la clase
class Usuario:
    pass
    #los metodos vna dentro de la clase
    def saluda(self): #self se usa por convencion hace referencia al objeto en si
        print("hola, soy un usuario")
    #puedo especificar parametros
    def saludo(self, nombre):
        print("hola, soy: " + nombre)
    #funcin que retorna un valor
    def saludito(self, nombre):
        return "hola, soy: " + nombre

obj1=Usuario()
obj2= Usuario()
#se imprimira las repuestas por llamar a los metodos
obj1.saluda()
#todo lo de funciones es aplicable a los metodos
#metodo con parametro
obj2.saludo("alejandro")
#metodo con return
print(obj1.saludito("bryan"))

#*****************asignacion de atributos****************
#nuestros objetos pueden contener n cantidad de atributos
#para crear atributos se puede hacer de dos maneras fuera de la clase y dentro de la CamelCase
#fuera de la clase**************
class Persona:
    def saluda(self, nombre):
        return "hola, soy: " + nombre
    #funcion que devuelve el atributo username recive al objeto mismo
    #por eso puede acceder a los atributos
    def mostrar_username(self):
        print(self.username)

#instancio
persona1= Persona()
# indico los atributos fuera de la clase
persona1.username = "Bryan"
persona1.correo = "correo@utc"
#llamo un metodo
persona1.mostrar_username()
#generar atributos dentro de la clase **********************
class Individuo:
    def saluda(self, nombre):
        return "hola, soy: " + nombre
    #funcion que devuelve el atributo username recive al objeto mismo
    #por eso puede acceder a los atributos
    def mostrar_username(self):
        print(self.username)
    #creo el atributo dentro de la funcion a traves de un metodo
    def crear_nombre(self,nombre):
        self.nombre = nombre
    #mostrar el atributo
    def mostrar_nombre(self):
        print(self.nombre)

#instancio
individuo1 = Individuo()
#llamo un metodo para crear atributo nombre
individuo1.crear_nombre("sandoval")
individuo1.mostrar_nombre()
#los inconvenientes al momento de o definir un lugar donde crear atributos
#el codigo sera difisil de mantener y tendremos que estar buscando  entre lineas de codigo
#para evitar esto nos apoyaremos del metodo init para inicializar los atributos dentro de el
#metodo init **************************
print("usando metodo init ******")
class People:
    #init para inicializar los atributos
    def __init__(self, username="",correo="",nombre=""): #por default estaran vacios
        self.username = username #asigno no q llegue
        self.correo = correo #asigno no q llegue
        self.nombre = nombre #asigno no q llegue


    #metodo saluda
    def saludando(self):
        return "hola, que mas ve soy: " + self.nombre
    #funcion que devuelve el atributo username recive al objeto mismo
    #por eso puede acceder a los atributos
    def mostrar_username(self):
        print(self.username)
    #mostrar el atributo
    def mostrar_nombre(self):
        print(self.nombre)

#instancio pero con los valores de los atributos
people1 = People("alejUser","alejo@utc","alejo")
#imprimo los atributos
print("\n\tDatos del usuario")
print("Nombre de Usuario: ",people1.username)
print("Correo: ",people1.correo)
print("Nombre: ",people1.nombre)

#llamo un metodo para crear atributo nombre
resultado = people1.saludando()
print(resultado)
#tipos de atributos************************
print("tipos de atributos")
#en nuestras clases podemos tener dos tipos de variables
#las de instancia y las de clase
class Circulo:
    pi=3.14159265 #no coloco self esta es una variable de clase
    #las variables de clase les pertenecen a la clase y pueden ser
    #utilizadas por instancias
    def __init__(self, radio):
        self.radio = radio #es una variable de intancia
        #una variable de instancia son valores que le pertenecen a la instancia
        #y son independientes para cada una de ellas
        #es decir circulo a tiene un radio totalmente diferente a circulo b

circulo_a = Circulo(10)
circulo_b = Circulo(20)
#si intentamos modificar solo se modificara a la isntancia a la cual le pertenece
#las variables de instancia no se comparten enre instancia
print(circulo_a.radio)
print(circulo_b.radio)
circulo_b.radio = 100
#vemos q solo cambia uno
print(circulo_a.radio)
print(circulo_b.radio)
#imprimo la variable de clase es la misma en los dos casos
print(circulo_a.pi)
print(circulo_b.pi)
#podemos utilizar la varibale de clase sin hacer una instancia
print(Circulo.pi)

#metodo de instncia
class Triangulo:
    #metodo de istancia 
    def area(self):
        return (self.base*self.altura)/2

tringulo = Triangulo()
tringulo.base = 10
tringulo.altura = 20
resultado = tringulo.area()
print(resultado)

#metodos estaticos
class Triangulo:
    numero = 2
    #metodo de estatico
    @staticmethod
    def area(base,altura):
        return (base*altura)/Triangulo.numero

resultado = Triangulo.area(10,20)
print(resultado)

#metodos de clase
class Circulo:
    pi = 3.141592
    #metodo de clase
    @classmethod
    def area(cls, radio):
        return cls.pi * radio**2 

resultado = Circulo.area(10)
print(resultado)

#herencia y herencia multiple
# clase padre1 
class Animal:
    def comer(self):
        print("comiendo")
    def dormir(self):
        print("durmiendo")
    def comun(self):
        print("metodo de ANimal")

#clase Padre2
class Mascota:
    #creo un atributo fecha adopcion
    def fecha_adopcion(self,fecha):
        self.fecha_adopcion = fecha 
    def comun(self):
        print("metodo de Mascota")

#clase hija1
class Perro(Animal, Mascota):
    def __init__(self, nombre):
        self.nombre = nombre
    def ladrar(self):
        print("ladrando")

#clase hija2
class Gato(Animal):
    def __init__(self, nombre):
        self.nombre = nombre

    def ronronear(self):
        print("ronroneando")

#instanciamos un objeto perro
firulais = Perro("firulais")
print("perro")
firulais.ladrar()
firulais.comer()
firulais.dormir()
firulais.fecha_adopcion("hoy") #creo el atributo mediante el metodo
print("adopcion ",firulais.fecha_adopcion) #imprimo el atributo
firulais.comun()
#instanciamos un objeto Gato
miau = Gato("miau")
print("gato")
miau.ronronear()
miau.comer()
miau.dormir()

#sobreescritura de metodos 
# clase padre1 
class Animal:
    def comer(self):
        print("comiendo")
    def dormir(self):
        print("durmiendo")

#clase Padre2
class Mascota:
    #creo un atributo fecha adopcion
    def fecha_adopcion(self,fecha):
        self.fecha_adopcion = fecha 

#clase hija1
class Perro(Animal, Mascota):
    def __init__(self, nombre):
        self.nombre = nombre
    def ladrar(self):
        print("ladrando")
    def dormir(self):
        #funcionalidades antes
        print(self.nombre, "esta durmiendo!")
        Animal.dormir(self) #ejecutamos el metodo del padre
        #funcionalidades despeus
        print("no molestar")

#instanciamos un objeto perro
firulais = Perro("firulais")
print("perro")
firulais.ladrar()
firulais.comer()
firulais.dormir()
firulais.fecha_adopcion("hoy") #creo el atributo mediante el metodo
print("adopcion ",firulais.fecha_adopcion) #imprimo el atributo

#trabajando con Object*************
#forma 1 de crear una clase 
class Gato:
    def __init__(self,nombre):
        self.nombre = nombre
    #sobreescribir metodo del object
    def __str__(self):
        return self.nombre

#forma 2 de crear una clase colocando Object

class Pato(object):
    def __init__(self,nombre):
        self.nombre = nombre

    #sobreescribir metodo del object
    def __str__(self):
        return self.nombre

gato = Gato("bigotes")
pato = Pato("lucas")
print(gato.__dict__)
print(pato.__dict__)
