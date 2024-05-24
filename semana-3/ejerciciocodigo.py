# Pregunta 1 Tienes una lista de listas con información de vuelos:

vuelos = [ ['Origen', 'Destino', 'precio', 'asientos disponibles', 'Fecha'],
['Santiago', 'Puerto Montt', 35000, 30, '11 Enero 2023'],
['Santiago', 'Concepción', 30000, 40, '20 Febrero 2023'],
['Santiago', 'Puerto Montt', 28000, 2, '19 Enero 2023'],
['Santiago', 'Puerto Montt', 12000, 100, '20 Mayo 2023'],
['Antofagasta', 'Santiago', 27000, 14, '18 Abril 2023' ]
]

# Nota: El primer elemento de la lista es el header, y no contiene información de ningún vuelo. 
# El header se utiliza para representar qué información está en cada elemento de las listas.
# Debes definir una función vuelos_disponibles(vuelos, origen, destino, pasajeros), la cual recibe
# una lista con la información de todos los vuelos, dos strings, uno con la ciudad de origen y otro
# con la ciudad de destino, y por último un entero con el número de pasajeros con los que quieres viajar.
# La función deberá retornar una lista con todos los vuelos que vayan desde la ciudad de origen al destino
# que tengan suficientes asientos disponibles para todos los pasajeros.
# Por ejemplo, si se llama la función vuelos_disponibles(vuelos, 'Santiago', 'Puerto Montt', 5), con vuelos 
# la lista vuelos definida anteriormente, entonces la función deberá retornar:

[
['Origen', 'Destino', 'precio', 'asientos disponibles', 'Fecha'],
['Santiago', 'Puerto Montt', 35000, 30, '11 Enero 2023'],
['Santiago', 'Puerto Montt', 12000, 100, '20 Mayo 2023']
]

#Puedes asumir que el header va a ser siempre el mismo.

def vuelos_disponibles(vuelos, origen, destino, pasajeros):
    vuelos_disponibles = [vuelos[0]]

    for vuelo in vuelos[1:]:
        if vuelo[0] == origen and vuelo[1] == destino and vuelo[3] >= pasajeros:
            vuelos_disponibles.append(vuelo)

    return vuelos_disponibles

def mostrar_vuelos(vuelos):
    for vuelo in vuelos:
        print(', '.join(map(str, vuelo)))

vuelos = [
    ['Origen', 'Destino', 'precio', 'asientos disponibles', 'Fecha'],
    ['Santiago', 'Puerto Montt', 35000, 30, '11 Enero 2023'],
    ['Santiago', 'Concepción', 30000, 40, '20 Febrero 2023'],
    ['Santiago', 'Puerto Montt', 28000, 2, '19 Enero 2023'],
    ['Santiago', 'Puerto Montt', 12000, 100, '20 Mayo 2023'],
    ['Antofagasta', 'Santiago', 27000, 14, '18 Abril 2023']
]

origen = 'Santiago'
destino = 'Puerto Montt'
pasajeros = 5

vuelos_disponibles_result = vuelos_disponibles(vuelos, origen, destino, pasajeros)
mostrar_vuelos(vuelos_disponibles_result)
print()
print("----------------------------------------------------------------------------------")

#-----------------------------------------------------------------------------------------

print ()

# Pregunta 2 Tienes una lista de listas con información de alumnos, esta lista contiene siempre 
# como primer elemento un header que muestra donde se guarda cada información:


12345
lista = [
['Nombre', 'Numero alumno', 'Correo', 'Nota final'],
['Alicia', 16848, 'amartinez@gmail.com', 5.7],
['Marco', 19845, 'marenas@gmail.com', 4.8]
]

# Esta lista puede contener distinta información y en distinto orden, pero siempre va a tener al menos 
# el nombre y la nota final. Por ejemplo, la lista también se podría ver como:

lista = [
['Numero alumno', 'Nota final', 'Nombre', 'Color favorito'],
[16848, 5.7, 'Alicia', 'Rojo'],
[19845, 4.8, 'Marco', 'Verde'],
[19515, 6.2, 'Federico', 'Azul']
]


# Deberás definir una función notas_alumnos(lista), la cual recibe una lista de listas en el formato anterior. 
# La función deberá retornar una lista de tuplas, donde cada tupla contiene el nombre de un estudiante y su nota final. 
# Por ejemplo, para las listas anteriores tu función deberá retornar:

[('Alicia', 5.7), ('Marco', 4.8) ]

# y 

[('Alicia', 5.7), ('Marco', 4.8), ('Federico', 6.2) ]

# Nota que los alumnos en la lista a retornar están en el mismo orden que estaban en la lista inicial. 
# (primero Alicia, luego Marco y por último Federico)

def notas_alumnos(lista):
    header = lista[0]  # Obtener el encabezado
    nombre_index = header.index('Nombre')  # Índice del nombre
    nota_index = header.index('Nota final')  # Índice de la nota final

    resultados = []

    for alumno_info in lista[1:]:
        nombre = alumno_info[nombre_index]
        nota = alumno_info[nota_index]
        resultados.append((nombre, nota))

    return resultados

# Ejemplo de uso
lista1 = [
    ['Nombre', 'Numero alumno', 'Correo', 'Nota final'],
    ['Alicia', 16848, 'amartinez@gmail.com', 5.7],
    ['Marco', 19845, 'marenas@gmail.com', 4.8]
]

lista2 = [
    ['Numero alumno', 'Nota final', 'Nombre', 'Color favorito'],
    [16848, 5.7, 'Alicia', 'Rojo'],
    [19845, 4.8, 'Marco', 'Verde'],
    [19515, 6.2, 'Federico', 'Azul']
]

print(notas_alumnos(lista1))
print(notas_alumnos(lista2))
print()
print("----------------------------------------------------------------------------------")

#-----------------------------------------------------------------------------------------

print ()

# Pregunta 3 Tienes una lista con información de países, esta información es el id 
# (número que identifica al país), el nombre y la capital:

paises = [
[0, 'España', 'Madrid'],
[2, 'Alemania', 'Berlin'],
[1, 'Francia', 'Paris'],
[3, 'Italia', 'Roma']
]

# Además, tienes una lista con el índice de belleza de los países, según un comentarista 
# de un canal de viajes. Esta lista contiene el id de cada pais, junto a un float entre 0 y 1 
# con su índice de belleza (un país con un índice más alto se considera más bello que un país 
# con el índice más bajo) 

belleza = [
[2, 0.57],
[1, 0.81],
[3, 0.68],
[0, 0.62]
]

# Nota que el índice de belleza pertenece al país con el mismo id en la lista países.
# Define la función paises_bellos(paises, belleza), que recibe como parámetro la lista
# paises y la lista belleza. La función deberá retornar una lista de tuplas, donde cada tupla 
# contiene el nombre de un país y su índice de belleza. Además, las tuplas de esta lista deberán
# estar ordenadas de país más bellos a país menos bellos. Para las listas anteriores
# a función deberá retornar:

[('Francia', 0.81),
('Italia', 0.68),
('España', 0.62),
('Alemania', 0.57)
]

def paises_bellos(paises, belleza):
    resultados = [(pais[1], indice) for id_pais, indice in belleza for pais in paises if pais[0] == id_pais]

    resultados.sort(key=lambda x: x[1], reverse=True)

    return resultados

# Ejemplo de uso
paises = [
    [0, 'España', 'Madrid'],
    [2, 'Alemania', 'Berlin'],
    [1, 'Francia', 'Paris'],
    [3, 'Italia', 'Roma']
]

belleza = [
    [2, 0.57],
    [1, 0.81],
    [3, 0.68],
    [0, 0.62]
]

print(paises_bellos(paises, belleza))

