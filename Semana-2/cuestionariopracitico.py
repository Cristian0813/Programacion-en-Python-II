
# Pregunta 1 Tienes una lista de enteros ordenados:

lista = [1, 2, 4, 5, 6, 7, 8, 9]

# Luego de crear la lista te das cuenta que se te olvidó agregar el 3, 
# ¿Cuál de los siguientes códigos agrega correctamente el 3 en la posición correcta?

lista.insert(2,3)
print(lista)
print()
print("-----------------------------------------------------------------------------------------")
print()

#-----------------------------------------------------------------------------------------------------

# Pregunta 2 Tienes una lista de enteros semi-ordenados:

lista = [1, 2, 7, 4, 5, 6, 3, 8, 9]

# Luego de crear la lista te das cuenta de que pusiste el 7 donde debía 
# ir el 3 y el 3 donde debía ir el 7 
# ¿Cuál de los siguientes códigos arregla la lista para que quede ordenada?

lista[2] = 3
lista[6] = 7
print(lista)
print()
print("-----------------------------------------------------------------------------------------")
print()

#-----------------------------------------------------------------------------------------------------

# Pregunta 3 Tienes la siguiente lista con nombres de clientes y sus años de nacimiento.

lista = ['Alicia', 1998, 'Bob', 1990, 'Carlos', 1986, 'David', 2001]
# Quieres imprimir el nombre de cada cliente seguido de su año de nacimiento. 
# Por ejemplo, para la lista anterior quieres imprimir:

# Alicia 1998
# Bob 1990
# Carlos 1986
# David 2001

# ¿Cuál de los siguientes códigos imprime correctamente lo pedido?

for i in range(0,len(lista),2):
    nombre = lista[i]
    nacimiento = str(lista[i+1])
    print(nombre, nacimiento)
print()
print("-----------------------------------------------------------------------------------------")
print()

#-----------------------------------------------------------------------------------------------------

# Pregunta 4 Tienes la siguiente lista con nombres de clientes:

lista = ['Alicia', 'Bob', 'Carlos', 'David']

# Quieres imprimir el nombre de los clientes de atrás hacía adelante. 
# Por ejemplo, para la lista anterior deberás imprimir:

# David
# Carlos
# Bob
# Alicia

# ¿Cuál de los siguientes códigos imprime correctamente lo pedido?

while len(lista) > 0:
    ultimo_cliente = len(lista) - 1
    cliente = lista.pop(ultimo_cliente)
    print(cliente)
print()
print("-----------------------------------------------------------------------------------------")
print()

#-----------------------------------------------------------------------------------------------------

# Pregunta 5 Tienes las siguientes listas con el nombre de dueños y los nombres de sus mascotas.

d = ['Alicia', 'Bob', 'Carlos', 'David']    # lista de dueños
m = ['Pelusa', 'Luke', 'Mickey', 'Madonna'] # lista de mascotas

# El dueño en la posición 0 tiene la mascota en la posición 0, 
# el dueño en la posición 1 tiene la mascota en la posición 1 y así. 
# Quieres imprimir el nombre de cada dueño seguido del nombre de su mascota. 
#Por ejemplo, para las listas anteriores quieres imprimir:

# Alicia Pelusa
# Bob Luke
# Carlos Mickey
# David Madonna

# ¿Cuál de los siguientes código imprime correctamente lo pedido?

for i in range(len(d)):
    print(d[i], m[i])
print()
print("-----------------------------------------------------------------------------------------")
print()

#-----------------------------------------------------------------------------------------------------

# Pregunta 6 Tienes una lista con datos de una estación meteorológica, esta contiene los strings 'soleado', 'nublado' o 'lluvia'. Siempre después de lluvia viene un float con la cantidad de milímetros de agua que cayeron durante la llovizna. Un ejemplo de esta lista es:

lista = ['soleado', 'nublado', 'soleado', 'lluvia', 2.4, 'lluvia', 0.1, 'nublado', 'lluvia', 0.8]

# ¿Cuál de los siguientes códigos imprime la suma total de milímetros 
# de agua que cayeron?

suma = 0
for i in lista:
    if i not in ['soleado','nublado','lluvia']:
        suma += i

print(suma)
print()
print("-----------------------------------------------------------------------------------------")
print()

#-----------------------------------------------------------------------------------------------------

# Pregunta 7 Tienes la siguiente lista de listas:

lista = [['A1', 'B1', 'C1', 'D1'],
         ['A2', 'B2', 'C2', 'D2'],
         ['A3', 'B7', 'C3', 'D3'],
         ['A4', 'B4', 'C4', 'D4']
]

# Luego de crearla te das cuenta que en lugar de poner B3 pusiste B7. 
# ¿Cuál de los siguientes códigos arreglan la lista anterior?

lista[2][1] = 'B3'
print(lista)
print()
print("-----------------------------------------------------------------------------------------")
print()

#-----------------------------------------------------------------------------------------------------


# Pregunta 8 Acaban de terminar las votaciones presidenciales y 
# decides crear un programa en Python para contar los votos. 
# Tienes una lista de listas con el siguiente formato:

votos = [['Alicia', 35],
         ['Bob', 42],
         ['Carlos', 29],
         ['David', 33]
]
# Cada elemento de esta lista es una lista con 2 valores: 
# el nombre de un candidato y la cantidad de votos que recibió. 
# ¿Cuál de los siguientes códigos imprime correctamente el nombre 
# del candidato que recibió la mayor cantidad de votos?

mejor = ['', 0]
for candidato in votos:
    if candidato[1] > mejor[1]:
        mejor = candidato
print(mejor[0])
print()
print("-----------------------------------------------------------------------------------------")
print()

#-----------------------------------------------------------------------------------------------------

# Pregunta 9 Tienes la siguiente lista de lista con números:

lista = [[-1, 2, -5, 40],
         [9, 65, -6, -34],
         [0, -4, 9, 2]
        ]

# Tu jefe te acaba de mencionar que los datos deben tener como valor mínimo el 0. 
# ¿Cuál de los siguientes códigos reemplaza todos los valores negativos 
# en la lista por ceros?

fils = len(lista)
cols = len(lista[0])
for i in range( fils ):
    for k in range( cols ):
        if lista[i][k] < 0:
            lista[i][k] = 0

print("\nLista modificada:")
for i in range(fils):
    for j in range(cols):
        print(f"{lista[i][j]:3}", end=" ")
    print()
print()
print("-----------------------------------------------------------------------------------------")
print()

#-----------------------------------------------------------------------------------------------------

# Pregunta 10 Tus amigos deciden organizar una completada 
# (una reunión para comer hot dogs). Para evitar que todos traigan 
# ketchup y nadie traiga salchichas, decides crear un programa en Python 
# que verifique la variedad de ingredientes. Tienes una lista de listas 
# con los ingredientes que tiene cada uno de tus amigos.

ingredientes_amigos = [
    ['Pan', 'Salchichas', 'Mostaza', 'Ketchup'], #ingr. amigo 1
    ['Pan', 'Tomate', 'Chucrut'], #ingr. amigo 2
    ['Ketchup','Salchichas'], #ingr. amigo 3
    ['Chucrut', 'Pan'] #ingr. amigo 4
]

# Además tienes una lista con tus ingredientes favoritos para los completos:

ingredientes_favoritos = ['Pan', 'Tomate', 'Salchichas', 'Chucrut', 'Mostaza', 'Ketchup', 'Mayonesa', 'Palta']  

# Quieres imprimir una lista con todos los ingredientes de entre tus 
# ingredientes favoritos que no están entre los que traen tus amigos, 
# para comprarlos tú y poder comer tus completos bien completos. 
# ¿Cuál de los siguientes códigos hace correctamente lo pedido?

for amigo in ingredientes_amigos:
    for ingrediente in amigo:
        if ingrediente in ingredientes_favoritos:
            ingredientes_favoritos.remove(ingrediente)
print(ingredientes_favoritos)
