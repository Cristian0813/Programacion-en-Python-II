# Pregunta 1 Dada la definición de Carta vista en clases. Si quieres crear una nueva clase Carta que tenga
# como atributos la pinta, el número y la baraja a la que pertenece (“Azul” o “Roja”). ¿Cuál sería la definición correcta de la clase con su constructor?

class Carta:
    def __init__(self, p, num, bar):
        self.pinta = p
        self.num = num
        self.bar = bar

# Ejemplo de uso
    def __str__(self):
        return f"Carta\n Pinta: {self.pinta}\n Número: {self.num}\n Baraja: '{self.bar}\n"
mi_carta = Carta('Corazones', 7, 'Roja')
print(mi_carta)
print()
print("-----------------------------------------------------------------------")
#-----------------------------------------------------------------------------
print()

# Pregunta 2 Quieres definir la clase Adulto, la cual recibe como parámetro un nombre y una edad
# y guarda esa información en los atributos nombre y edad respectivamente.
# ¿Cuál de los siguientes códigos la define correctamente?

class Adulto:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
# Ejemplo de uso
    def __str__(self):
        return f"Nombre: {self.nombre}\n Edad: {self.edad}\n"
adulto1 = Adulto('Carlos', 82)
adulto2 = Adulto('Erica', 22)
adulto3 = Adulto('Felipe', 33)
print (adulto1)  
print (adulto2)  
print (adulto3)  

print()
print("-----------------------------------------------------------------------")
#-----------------------------------------------------------------------------
print()

# Pregunta 3 Dada la definición de Estudiante vista en clases:

class Estudiante:
    def __init__(self,n,p,f):
        self.nombre = n
        self.parcial = p
        self.final = f

# El profesor decide sumarle 5 a la nota final de todos los alumnos.
# ¿Cuál de los siguientes códigos modifica el inicializador anterior
# para que la nota final que guarde el alumno sea 5 más que la nota
# que recibe como parámetro f?

class Estudiante:
    def __init__(self,n,p,f):
        self.nombre = n
        self.parcial = p
        self.final = f+5

# Ejemplo de uso
    def __str__(self):
        return f"Nombre del estudiante: {self.nombre}\n Nota de parcial: {self.parcial}\n Nota final: {self.final}\n"

estudiante1 = Estudiante('Carlos', 80, 70)
estudiante2 = Estudiante('Camilo', 10, 92)
estudiante3 = Estudiante('Pedro', 70, 55)

print(estudiante1)
print(estudiante2)
print(estudiante3)

print()
print("-----------------------------------------------------------------------")
#-----------------------------------------------------------------------------
print()

# Pregunta 4 Dada la definición de Estudiante vista en clases:

class Estudiante:
    def __init__(self,n,p,f):
        self.nombre = n
        self.parcial = p
        self.final = f

# El profesor decide no almacenar el nombre de cada alumno, sino que
# en su lugar decide guardar en el atributo nombre solamente la
# primera letra del nombre recibido. Considerando que el constructor
# recibe el nombre completo del alumno, su nota parcial y su nota final.
# ¿Cuál de los siguientes código hace lo pedido por el profesor?

class Estudiante:
    def __init__(self,n,p,f):
        self.nombre = n[0]
        self.parcial = p
        self.final = f
# Ejemplo de uso
    def __str__(self):
        return f"Nombre del estudiante: {self.nombre}\n Nota de parcial: {self.parcial}\n Nota final: {self.final}\n"

estudiante1 = Estudiante('Nicole', 80, 70)
estudiante2 = Estudiante('Isabella', 10, 92)
estudiante3 = Estudiante('Thaliana', 70, 55)

print(estudiante1)
print(estudiante2)
print(estudiante3)

print()
print("-----------------------------------------------------------------------")
#-----------------------------------------------------------------------------
print()

# Pregunta 5 Dada la definición de Carta vista en clases:

""" 
class Carta:
    def __init__(self, p, num)
        self.pinta = p
        self.num = n
 """
# Se quiere cambiar el constructor para recibir primero el
# parámetro de número y después el parámetro de pinta.
# ¿Cuál de los siguientes constructores NO cumple este requisitos?
""" 
(x) class Carta:
        def __init__(self, num, p)
            self.pinta = num
            self.num = p
 """

#-----------------------------------------------------------------------------

# Pregunta 6 Quieres definir una clase Empleado, la cuál recibe como
# parámetro de su constructor un nombre y un número de teléfono.
# El número de teléfono puede venir en uno de los siguientes formatos:

# - Un entero de 8 dígitos
# - Un entero de 9 dígitos que comienza con 9
# - Un string de 9 dígitos que comienza con 9
# - Un string que comienza con +569 seguido de 8 dígitos

# El constructor de la clase Empleado deberá recibir un nombre y
# un número en uno de los formatos anteriores. La clase deberá guardar
# el nombre, además del número con el formato +569 seguido de 8 dígitos.

# ¿Cuál de los siguientes códigos define correctamente el constructor de la clase Empleado?

class Empleado:
    def __init__(self, nombre, numero):
        self.nombre = nombre

        numero = str(numero)
        faltan = 12 - len(numero)
        self.numero = '+569'[:faltan] + numero

# Ejemplo de uso
    def __str__(self):
        return f"Empleado: {self.nombre}\n Numero: {self.numero}\n"

empleado1 = Empleado('Juan Pérez', 12345678)
empleado2 = Empleado('Maria Gómez', 987654321)
empleado3 = Empleado('Cristian Arias', 989654329)
print(empleado1)
print(empleado2)
print(empleado3)
print()
print("-----------------------------------------------------------------------")
#-----------------------------------------------------------------------------
print()

# Pregunta 7 Dada la definición de Estudiante vista en clases: 

class Estudiante: 
    def __init__(self,n,p,f): 
        self.nombre = n 
        self.parcial = p 
        self.final = f 

# ¿Cuál es los siguientes códigos le agrega correctamente a la clase
# el método recorreccion_parcial(self, nota_nueva), el cual recibe
# como parámetro la nota recorregida de la evaluación parcial del
# alumno? El método debe reemplazar la nota del parcial que tenía
# el alumno por la nota nota_nueva. 

class Estudiante: 
    def __init__(self, n, p, f): 
         self.nombre = n 
         self.parcial = p 
         self.final = f
    
    def recorreccion_parcial(self, nota_nueva): 
        self.parcial = nota_nueva 
        
# Ejemplo de uso
    def __str__(self):
        return f"Nombre del estudiante: {self.nombre}\n Nota de parcial: {self.parcial}\n Nota final: {self.final}\n"

estudiante1 = Estudiante('Nicole', 8.0, 7.0)
estudiante2 = Estudiante('Isabella', 1.0, 9.2)
estudiante3 = Estudiante('Thaliana', 7.0, 5.5)

print(estudiante1)
print(estudiante2)
print(estudiante3)

estudiante2.recorreccion_parcial(9.0)
print(f"\nEl estudiante: {estudiante2.nombre} su nota parcial: {estudiante1.parcial} - Final: {estudiante1.final}")
print()
print("-----------------------------------------------------------------------")
#-----------------------------------------------------------------------------
print()

# Pregunta 8 Tienes la siguiente clase: 

class Estudiante: 
    def __init__(self, n):
        self.nombre = n 
        self.notas = [] 
# ¿Cuál de los siguientes códigos le agrega correctamente a la clase
# anterior el método agregar_nota(self, nota)? Este método deberá
# recibir como parámetro un entero nota. El método deberá agregar
# la nota recibida a la lista de notas del alumno. 

class Estudiante:
    def __init__(self, n):
        self.nombre = n
        self.notas = []

    def agregar_nota(self, nota):
        self.notas.append(nota)

    def mostrar_notas(self):
        print(f"Estudiante: {self.nombre}")
        print(f"Notas:")
        for nota in self.notas:
            print(f"{nota}")

# Ejemplo de uso
estudiante1 = Estudiante('Juan Pérez')
estudiante1.agregar_nota(7.5)
estudiante1.agregar_nota(8.2)
estudiante1.agregar_nota(9.0)

estudiante1.mostrar_notas()
print()
print("-----------------------------------------------------------------------")
#-----------------------------------------------------------------------------
print()

# Pregunta 9 Tienes la clase: 

class Estudiante:
    def __init__(self, nombre, notas):
        self.nombre = nombre
        self.notas = notas

# Sabemos que nombre es un string y notas es una lista de floats, por ejemplo, notas puede ser [6.2, 5.5,4.8]. Al imprimir esta clase quieres que se imprima lo siguiente:
# Nota mínima X - Nota máxima Y

# Por ejemplo, si tienes una Estudiante Alicia con las notas 
# [6.2, 5.5, 4.8]. Entonces deberá imprimir:
# Nota mínima 4.8 - Nota máxima 6.2
# ¿Cuál de los siguientes códigos hace lo pedido?

class Estudiante:
    def __init__(self, nombre, notas):
        self.nombre = nombre
        self.notas = notas

    def __str__(self):
        menor = min(self.notas)
        mayor = max(self.notas)
        return 'Nota mínima '+str(menor)+' - Nota máxima ' + str(mayor)

# Ejemplo de uso
estudiante1 = Estudiante('Juan Pérez', [7.5, 8.2, 9.0])
estudiante2 = Estudiante('Maria Gómez', [6.8, 9.4, 8.5])
print(estudiante1)
print(estudiante2)

print()
print("-----------------------------------------------------------------------")
#-----------------------------------------------------------------------------
print()

# Pregunta 10 Tienes la siguiente clase ya definida: 

class Gato:
    def __init__(self):
        self.tablero = [[' ']*3,
                        [' '] * 3,
                        [' '] * 3]
        
# Esta clase representa un juego de Gato, donde inicialmente hay
# un tablero vacío. Esta clase necesita el método 
# jugada(self, fila, columna, figura), el cual recibe como parámetros
# dos enteros (fila y columna) y un string figura. El método deberá
# asegurarse de lo siguiente:

# (a) fila y columna deben ser enteros entre 0 y 2 inclusive.
# (b) figura tiene que ser un string de un solo carácter
# (c) la posición indicada del tablero debe estar vacía
# (ser un string inicial del tablero)

# Si no se cumple alguna de estas condiciones, la función deberá
# retornar False. En caso de que se cumplan todas las condiciones
# se deberá actualizar el tablero con la jugada y retornar True.
# ¿Cuál de los siguientes códigos define el método correctamente?

class Gato:
    def __init__(self):
        self.tablero = [[' ']*3,
                        [' '] * 3,
                        [' '] * 3]

    def jugada(self, fila, columna, figura):
        if fila < 0 or fila > 2:
            return False
        if columna < 0 or columna > 2:
            return False
        if len(figura) != 1:
            return False
        if self.tablero[fila][columna] != ' ':
            return False
        self.tablero[fila][columna] = figura
        return True
    
# Ejemplo de uso
    def mostrartablero(self):
        for fila in self.tablero:
            print("| " + "| ".join(fila)+" |")
gato = Gato()
gato.jugada(0, 0, "X")
gato.jugada(1, 1, "O")
gato.jugada(2, 2, "X")

gato.mostrartablero()