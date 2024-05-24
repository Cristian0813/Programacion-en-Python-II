# Pregunta 1 Tienes la siguiente tupla con números:

tupla = (1,2,3,5,6,7,8,9)

# Luego de crearla te das cuenta de que se te olvidó agregar al 4. 
# ¿Cuál de los siguientes códigos agrega el 4 en la posición correcta?

"""
    (x) No se puede
"""

# Pregunta 2 Tienes una tupla con información de la película Toy Story. Esta tupla contiene el título, año de estreno, la duración y una lista con las categorías a las que pertenece.

m1 = ('Toy Story', 1995, '01:21', ['animacion', 'comedia'])
# Luego de hablar con tu agente te recomienda que agregues a la lista 
# de categorías la categoría infantil. 
# ¿Cuál de los siguientes códigos agrega correctamente la categoría?

m1[3].append( 'infantil' )
print(m1)
print()
print("-------------------------------------------------------------")

#--------------------------------------------------------------------

print()

# Pregunta 3 Creaste la siguiente tupla con las notas que 
# te sacaste en un curso:

tupla = (2.0, 4.7, 6.8, 5.1)

# El profesor acaba de volver a corregir las notas y tu nota en la 
# primera evaluación subió de 2.0 a 3.2. Como sabes que las tuplas 
# no son mutables decides pasar todas tus notas a una lista y 
# reemplazar el 2.0 por el 3.2. ¿Cuál de los siguientes códigos hace 
# lo pedido correctamente? 

lista = []
for nota in tupla:
    lista.append(nota)
lista[0] = 3.2
print(lista)
print()
print("-------------------------------------------------------------")

#--------------------------------------------------------------------

print()

# Pregunta 4 Tienes la siguiente lista y tupla:

clientes = ['Alicia', 'Bob', 'Carlos', 'David']
clientes_nuevos = ('Eva', 'Fabricio', 'Gloria')

# Quieres agregar todos los clientes de la tupla 
# clientes_nuevos a la lista clientes 
# ¿Cuál de los siguientes códigos lo hace correctamente?

for cliente in clientes_nuevos:
    clientes.append(cliente)
print(lista)
print()
print("-------------------------------------------------------------")

#--------------------------------------------------------------------

print()

# Pregunta 5 Tienes el siguiente deque:

from collections import deque
deq = deque( (1,4,5,3,2) )

# ¿Cuál de los siguientes códigos imprime los números 
# del 1 al 5 en orden? (cada uno en una línea)

print( deq.count(1) )
print( deq.pop() )
print( deq.pop() )
print( deq.popleft() )
print( deq.popleft() )
print()
print("-------------------------------------------------------------")

#--------------------------------------------------------------------

print()

# Pregunta 6 Varios amigos te han recomendado series, y como no los 
# quieres decepcionar decides crear un programa en python donde ir 
# guardando todas las series que te recomiendan para luego ir viéndolas. Como buena persona, decides ver primero las series que te recomendaron antes y por último las que te recomendaron más recientemente. Si tus amigos te recomendaron 'You', 'Community' y 'Breaking Bad' en ese orden y solo has visto la primera, 
# ¿Cuál de los siguientes códigos modela correctamente este problema?

from collections import deque

series = deque()
series.append('You')
series.append('Community')
series.append('Breaking Bad')
series.popleft()

print(series)
print()
print("-------------------------------------------------------------")

#--------------------------------------------------------------------

print()

# Pregunta 7 Tienes un supermercado con 3 cajas registradoras. 
# Las filas en estas cajas están modeladas con deques, además estas 
# filas las tienes almacenadas en una tupla.

from collections import deque

fila1 = deque()
fila2 = deque()
fila3 = deque()
filas = ( fila1, fila2, fila3 )

# Además, sabes que para elegir al siguiente cliente de una fila 
# se utiliza popleft(). Para que los clientes esperen la menor cantidad 
# de tiempo en las filas decides crear la función 
# elegir_fila(filas, cliente), que recibe como parámetro una tupla con 
# las filas y un cliente. La función deberá encontrar la fila con menos 
# elementos y agregar al cliente al final de esa fila. 

# ¿Cuál de los siguientes códigos define elegir_fila(filas, cliente) 
# correctamente?

def elegir_fila(filas, cliente):
    mejor_fila = filas[0]
    for fila in filas:
        if len(fila) < len(mejor_fila):
            mejor_fila = fila
    mejor_fila.append( cliente )

cliente = "Juan"
elegir_fila(filas, cliente)

print("Fila 1:", fila1)
print("Fila 2:", fila2)
print("Fila 3:", fila3)
print()
print("-------------------------------------------------------------")

#--------------------------------------------------------------------

print()

#  Pregunta 8 Tienes el siguiente deque:

from collections import deque
deq = deque( (1,2,3,4,5) )

# Te gustaría invertirlo para que quede con los valores en orden de 
# mayor a menor (5,4,3,2,1) ¿Cuál de los siguientes códigos NO 
# invierte correctamente deq?

deq2 = deque()
for i in deq:
    deq2.append( i )
deq = deq2
print(deq)
print()
print("-------------------------------------------------------------")

#--------------------------------------------------------------------

print()

# Pregunta 9 Acaba de ocurrir un accidente y se debe evacuar a todos los 
# pasajeros. Para evacuar de forma ordenada creas las siguientes colas:

from collections import deque

pasajeros_prioritarios = deque()
pasajeros = deque()
tripulacion = deque()

# Estas colas se acaban de llenar con la información de todos los 
# pasajeros, quedando en la primera todos los pasajeros que tienen 
# prioridad al evacuar, luego los demás pasajeros y por último la 
# tripulación. Es tu deber como capitán vaciar estas colas en orden, 
# vaciando primero la cola de pasajeros_prioritarios, luego la de 
# pasajeros y por último la de tripulacion. Cada una de estas colas 
# la deberás vaciar por orden de llegada. Puedes asumir que las colas
# se llenaron utilizando append ¿Cuál de los siguientes códigos vacía
# las colas correctamente?

while len(pasajeros_prioritarios) > 0 and len(pasajeros) > 0 and len(tripulacion) > 0:
    pasajeros_prioritarios.popleft()
    pasajeros.popleft()
    tripulacion.popleft()

print(f"Procesando: {pasajeros_prioritarios} (prioritario), {pasajeros}, {tripulacion}")

print("\nFin del procesamiento.")

print()
print("-------------------------------------------------------------")

#--------------------------------------------------------------------

print()

# Pregunta 10 La función llenar_cola(cola) recibe como parámetro una 
# cola y la llena de varios elementos.

from collections import deque

cola = deque()
llenar_cola(cola)

# Luego de llamar la función notas que los elementos dentro de la cola 
# están al revés. ¿Cuál de los siguientes códigos invierte la cola 
# correctamente?


cola_aux = deque()
while len(cola)>0:
    elemento = cola.popleft()
    cola_aux.appendleft(elemento)
cola = cola_aux 
print(cola)