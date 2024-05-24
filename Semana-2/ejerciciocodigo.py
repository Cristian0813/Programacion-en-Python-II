#  Pregunta 1 Tienes una lista de enteros ordenados de menor a mayor, por ejemplo:


lista = [-40, -1, 1, 5, 16, 72, 100]

# Deberás definir la función agregar_entero(lista, entero), 
# la cual recibe como parámetro una lista en el formato anterior y un entero cualquiera. 
# La función deberá agregar el entero en la posición correcta de la lista y luego retornar 
# la lista. Por ejemplo, si se llama la función: agregar_entero(L, 13), siendo L la lista anterior, 
# entonces deberás retornar la lista:

# [-40, -1, 1, 5, 13, 16, 72, 100]

def agregar_entero(lista, entero):
    i = 0
    while i < len(lista) and lista[i] <entero:
        i+=1
    lista.insert(i, entero)
    return lista

resultado = agregar_entero (lista, 13)
print(resultado)
print()
print("-----------------------------------------------------------------------------------------")
print()

#-----------------------------------------------------------------------------------------------------

# Pregunta 2 Tienes una lista de enteros repetidos:

lista = [1,4,6,2,4,3,1,1,3,5,6,7,3,4,5,5,5,3,3,2,1,2,1,1,1,2,6,6]

# Deberás definir la función max_repetido(lista), la cual recibe como parámetro una lista 
# en el formato anterior. La función deberá retornar el número de veces que se repite el 
# entero que se repite más veces dentro de la lista. En el ejemplo anterior, el entero que más se 
# repite es el 1, el cual se repite 7 veces, por lo que tu función deberá retornar 7.

def max_repetido(lista):
    contenor = {}
    for entero in lista:
        if entero in contenor:
            contenor[entero] += 1
        else:
            contenor[entero] = 1
    max_ocurrente = max(contenor.values())
    return max_ocurrente

resultado = max_repetido(lista)
print(resultado)
print()
print("-----------------------------------------------------------------------------------------")
print()

#-----------------------------------------------------------------------------------------------------

# Pregunta 3 Tienes una lista con los nombres y apellidos de estudiantes de un curso, 
# ordenados alfabéticamente por apellido y luego por nombre:

estudiantes = [
'Mario Avedaño',
'Policarpo Avedaño',
'Juan Bodoque',
'Juanin Harry',
'Mario Hugo',
'Dylan Manguera',
'Eusebio Manguera'
]

# Deberás definir la función agregar_estudiante(lista, estudiante), la cual recibe como parámetro 
# una lista en el formato anterior y el nombre de un nuevo estudiante. 
# La función deberá agregar al estudiante en la posición correcta (ordenado alfabéticamente por apellido y nombre) 
# de la lista y luego retornar la lista. Por ejemplo, si en la lista anterior se agrega el estudiante 
# 'Eliza Manguera', entonces tu función deberá retornar:
# ['Mario Avedaño',
# 'Policarpo Avedaño',
# 'Juan Bodoque',
# 'Juanin Harry',
# 'Mario Hugo',
# 'Dylan Manguera',
# 'Eliza Manguera',
# 'Eusebio Manguera'
# ]

def agregar_estudiante(lista, estudiante):
    if estudiante.strip():
        lista.append(estudiante)
        lista.sort(key=lambda x: (x.split()[1], x.split()[0]))
    return lista

agregar_estudiante(estudiantes, "Eliza Manguera")
print(estudiantes)