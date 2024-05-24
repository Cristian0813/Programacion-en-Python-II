# Pregunta 1 Tienes la siguiente clase Libro:

class Libro:
    def __init__(self, t, a, g):
        self.titulo = t
        self.autor = a
        self.genero = g
        
    def __str__(self):
        return self.titulo

L1 = Libro('Harry Potter', 'J. K. Rowling', 'Fantasía')
L2 = Libro('Juego de tronos', 'George R. R. Martin', 'Novela')
L3 = Libro('El señor de los anillos', 'J. R. R. Tolkien', 'Novela')

biblioteca = [L1, L2, L3]

# ¿Cuál de los siguientes códigos imprimirá correctamente el título
# de todas las novelas que hay en la biblioteca?

for libro in biblioteca:
    if libro.genero == 'Novela':
        print(libro)

print()
print("-------------------------------------------------------------------")
#--------------------------------------------------------------------
print()

# Pregunta 2 Tienes las siguientes clases que definen a una mascota y su dueño

class Mascota:
    def __init__(self, n, h):
        self.nombre = n
        self.dueño = h

class Humano:
    def __init__(self, n):
        self.nombre = n

humano = Humano('Alex')
perro = Mascota('Rex' , humano)

# Quieres agregarle a Mascota el método saludar(self, humano), el
# cual recibe como parámetro un humano que lo quiere saludar. El
# método deberá imprimir 'Hola {nombre humano}' si el humano es su
# dueño, y 'grrr, no te conozco {nombre humano}'. si el humano
# no es su dueño.
# ¿Cuál de los siguientes código agrega correctamente el método
# saludar?

class Mascota:
    def __init__(self, n, h):
        self.nombre = n
        self.dueño = h

    def saludar(self, humano):
        if humano == self.dueño:
            return 'Hola '+ humano.nombre
        return 'grrr, no te conozco ' + humano.nombre

class Humano:
    def __init__(self, n):
        self.nombre = n

humano = Humano('Alex')
perro = Mascota('Rex' , humano)

# Ejemplo de uso
print(perro.saludar(humano))
otro_humano = Humano('Benito')
print(perro.saludar(otro_humano))

print()
print("-------------------------------------------------------------------")
#--------------------------------------------------------------------
print()

# Pregunta 3 Tienes las siguientes clases que definen a una aula
# y sus alumnos

class Aula:
    def __init__(self, p):
        self.profesor = p
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

class Estudiante:
    def __init__(self, nom, nota):
        self.nombre = nom
        self.nota_final = nota

class Profesor:
    def __init__(self, n):
        self.nombre = n

profesor = Profesor( 'Calamardo' )
e1 = Estudiante( 'Bob', 6 )
e2 = Estudiante( 'Patricio', 2 )
e3 = Estudiante( 'Arenita', 7 )

aula = Aula(profesor)
aula.agregar_estudiante(e1)
aula.agregar_estudiante(e2)
aula.agregar_estudiante(e3)

# Quieres agregarle al Aula el método imprimir_mejor_nota(self). El
# método deberá imprimir la nota final más alta entre todos los
# estudiantes del aula ¿Cuál de los siguientes código agrega
# correctamente el método imprimir_mejor_nota?

class Aula:
    def __init__(self, p):
        self.profesor = p
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)
        
    def imprimir_mejor_nota(self):
        mejor = 0
        for estudiante in self.estudiantes:
            if estudiante.nota_final > mejor:
                mejor = estudiante.nota_final
        print(mejor)
        

class Estudiante:
    def __init__(self, nom, nota):
        self.nombre = nom
        self.nota_final = nota

class Profesor:
    def __init__(self, n):
        self.nombre = n

profesor = Profesor( 'Calamardo' )
e1 = Estudiante( 'Bob', 6 )
e2 = Estudiante( 'Patricio', 2 )
e3 = Estudiante( 'Arenita', 7 )

aula = Aula(profesor)
aula.agregar_estudiante(e1)
aula.agregar_estudiante(e2)
aula.agregar_estudiante(e3)

#Ejemplo de uso
aula.imprimir_mejor_nota()

print()
print("-------------------------------------------------------------------")
#--------------------------------------------------------------------
print()

# Pregunta 4 Tienes la siguiente clase Estudiante:

class Estudiante:
    def __init__(self, nom):
        self.nombre = nom
        self.notas = []

eva = Estudiante('Eva')

# Sabes que para agregar notas al atributo notas de eva
# deberías escribir:

eva.notas.append(6.8)

# Para facilitarte la escritura de esta acción decides sobreescribir
# el operador +. De este modo, para agregar una nota a eva bastaría
# con escribir:

eva + 6.8

# ¿Cuál de los siguientes códigos agrega el método __add__ correctamente?

class Estudiante:
    def __init__(self, nom):
        self.nombre = nom
        self.notas = []

    def __add__(self, nota):
        self.notas.append(nota)
    
    def mostrar_notas(self):
        print(f"Estudiante: {self.nombre}")
        print(f"Notas:")
        for nota in self.notas:
            print(f"- {nota}")

eva = Estudiante('Eva')
eva + 6.8
eva.mostrar_notas() 

print()
print("-------------------------------------------------------------------")
#--------------------------------------------------------------------
print()

# Pregunta 5 Tienes la siguiente clase 

class Vehiculo:
    
    def __init__(self):
        self.ruedas = 4
        self.kilometraje = 0
        
    def avanzar(self, km):
        self.kilometraje += km

    def cambiar_neumaticos(self):
        print(f"Se han cambiado las {self.ruedas} ruedas")

# Decides crear la clase Camion en base a Vehiculo. Esta clase debe 
# heredar de Vehiculo, pero con los siguientes cambios: en lugar de 
# tener 4 ruedas tiene 6 y deberá tener el método 
# ver_kilometraje(self) el cuál deberá retornar el kilometraje 
# actual del vehículo. 
# ¿Cuál de los siguientes códigos define la clase Camion correctamente?

class Camion(Vehiculo):
    def __init__(self):
        super().__init__()
        self.ruedas = 6

    def ver_kilometraje(self):
        return self.kilometraje
# Ejemplo de uso
camion = Camion()
camion.avanzar(50)

print(f"Kilometraje actual del camión: {camion.ver_kilometraje()} km")
camion.cambiar_neumaticos()

print()
print("-------------------------------------------------------------------")
#--------------------------------------------------------------------
print()

# Pregunta 6 Tienes la clase Mueble:

class Mueble:
    def __init__(self, h, a, l, v):
        self.alto = h
        self.ancho = a
        self.largo = l
        self.valor = v

    def precio(self):
        return self.alto * self.ancho * self.largo * self.valor


M1 = Mueble(1.0, 2.0, 3.0, 50)
M2 = Mueble(2.0, 2.0, 2.0, 600)
M3 = Mueble(1.5, 1.5, 3.0, 40)

tienda = [M1, M2, M3]

# ¿Cuál de los siguientes códigos crea una nueva lista tienda, tal
# que los muebles dentro de esta nueva lista estén ordenados de 
# menor a mayor precio?

tienda_aux = []
while len(tienda) > 0:
        menor = tienda[0]
        for mueble in tienda:
            if menor.precio() > mueble.precio():
                menor = mueble
        tienda.remove(menor)
        tienda_aux.append(menor)
tienda = tienda_aux
# Impresión de los muebles ordenados
print("Muebles ordenados por precio:")
for mueble in tienda:
    print(f"- Alto: {mueble.alto} - Ancho: {mueble.ancho} - Largo: {mueble.largo} - Valor: {mueble.valor} - Precio: {mueble.precio()}")

print()
print("-------------------------------------------------------------------")
#--------------------------------------------------------------------
print()

# Pregunta 7 ¿Que imprime el siguiente código?

class A:
    def __init__(self, val):
        self.value = val

    def sumar_a_valor(self, suma):
        self.value += suma

    def sumar_valor_y_retornar(self, suma):
        self.sumar_a_valor(suma)
        return self.value

class B(A):
    def __init__(self, val):
        self.value = val + 2

    def sumar_valor_y_retornar(self, suma):
        self.sumar_a_valor(suma)
        return self.value

foo = B(10)
print(foo.sumar_valor_y_retornar(5))

# No imprime, levanta error ya que sumar_a_valor no está definida
# en B
"""
    (x) 17
"""
print()
print("-------------------------------------------------------------------")
#--------------------------------------------------------------------
print()

# Pregunta 8 Tienes la siguiente clase Vehiculo:

class Vehiculo:
    def __init__(self, r):
        self.ruedas = r
        self.kilometraje = 0

    def avanzar(self):
        self.kilometraje += 10

    def tiempo_reparacion(self):
        if self.ruedas == 2:
            return 5
        if self.ruedas > 4:
            return 20
        return 10

# Debes definir la clase Taller. En este taller los autos se reparan
# en orden de llegada, sin embargo, siempre se reparan en primer lugar
# los vehículos que toman menos de 15. Si no hay vehículos que se
# demoren menos de 15, entonces reparan al vehículo de más de 15 que
# lleve más rato en el taller.

# ¿Cuál de los siguientes código define correctamente una clase
# Taller, además de su constructor y un método siguiente_vehículo, el
# cuál retorna correctamente el siguiente vehículo a reparar?

from collections import deque

class Taller:
    def __init__(self):
        self.rapidos = deque()
        self.lentos = deque()

    def agregar_vehiculo(self, veh):
        if veh.tiempo_reparacion() < 15:
            self.rapidos.append(veh)
        else:
            self.lentos.append(veh)

    def siguiente_vehiculo(self):
        if len(self.rapidos) > 0:
            return self.rapidos.popleft()
        return self.lentos.popleft()

# Crear instancias de Vehiculo
vehiculo1 = Vehiculo(2)  # Bicicleta
vehiculo2 = Vehiculo(4)  # Coche
vehiculo3 = Vehiculo(6)  # Camión

# Crear instancia de Taller
taller = Taller()

# Agregar vehículos al taller
taller.agregar_vehiculo(vehiculo1)
taller.agregar_vehiculo(vehiculo2)
taller.agregar_vehiculo(vehiculo3)

# Obtener y mostrar el siguiente vehículo para reparar
siguiente_vehiculo = taller.siguiente_vehiculo()
print(f"Siguiente vehículo para reparar tiene {siguiente_vehiculo.ruedas} ruedas y un kilometraje de {siguiente_vehiculo.kilometraje} km.")

    
print()
print("-------------------------------------------------------------------")
#--------------------------------------------------------------------
print()

# Pregunta 9 Tienes la siguiente clase de Usuario:

class Usuario:
    def __init__(self, nombre, password):
        self.nombre = nombre
        self.passw = password

# Además, tiene la siguiente clase Netflix:  

class Netflix:
    def __init__(self):
        self.usuarios = dict()
        self.siguiente_id = 0

    def agregar_usuario(self, usuario):
        self.usuarios[self.siguiente_id] = usuario
        self.siguiente_id += 1

# Quieres agregar a la clase Netflix el método conectarse(self, 
# nombre, password), la cual representa el inicio de sesión de un 
# usuario. El método deberá retornar True si existe algún usuario en 
# la lista de usuarios que tenga ese nombre y contraseña; y debe 
# retornar False en caso contrario. 


# ¿Cuál de los siguientes códigos define conectarse correctamente? 

# Puedes suponer que en todos los casos el método se define dentro 
# de la clase Netflix.

def conectarse(self, nombre, password):
        for usuario_id in self.usuarios:
            usuario = self.usuarios[usuario_id]
            if usuario.nombre == nombre and usuario.passw == password:
                return True
        return False

# Ejemplo de uso
# Crear instancias de Usuario
usuario1 = Usuario("usuario1", "password1")
usuario2 = Usuario("usuario2", "password2")

# Crear instancia de Netflix
netflix = Netflix()

# Agregar usuarios a Netflix
netflix.agregar_usuario(usuario1)
netflix.agregar_usuario(usuario2)

# Intentar conectarse
print(netflix.conectarse("usuario1", "password1"))  # Debería imprimir True
print(netflix.conectarse("usuario2", "password1"))  # Debería imprimir False
print(netflix.conectarse("usuario3", "password3"))  # Debería imprimir False

print()
print("-------------------------------------------------------------------")
#--------------------------------------------------------------------
print()

# Pregunta 10 Dado el siguiente código:

class Gema:
    def __init__(self, nom, dur, vol):
        self.nombre = nom
        self.dureza = dur
        self.volumen = vol

    def precio(self):
        return self.dureza * self.volumen * 500

gemas = []
llenar_lista(gemas)

# Sabes que la función llenar_lista(gemas) llena la lista gemas con
# varias instancias de la clase Gema. Te piden que retornes una lista
# de diccionarios, donde cada diccionario de la lista contiene la
# información de una instancia de la lista gemas. Estos diccionarios
# deberán tener las keys: nombre, dureza, volumen y precio. El value
# de estas keys deberá ser el valor que tienen estos atributos en la
# instancia, el key precio deberá tener de valor el retorno del método
# precio(). Por ejemplo, si gemas tiene las siguientes instancias:

g1 = Gema('Esmeralda', 7.5, 60)
g2 = Gema('Ruby', 9, 30)
g3 = Gema('Diamante', 10, 20)

gemas = [g1, g2, g3]

# Entonces tu función deberá retornar la siguiente lista:

# [{'nombre': 'Esmeralda',
# 'dureza': 7.5,
# 'volumen': 60,
# 'precio': 225000},{
# 'nombre': 'Ruby',
# 'dureza': 9,
# 'volumen': 30,
# 'precio': 135000},{
# 'nombre': 'Diamante',
# 'dureza': 10,
# 'volumen': 20,
# 'precio': 100000}]

# ¿Cuál de los siguientes códigos imprime correctamente la lista pedida?

lista = []
for gema in gemas:
    diccionario = {
        'nombre': gema.nombre,
        'dureza': gema.dureza,
        'volumen': gema.volumen,
        'precio': gema.precio()
    }
    lista.append(diccionario)
print(lista)