"""
#primera forma de definir una clase e instanciar objetos
class persona:
    lugarTrabajo = "hospital"
    sueldo = "2000"
medico=persona()
print(medico.lugarTrabajo)
print(medico.sueldo)
"""
#segunda forma de definir una clase e instanciar objetos

#creacion de la clase
class Persona:
    pass
#pass: es una sentencia nula con la que
#puedo salir de la ejecucion normal de clase

#instancio los objetos
medico=Persona()
teacher=Persona()
contador=Persona()
estudiante=Persona()
turista=Persona()

#defino los atributos y caracteristias
#objeto 1 Medico
medico.nombre = "Bryan"
medico.apellido = "Sandoval"
medico.lugarTrabajo = "Hospital"
medico.sueldo = 1500
medico.direccion = "Quito"
medico.email = "bryan@gmail.com"
#objeto 2 Teacher
teacher.nombre = "Johana"
teacher.apellido = "Sanchez"
teacher.lugarTrabajo = "UTC"
teacher.sueldo = 1000
teacher.direccion = "Latacunga"
teacher.email = "johana@hotmail.com"
#objeto 3 Contador
contador.nombre = "Carlos"
contador.apellido = "Zuares"
contador.lugarTrabajo = "Empresa Electrica"
contador.sueldo = 1200
contador.email = "carlos@hotmail.com"
contador.edad = 21
#objeto 4 Estudiante
estudiante.nombre = "Alejandro"
estudiante.apellido = "Sandoval"
estudiante.edad = 24
estudiante.email = "alejo@hotmail.com"
estudiante.carrera = "sistemas"
estudiante.curso = 7
#objeto 5 Turista
turista.nombre = "Diego"
turista.apellido = "Perez"
turista.edad = 34
turista.paisProcedencia = "Argentina"
turista.email = "diego@hotmail.com"
turista.diasHospedaje = 3
#imprimir caracteriscas
print("\n\tDatos del Medico")
print("\nNombre: ",medico.nombre +" "+ medico.apellido)
print("Lugar de trabajo: ",medico.lugarTrabajo)
print("Sueldo: ",medico.sueldo)
print("Direccion: ",medico.direccion)
print("Email: ",medico.email)

print("\n\tDatos del Teacher")
print("\nNombre: ",teacher.nombre +" "+ teacher.apellido)
print("Lugar de trabajo: ",teacher.lugarTrabajo)
print("Sueldo: ",teacher.sueldo)
print("Direccion: ",teacher.direccion)
print("Email: ",teacher.email)

print("\n\tDatos del Contador")
print("\nNombre: ",contador.nombre +" "+ contador.apellido)
print("Lugar de trabajo: ",contador.lugarTrabajo)
print("Sueldo: ",contador.sueldo)
print("Email: ",contador.email)
print("Direccion: ",contador.edad)

print("\n\tDatos del estudiante")
print("\nNombre: ",estudiante.nombre +" "+ estudiante.apellido)
print("Direccion: ",estudiante.edad)
print("Email: ",estudiante.email)
print("Sueldo: ",estudiante.carrera)
print("Sueldo: ",estudiante.curso)

print("\n\tDatos del turista")
print("\nNombre: ",turista.nombre +" "+ turista.apellido)
print("Direccion: ",turista.edad)
print("Email: ",turista.paisProcedencia)
print("Sueldo: ",turista.email)
print("cuantos dias se hospedara: ",turista.diasHospedaje)
