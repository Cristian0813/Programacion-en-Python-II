# Pregunta 1
n=5
contador = 0
def func(n):
    global contador
    if n == 0:
        return 0
    for i in range(n):
        func(n-1)
        contador += 1
func(5)

# Sin contar el llamado de la línea 7. ¿Cuántas veces se llama a la
# función func en el código anterior?

print("Total de llamadas a la función:", contador)
"""
    (x) 325
"""

print()
print("-------------------------------------------------------------------")
#--------------------------------------------------------------------
print()

# Pregunta 2

def func(n):
    if n == 0:
        print("Caso base alcanzado") # Print base case
        return 0
    else:
        print(f"Llamando a func({n})") # Print function call
        return func(n/2+1)

func(16)


# Sin contar el llamado de la línea 6. ¿Cuántas veces se llama a la
# función func en el código anterior?

"""
(x) Infinitas (Llega al límite de recursión)
"""

#--------------------------------------------------------------------
print()

# Pregunta 3

def func(nom, lista):
    otra = lista
    for i in range(len(nom)):
        otra.append(nom[0])
        func(nom[1:], otra)

output = []
func("Sol", output)
print(output)

# ¿Que imprime el código anterior?

"""
    (x) ['S', 'o', 'l', 'o', 'l', 'S', 'o', 'l', 'o', 'l', 'S', 'o', 'l', 'o', 'l']
"""

print()
print("-------------------------------------------------------------------")
#--------------------------------------------------------------------
print()

# Pregunta 4 La secuencia de Fibonacci es una secuencia númerica que
# tiene como primer y segundo valor el 1. Cada uno de los valores
# siguientes es la suma de los dos anteriores. Así, la secuencia se
# ve de la siguiente forma:

# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, …..

# Esto se debe a que:

# 1 + 1 = 2
# 1 + 2 = 3
# 2 + 3 = 5
# 3 + 5 = 8
# ... ...

# y así sucesivamente.

# Quieres crear la función fib(n), la cual, dado un n , retorna el 
# valor en la posición n de la secuencia de Fibonnaci. En el ejemplo 
# anterior si n = 0 ó n=1, entonces fib(n) retornaría 1, mientras 
# que fib(4) retorna 5 y fib(5) retorna 8.

# Suponiendo que nunca se va a llamar a fib(n) con un n negativo
# ¿Cuál de los siguientes códigos define fib(n) de manera correcta?

def fib(n):
    if n == 0 or n == 1:
        return 1
    return fib(n-1) + fib(n-2)

result = fib(5)
print(result)

print()
print("-------------------------------------------------------------------")
#--------------------------------------------------------------------
print()

# Pregunta 5 Tienes una lista con palabras:

a = ['casa', 'palabra', 'codigo', 'pala', 'fuente', 'fuerte']

# ¿Cuál de los siguientes códigos imprime, en este mismo orden,
# todas las palabras  de la lista a?

def imprimir_lista(lista):
    primer_elemento = lista.pop(0)
    print(primer_elemento)
    if len(lista) > 0:
        imprimir_lista(lista)

imprimir_lista(a)

print()
print("-------------------------------------------------------------------")
#--------------------------------------------------------------------
print()

# Pregunta 6 ¿Qué imprime el siguiente código?

def func(a):
    a += 24

    if a > 100:
        return 'a es muy grande'

    a = str(a)
    ultimo_digito = a[len(a) - 1]
    if ultimo_digito == 1 or ultimo_digito == 4:
        return 'ultimo_digito no puede ser 1 ni 4'

    return func(a)

print(func(33))

"""
    (x) El código levanta un error  
"""

print()
print("-------------------------------------------------------------------")
#--------------------------------------------------------------------
print()

# Pregunta 7 Tienes un torneo en formato de brackets donde 
# participan 8 equipos. La información de estos equipos viene en una 
# lista de tuplas, donde cada tupla contiene el nombre del equipo 
# (str) y su nivel de habilidad (int):

equipos = [
( 'Equipo 1 ', 5 ),
( 'Equipo 2 ', 7 ),
( 'Equipo 3 ', 8 ),
( 'Equipo 4 ', 2 ),
( 'Equipo 5 ', 9 ),
( 'Equipo 6 ', 1 ),
( 'Equipo 7 ', 3 ),
( 'Equipo 8 ', 4 )
]

# Los equipos van a jugar el torneo por orden de la lista. En el 
# ejemplo anterior, los partidos se jugarán en el siguiente orden:

# ┌──────────┬──────────┬──────────┬──────────┬──────────┬──────────┬──────────┬──────────┐
# │ Equipo 1 │ Equipo 2 │ Equipo 3 │ Equipo 4 │ Equipo 5 │ Equipo 6 │ Equipo 7 │ Equipo 8 │
# └──────────┴──────────┴──────────┴──────────┴──────────┴──────────┴──────────┴──────────┘
#      │     1    │          │     2    │          │     4    │          │     5    │            
#      │──────────│          │──────────│          │──────────│          │──────────│   
#            │          3          │                     │          6           │
#            │─────────────────────│                     │─────────────────────│
#                       │                     7                     │
#                       │───────────────────────────────────────────│


# Los partidos se juegan en el orden que muestra el diagrama, 
# primero el partido 1, luego el partido 2, luego el partido 3 y
# así. Además, un equipo gana un partido si su nivel de habilidad es
# mayor que el nivel de habilidad del adversario.

# ¿Cuál de los siguientes código imprime, en orden en que se
# jugaron, al ganador de cada uno de los 7 partidos?

def partido( equipos ):
    if len(equipos) == 1:
        return equipos[0]

    mitad = len(equipos)//2
    gan_izq = partido(equipos[:mitad])
    gan_der = partido(equipos[mitad:])
    nom1, hab1 = gan_izq
    nom2, hab2 = gan_der

    if hab1 > hab2:
        print('Gana: ' + nom1)
        return equipos[0]
    else:
        print('Gana: ' + nom2)
        return equipos[1]

partido(equipos)

print()
print("-------------------------------------------------------------------")
#--------------------------------------------------------------------
print()

# Pregunta 8 Tienes una lista con los nombres de 4 jugadores de un juego:

jugadores = [ 'Bob', 'Patricio', 'Calamardo', 'Arenita' ]

#El juego funciona de la siguiente forma, el primer jugador lanza 
# una moneda: si lanza cara sigue participando, si lanza sello es 
# eliminado. Luego, el segundo jugador lanza la moneda y así 
# sucesivamente. Luego de que juegue el cuarto jugador le toca de 
# nuevo al primero. Si un jugador es eliminado, entonces ya no
# deberá lanzar la moneda y se saltará su turno.

# La lista está ordenada por orden de jugadores. En el ejemplo, el 
# primer jugador sería Bob y el cuarto jugador Arenita. El juego 
# termina cuando solamente queda un jugador que no haya
# sido eliminado.

# Para simular el lanzamiento de la moneda se utiliza la función 
# randint(0,1), la cuál retorna al azar 0 ó 1. Si retorna 1 lo 
# consideraremos como cara y si retorna 0 lo consideraremos
# como sello.

# ¿Cuál de las siguientes funciones simula el juego y retorna 
# correctamente al ganador?

from random import randint

def juego(jugadores):
    if len(jugadores) == 1:
        return 'Ganador: ' + jugadores[0]
    jugador = jugadores.pop(0)
    if randint(0,1) == 1:
        jugadores.append(jugador)
    return juego(jugadores)

print( juego(jugadores) )

print()
print("-------------------------------------------------------------------")
#--------------------------------------------------------------------
print()

# Pregunta 9 Quieres imprimir todos los elementos de la siguiente lista:

lista = [0,0,0,1,1,1,2,2,2,3,3,3,4,4,4]

# Para practicar recursión, decides iterar sobre esta lista 
# utilizando recursión en lugar de un while o un for. ¿Cuál de los 
# siguientes códigos imprime en orden todos los elementos de la 
# lista de forma correcta?

def imprimir(lista, pos):
    if pos < len(lista):
        print(lista[pos])
        imprimir(lista, pos+1)

imprimir(lista, 0)

print()
print("-------------------------------------------------------------------")
#--------------------------------------------------------------------
print()

# Pregunta 10 La secuencia de número bonitos sigue una regla simple: 
# parte con 2 y 3, luego, cada valor es igual a la multiplicación de 
# los 2 anteriores menos 5. Por ejemplo, los primeros 8 valores son 
# los siguientes:

# 2, 3, 1, -2, -7, 9, -68, -617  , …

# Así, el número en la posición 0 de la secuencia es el 2, el 
# número en la posición 1 es el 3, el de la posición 2 es el 1 y así.

# Quieres definir la función bonitos(pos), la cual recibe como 
# parámetro con un entero con una posición y retorna el número que
# se encuentra en esa posición de la secuencia de números bonitos. 
# ¿Cuál de los siguientes códigos define bonitos(pos) correctamente?


def bonitos(pos):
    if pos == 0 or pos == 1:
        return pos + 2
    return bonitos(pos-1)*bonitos(pos-2) - 5

print(bonitos(0))  
print(bonitos(1))  
print(bonitos(2))  
print(bonitos(3))  
print(bonitos(4))  
print(bonitos(5))  
print(bonitos(6))  
print(bonitos(7))
