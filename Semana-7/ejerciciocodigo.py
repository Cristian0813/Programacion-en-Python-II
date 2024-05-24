# Pregunta 1 Tienes una lista de listas. Cada lista interior contiene listas o strings. 
# Por ejemplo, la lista se podría ver de la siguiente forma:

lista = [
          [['a'], ['b', 'c']],
          ['d', ['e']]
]

# Deberás definir la función recursiva en_orden(lista, ordenada), la cuál recibe como
# parámetro una lista en el formato anterior y una lista vacía. La función deberá llenar
# la lista ordenada de la siguiente manera:

# Primero se debe agregar (append) a ordenada , la lista recibida, y luego deben agregarse
# a continuación cada una de las listas dentro de lista.

# POR EJEMPLO:

def en_orden(lista, ordenada):
    lista =  [['a'], [['b'], 'c']]
    ordenada = []
    en_orden(lista, ordenada)
    for x in ordenada:
        print(x)

# Deberá imprimir:

# [['a'], [['b'], 'c']]
# ['a']
# [['b'], 'c']
# ['b']

# POR EJEMPLO: 

def en_orden(lista, ordenada):
    lista = [
            [['a'], ['b', 'c']],
            ['d', ['e']],
            'f',
            ['g', 'h']
    ]

    ordenada = []
    en_orden(lista, ordenada)
    for x in ordenada:
        print(x)

# Deberá imprimir:

# [[['a'], ['b', 'c']], ['d', ['e']], 'f', ['g', 'h']]
# [['a'], ['b', 'c']]
# ['a']
# ['b', 'c']
# ['d', ['e']]
# ['e']
# ['g', 'h']

# POR EJEMPLO: 

def en_orden(lista, ordenada):

    lista = [
            ['f', 'g', 'h', 'i'],
            [[[[['j']]]]]
    ]

    ordenada = []
    en_orden(lista, ordenada)
    for x in ordenada:
        print(x)

# deberá imprimir:

# [['f', 'g', 'h', 'i'], [[[[['j']]]]]]
# ['f', 'g', 'h', 'i']
# [[[[['j']]]]]
# [[[['j']]]]
# [[['j']]]
# [['j']]
# ['j']

# AYUDA: La instrucción type(x) retorna el tipo de la variable x. Por ejemplo, para saber si una
# variable es del tipo str, puedes hacer la comparación type(x) == str. Lo mismo se puede hacer con el tipo list.

def en_orden(lista, ordenada):

    ordenada.append(lista)  # Add the list directly
    for elem in lista:
        if isinstance(elem, list):  # If elem is a list, recurse
            en_orden(elem, ordenada)
        else:  # If elem is not a list, it's a string, so do nothing
            pass

my_list = [[1, 2, [3, 4]], "hello", [5, 6]]
ordered_list = []
en_orden(my_list, ordered_list)
print(f"Final ordered list: {ordered_list}")

print()
print("-------------------------------------------------------------------")
#--------------------------------------------------------------------
print()

# Pregunta 2 Está definida la siguiente clase Alcancia:

class Alcancia:
    def __init__(self, nombre, dinero, alcancia):
        self.nombre = nombre
        self.dinero = dinero
        self.siguiente_alcancia = alcancia

#Cada alcancía tiene un nombre que es un string que guarda una descripción del tipo de alcancía, 
# un entero dinero con la cantidad de dinero almacenado en la alcancía y una 
# alcancía siguiente_alcancia, la cuál es la siguiente alcancía de la cuál vas a 
# sacar dinero si se acaba el de la alcancía actual.

# Por ejemplo, si tienes las siguientes alcancías:

a1 = Alcancia('Chanchito de greda', 900, None)
a2 = Alcancia('Debajo del Colchón', 100, a1)

# Entonces si intentas quitar 300 de la alcancía a2 deberás quitar los 100 que le quedan 
# y luego 200 de la alcancía a1.

# Notar que la alcancía a1 no tiene una siguiente_alcancia (ya que siguiente_alcancia = None). 
# Puedes suponer que nunca se pedirá sacar más dinero del que contiene una alcancía 
# cuya siguiente alcancía sea None.

# Para este ejercicio deberás definir la función recursiva sacar_dinero(alcancia, monto). 
# La función deberá restar el monto de la alcancía indicada. Si el dinero en la alcancía 
# no alcanza para el monto que se necesita, entonces deberás ir  a la siguiente alcancía 
# y sacar el resto. Deberás repetir lo anterior hasta haber restado tanto dinero
# entre todas las alcancías como el monto indicado.

# Nota: el corrector de este ejercicio siempre tendrá la alcancía a1 con 
# siguiente_alcancia = None, la alcancía a2 con siguiente_alcancía = a1, 
# la alcancía a3 con siguiente_alcancia = a2 y así.


class Alcancia:
    def __init__(self, nombre, dinero, alcancia):
        self.nombre = nombre
        self.dinero = dinero
        self.siguiente_alcancia = alcancia

def sacar_dinero(alcancia, monto):
    if monto <= alcancia.dinero:
        alcancia.dinero -= monto
        print(f"Se sacaron {monto} de la alcancía '{alcancia.nombre}'")
    else:
        print(f"Se sacaron {alcancia.dinero} de la alcancía '{alcancia.nombre}'")
        monto_restante = monto - alcancia.dinero
        alcancia.dinero = 0
        if alcancia.siguiente_alcancia is not None:
            sacar_dinero(alcancia.siguiente_alcancia, monto_restante)
        else:
            print("Se ha sacado todo el dinero necesario pero no hay más alcancías.")

# Ejemplo de uso
a1 = Alcancia('Chanchito de greda', 900, None)
a2 = Alcancia('Debajo del Colchón', 100, a1)

sacar_dinero(a2, 300)


print()
print("-------------------------------------------------------------------")
#--------------------------------------------------------------------
print()

# Pregunta 3 Tienes un árbol de descendencia de la siguiente forma:

#                    ( ) 
#                    ─┼─
#                     │
#                    / \
#              ┌─── Eligio ───┐
#              ↓              ↓ 
#             ( )            ( )
#             ─┼─            ─┼─
#              │              │ 
#             / \            / \
#      ┌─ Celestina ─┐      Julián
#      ↓             ↓ 
#     ( )           ( )       ( ) 
#     ─┼─           ─┼─       ─┼─
#      │             │         │
#     / \           / \       / \
#   Carmerla  ┌─ Rosendo ─┐  Fabián ──────────────────────────────┐
#             ↓           ↓         ↓         ↓         ↓         ↓  
#            ( )         ( )       ( )       ( )       ( )       ( )
#            ─┼─         ─┼─       ─┼─       ─┼─       ─┼─       ─┼─
#             │           │         │         │         │         │ 
#            / \         / \       / \       / \       / \       / \
#           José     Anastacia   Berto     Fausto     Abel     Florina


# En este árbol Celestina y Julián son hijos de Eligio. Carmela y Rosendo
# son hijos de Celestina; y Fabián es hijo de Julián. Por último, José y
# Anastacia son hijos de Rosendo; y Berto, Fausto, Abel y Florina son hijos
# de Fabián. Carmela no tuvo descendencia.

# La información del árbol fue guardada por generación en una tupla con el siguiente formato:

# descendencia = ('Eligio', [
#                         ('Celestina', [
#                                 ('Carmela', []),
#                                 ('Rosendo', [
#                                         ('José', []),
#                                         ('Anastacia', [])
#                                 ])
#                         ]),
#                         ('Julián', [
#                                 ('Fabián', [
#                                         ('Berto', []),
#                                         ('Fausto', []),
#                                         ('Abel', []),
#                                         ('Florina', [])
#                                 ]),
#                         ])
# ])

# Esta tupla guarda la información de cada persona en dos elementos.
# El primero es un string con el nombre de la persona y el segundo es
# una lista de tuplas con todos sus hijos.

# Define una función encontrar_padres(arbol, nombre) la cual recibe como
# parámetros un árbol de descendencia y un nombre. La función deberá retornar
# una lista con todos los padres de nombre en orden de ascendencia. Si nombre
# no está en el arbol deberá retornar False.

# Algunos casos basados en el árbol de ejemplo:
# encontrar_padres(descendencia,'Fausto')
# deberá retornar: ['Fausto', 'Fabián', 'Julián', 'Eligio']
# ya que Fabián es el padre de Fausto, Julián es el padre de Fabián y Eligio es el padre de Julián.
# encontrar_padres(descendencia,'Celestina')
# deberá retornar: ['Celestina', 'Eligio']
# encontrar_padres(descendencia,'Jorge')
# deberá retornar: False


# Recomendamos fuertemente pensar de forma RECURSIVA este ejercicio en lugar de forma iterativa.

def encontrar_padres(arbol, nombre):
    if arbol[0] == nombre:
        return [nombre]
    for hijo in arbol[1]:
        resultado = encontrar_padres(hijo, nombre)
        if resultado:
            return resultado + [arbol[0]]
    return False

# Ejemplo de uso:
descendencia = ('Eligio', [
                        ('Celestina', [
                                ('Carmela', []),
                                ('Rosendo', [
                                        ('José', []),
                                        ('Anastacia', [])
                                ])
                        ]),
                        ('Julián', [
                                ('Fabián', [
                                        ('Berto', []),
                                        ('Fausto', []),
                                        ('Abel', []),
                                        ('Florina', [])
                                ])
                        ])
                ])

print(encontrar_padres(descendencia, 'Fausto'))
print(encontrar_padres(descendencia, 'Celestina'))
print(encontrar_padres(descendencia, 'Jorge'))

