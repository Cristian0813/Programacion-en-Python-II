#-------------------------------------------------------------------------------------------

# Pregunta 1 Si tengo el siguiente código:

a = {"Perro", "Gato"}

# ¿Qué tipo de variable es a?

"""
    (x) set
"""
#-------------------------------------------------------------------------------------------

# Pregunta 2

a = set(["Jorge", "Alicia", "Carla", "Leonardo", "Alicia"])
print(len(a))
a.add("Bob")
print(len(a))
a.add("Bob")
print(len(a))

# ¿Qué imprime el código anterior?

"""   
    4
    5
    5
"""


#-------------------------------------------------------------------------------------------

# Pregunta 3 Tienes los siguientes sets:

a = {1, 2, 3, 4}
b = {4, 5, 6, 7}

# Quieres crear un nuevo set c que contenga todos los elementos de a
# y todos los elementos de b. ¿Cuál de los siguientes código hace lo
# pedido?

c = a | b
print(c)

#-------------------------------------------------------------------------------------------

#  Pregunta 4 Tienes una lista con todas las palabras de un poema:

poema = ['Mis', 'pasos', 'en', 'esta', 'calle', 'Resuenan', 'En', 'otra', 'calle', 'Donde', 'Oigo', 'mis', 'pasos', 'Pasar', 'en', 'esta', 'calle', 'Donde', 'Sólo', 'es', 'real', 'la', 'niebla']

# además, tiene un set con palabras prohibidas:

prohibidas = set( ['calle', 'mis', 'pasos'] )

# ¿Cuál de los siguientes códigos elimina todas las 
# palabras prohibidas del poema?

for palabra in prohibidas:
    if palabra in poema:
        poema.remove(palabra)
        
print(poema)

#-------------------------------------------------------------------------------------------

# Pregunta 5 Tienes una lista con números repetidos:

lista = [1,2,1,1,5,6,4,4,4,6,7,5,1,1,7,7,7,2,1,2]

# ¿Cuál de los siguientes códigos NO imprime la cantidad de números 
# distintos que hay en la lista?

for num in lista:
    veces = lista.count(num)
    for i in range(veces):
        lista.remove(num)
print(len(lista))


#-------------------------------------------------------------------------------------------

# Pregunta 6 Tus amigos deciden organizar una completada (una junta para comer hot dogs, o "completos"). Para evitar que todos traigan ketchup y nadie traiga salchichas, decides crear un programa en Python que verifique la variedad de ingredientes. Por cada uno de tus 4 amigos tienes un set con los ingredientes que trae:

a1 = set(['Pan', 'Salchichas', 'Mostaza', 'Ketchup'])
a2 = set(['Pan', 'Cebolla', 'Tomate', 'Chucrut'])
a3 = set(['Ketchup','Salchichas', 'Aji'])
a4 = set(['Chucrut', 'Pan'])

# Además tienes un set con tus ingredientes favoritos para los
# completos:

ing_favoritos = set(['Pan', 'Tomate', 'Salchichas', 'Chucrut', 'Mostaza', 'Ketchup', 'Mayonesa', 'Palta'])

# Quieres imprimir un set con todos los ingredientes de entre tus 
# ingredientes favoritos que no están entre los que traen tus amigos, 
# para comprarlos tú y poder comer tus completos bien completos. 
# ¿Cuál de los siguientes códigos hace correctamente lo pedido?

faltantes = ing_favoritos - (a1 | a2 | a3 | a4) 
print(faltantes)

#-------------------------------------------------------------------------------------------

# Pregunta 7 Tienes una lista con números repetidos:

lista = [1,2,1,1,5,6,4,4,4,6,7,5,1,1,7,7,7,2,1,2]

# Quieres imprimir un diccionario que tenga como llave (key) a cada uno
# de los números de la lista, y que su respectivo valor (value) sea
# la cantidad de veces que ese númeero se encuentra en la lista.
# Por ejemplo, para la lista anterior deberás imprimir el diccionario:

# {1: 6, 2: 3, 5: 2, 6: 2, 4: 3, 7: 4}

# ¿Cuál de los siguientes códigos imprime el diccionario correctamente?

d = dict()
for num in set(lista):
    d[num] = lista.count(num)
print(d)

#-------------------------------------------------------------------------------------------

# Pregunta 8 Tienes un diccionario con el nombre y la información
# personal de varios clientes de un banco:

clientes = {
    'Alicia': (28, 'Chile', 1200),
    'Bob': (45, 'Francia', 2000),
    'Carlos': (30, 'Argentina', 500),
    'David': (23, 'Inglaterra', 0)
}

# La información almacenada de cada cliente es una tupla con su edad,
# país de residencia y la deuda que tiene pendiente con el banco.

# ¿Cuál de los siguientes códigos imprime el nombre de todos los 
# clientes que tiene una deuda mayor a 1000?

for cliente in clientes:
    edad, residencia, deuda = cliente
    if deuda > 1000:
        print(cliente)

#-------------------------------------------------------------------------------------------

# Pregunta 9 Tienes un diccionario de amigos, donde cada key es el nombre de una persona y cada value es una lista con los nombres de todos quienes la persona considera sus amigos. Por ejemplo:

amigos = {'Bob': ['Patricio', 'Calamardo', 'Arenita', 'Don Cangrejo'],
    'Patricio': ['Bob', 'Calamardo'],
    'Arenita': ['Bob'],
    'Calamardo': [],
    'Don Cangrejo': ['Bob', 'Calamardo']
}

# Para cada persona quieres saber cuántas otras personas los consideran
# como amigos. En este ejemplo, hay 3 personas que consideran como
# amigo a Calamardo. El resultado debe ser un diccionario donde las
# keys son los nombres de las personas, y su value es la cantidad de
# personas que los consideran como amigos. Si utilizamos el diccionario
# inicial, el resultado debería ser el siguiente diccionario:

""" 
    {'Bob': 3,
    'Patricio': 1,
    'Arenita': 1,
    'Calamardo': 3,
    'Don Cangrejo': 1
    } 
"""

# ¿Cuál de los siguientes códigos NO imprime un diccionario como el
# solicitado?

otro = dict()
for nombre, lista_amigos in amigos.items():
    otro[nombre] = 0
    for amigo in lista_amigos:
        otro[amigo] += 1
print(otro)

#-------------------------------------------------------------------------------------------

# Pregunta 10 Tienes una lista con los géneros de los clientes de una empresa:

clientes = [
    "Male",
    "Male",
    "N/A",
    "Female",
    "N/A",
    "Female",
    "Male",
    "N/A",
    "Female",
    "Female"
]

resumen = [0,0,0]

# Tu lista solamente contiene los géneros "Male", "Female" y "N/A"
# para cuando la empresa no conoce el género. Quieres resumir esta
# información en una lista de tres enteros, donde el primer entero
# contiene el número de hombres en la lista clientes, el segundo el
# número de mujeres y el tercero el número de N/As.

# ¿Cuál de los siguientes código llena la lista resumen correctamente?

generos = {
    "Male": 0,
    "Female": 1,
    "N/A": 2
}
for cliente in clientes:
    resumen[generos[cliente]] += 1

print("Resumen de géneros:")
print(f"Male: {resumen[0]}")
print(f"Female: {resumen[1]}")
print(f"N/A: {resumen[2]}")