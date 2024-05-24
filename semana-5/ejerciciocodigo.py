# Pregunta 1Define la clase Planta, la cuál en su constructor recibe
# los parámetros: especie (str) y altura (int) y guarda la información
# en atributos con los mismos nombres. Tu código deberá ejecutarse
# correctamente con un código como el siguiente:

""" 
a = Planta('Washingtonia filifera', 15)
print(a.especie)
print(a.altura)
 """
# Si se ejecuta el código anterior,  deberá imprimir:
# Washingtonia filifera
# 15

class Planta:
    def __init__(self, especie, altura):
        self.especie = especie
        self.altura = altura

a = Planta('Washingtonia filifera', 15)
print(a.especie)
print(a.altura)

print()
print("-----------------------------------------------------------------------")
#-----------------------------------------------------------------------------
print()

# Pregunta 2 Estás digitalizando la información de tu restaurante.
# Para manejar la información del menú decides crear la clase Menu.
# La clase deberá recibir los parámetros: comidas (lista de strings)
# y precios (lista de ints del mismo largo que la lista comidas).
# Además, deberás definir el método __str__(self). Este método deberá
# retornar tantas líneas como comidas tenga el menú, donde cada línea
# deberá ser una comida seguida de dos puntos y su precio.
# Tu código deberá ejecutarse correctamente con un código como el
# siguiente:

""" 
comidas = ['Pato a la mostaza', 'Hamburguesa', 'Ensalada', 'Lasagna']
precios = [20000, 8000, 6000, 9000]
menu = Menu(comidas, precios)
 """
# print(menu)

# Si se ejecuta el código anterior, este deberá imprimir:

# Pato a la mostaza: 20000
# Hamburguesa: 8000
# Ensalada: 6000
# Lasagna: 9000

class Menu:
    def __init__(self, comidas: list, precios: list) -> None: 
        assert len(comidas) == len(precios), "comidas debe tener la misma longitud que precios para crear el Menú"
        self.comidas = comidas 
        self.precios = precios 

    def __str__(self) -> str:
        tex = []
        for (comida, precio) in zip(self.comidas, self.precios):
            tex.append(comida + ": " + str(precio))
        return "\n".join(tex)

comidas = ['Pato a la mostaza', 'Hamburguesa', 'Ensalada', 'Lasagna'] 
precios = [20000, 8000, 6000, 9000] 
menu = Menu(comidas, precios)
print(menu)

print()
print("-----------------------------------------------------------------------")
#-----------------------------------------------------------------------------
print()

# Pregunta 3 Estás programando un videojuego. Para facilitar el
# manejo de enemigos decides crear tu propia clase. Define la clase
# Enemigo, la cual en su constructor recibe los parámetros: nombre
# (str), vida (float) y fuerza_ataque (float); el constructor deberá
# guardar esa información en atributos con los mismos nombres.

# Además tu clase deberá tener los siguientes métodos:

# recibir_ataque(self, daño): este método deberá descontar daño de
# la vida del enemigo, considerando que la vida nunca puede
# ser menor a 0.

# atacar(self, otro): este método recibe como parámetro otro enemigo.
# El monstruo deberá hacer daño al monstruo recibido. El daño
# debe ser igual a su fuerza de ataque. Considerar que la vida nunca
# puede ser menor a 0.

# __str__(self): este método deberá retornar el nombre del monstruo
# seguido de un - y su vida actual.

# Tu código deberá ejecutarse correctamente con un código como el 
# siguiente:

""" a = Enemigo( 'Esqueleto', 8, 6 )
b = Enemigo( 'Zombie', 10, 5 )
print(a)
print(b)

a.recibir_ataque(5)
print(a)

a.atacar(b)
print(b)
 """
# Si se ejecuta el código anterior, este deberá imprimir:

# Esqueleto - 8
# Zombie - 10
# Esqueleto - 3
# Zombie - 4
# Zombie - 0

class Enemigo:
    def __init__(self, nombre, vida, fuerza_ataque):
        self.nombre = nombre
        self.vida = vida
        self.fuerza_ataque = fuerza_ataque

    def recibir_ataque(self, daño):
        self.vida = max(0, self.vida - daño)

    def atacar(self, otro):
        otro.recibir_ataque(self.fuerza_ataque)

    def __str__(self):
        return f"{self.nombre} - {self.vida}"

# Ejemplo de uso
a = Enemigo('Ladrón', 14, 3)
b = Enemigo('Kraken', 12, 6)

print(a)
print(b)

b.recibir_ataque(5)
a.atacar(b)
print(a)
print(b)

b.recibir_ataque(7)
b.atacar(a)
print(a)
print(b)

a.recibir_ataque(5)
b.atacar(a)
print(a)
print(b)

