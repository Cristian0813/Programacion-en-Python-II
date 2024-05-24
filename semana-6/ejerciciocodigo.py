# Pregunta 1 Estás trabajando para una empresa de envío de
# encomiendas. Para eso debes terminar de escribir un código ya
# existente. El código tiene la siguiente clase ya implementada:

class Envio:
    def __init__(self, emisor, receptor):
        self.emisor = emisor
        self.receptor = receptor

    def enviar(self):
        pass

# El método enviar de la clase Envio se conecta directamente con la 
# empresa de encomiendas y se encarga del despacho. No sabes como 
# funciona este método, pero sabes que está implementado 
# correctamente y funciona.

# PARTE 1

# Deberás definir la clase Carta que herede de Envio. Esta clase tiene los siguientes métodos:

# __init__(self, emisor, receptor): método que hace como mínimo lo 
# mismo que el __init__ de Envio.

# poner_estampilla(self): este método no recibe parámetros, pero
# al llamarse coloca una estampilla en la carta

# enviar(self): este método deberá revisar que la carta tenga una 
# estampilla y luego enviar correctamente con el método definido en 
# Envio. Si la carta no tiene estampilla, entonces NO se deberá 
# enviar. Finalmente, la función deberá retornar True si se envia la 
# Carta y False en caso contrario.

class Carta(Envio):
    def __init__(self, emisor, receptor):
        super().__init__(emisor, receptor)
        self.estampilla = False

    def poner_estampilla(self):
        self.estampilla = True

    def enviar(self):
        if self.estampilla:
            super().enviar()
            print("Carta enviada correctamente!")
            return True
        else:
            print("No se puede enviar la carta porque no tiene estampilla.")
            return False

# Ejemplo de uso
carta1 = Carta("Juan", "María")
carta2 = Carta("Pedro", "Ana")

# Enviar carta con estampilla
carta1.poner_estampilla()
carta1.enviar()

# Enviar carta sin estampilla
carta2.enviar()

print()
print("-------------------------------------------------------------------")
#--------------------------------------------------------------------
print()

# Pregunta 2 Estás trabajando para una empresa de envío de 
# encomiendas, para eso debes terminar de escribir un código ya 
# existente, el código tiene la siguiente clase ya implementada:

class Envio:
    def __init__(self, emisor, receptor):
        self.emisor = emisor
        self.receptor = receptor

    def enviar(self):
        pass

# El método enviar de la clase Envio se conecta directamente con la # empresa de encomiendas y se encarga del despacho. No sabes como 
# funciona este método, pero sabes que está implementado 
# correctamente y funciona.

# PARTE 2

# Deberás definir la clase Paquete que herede de Envio. Esta 
# clase tiene los siguientes métodos:

# __init__(self, emisor, receptor, max_volumen): método que deberá 
# hacer lo mismo que el __init__ de envío, además de guardar 
# max_volumen. Cuando se crea el paquete este está
# inicialmente abierto.

# agregar_producto(self, peso, volumen): este método se llama cuando 
# se quiere agregar un producto al paquete. Este método recibe como 
# parámetros el peso y el volumen que tiene el producto a agregar a
# la caja. Si la caja está cerrada, entonces la caja se deberá
# abrir y agregar el producto.

# cerrar(self): método que no recibe parámetros. Este método se 
# llama cuando se quiere cerrar el paquete. El paquete se deberá 
# cerrar solamente si el volumen de todos los productos dentro del 
# paquete es menos que el volumen máximo de la caja, en
# caso contrario la caja NO se deberá cerrar.

# enviar(self): método que no recibe parámetros. Este método se 
# llama cuando se quiere enviar el paquete. El método deberá enviar
# el paquete utilizando el método enviar de Envio solamente si el paquete está cerrado y el peso de todos los productos dentro del
# paquete es menor o igual a 30. En caso contrario NO se deberá
# enviar el  paquete. Finalmente, la función deberá retornar True si
# se envia el paquete y False en caso contrario.

class Paquete(Envio):
    def __init__(self, emisor, receptor, max_volumen):
        super().__init__(emisor, receptor)
        self.max_volumen = max_volumen
        self.productos = []
        self.cerrado = False

    def agregar_producto(self, peso, volumen):
        if not self.cerrado:
            self.productos.append((peso, volumen))
        else:
            self.abrir()
            self.productos.append((peso, volumen))

    def cerrar(self):
        if sum(volumen for _, volumen in self.productos) <= self.max_volumen:
            self.cerrado = True
        else:
            self.cerrado = False

    def enviar(self):
        if self.cerrado and sum(peso for peso, _ in self.productos) <= 30:
            super().enviar()
            print(f"{self.emisor} ha enviado Paquete a {self.receptor}")
            return True
        else:
            return False

    def abrir(self):
        self.cerrado = False

# Ejemplo de uso
paquete1 = Paquete("Tienda Online", "Juan", 10)
paquete1.agregar_producto(1.5, 0.5)  # Producto 1
paquete1.agregar_producto(2.0, 1.0)  # Producto 2

paquete1.cerrar()  # Cerrar paquete
paquete1.agregar_producto(3.0, 2.0)  # Intento agregar producto después de cerrar
paquete1.abrir()  # Abrir paquete
paquete1.agregar_producto(3.0, 2.0)  # Agregar producto después de abrir
paquete1.cerrar()  # Cerrar paquete
paquete1.enviar()  # Enviar paquete
print()
print("-------------------------------------------------------------------")
#--------------------------------------------------------------------
print()

# Pregunta 3 La empresa lleva un par de semanas funcionando con tu 
# clase Paquete definida en la pregunta anterior, sin embargo ahora 
# que ya la probaron deciden hacerle un par de cambios para # adaptarse a nuevas necesidades.

# La empresa tiene una clase Paquete la cual cumple todas
# las condiciones de la pregunta anterior.

# Para esta parte deberás definir la clase PaqueteMejorado, la cual
# hereda de Paquete y tiene los siguientes cambios:

# Un PaqueteMejorado no se deberá enviar si su emisor y su receptor 
# son la misma persona. Además, una misma instancia de 
# PaqueteMejorado solo se podrá enviar una vez; si se intenta enviar # una segunda vez, entonces NO se deberá realizar el segundo envio.

# NOTA: No es necesario que redefinas la clase Paquete, puedes 
# suponer que ya está definida (de manera equivalente a como Envio 
# ya estaba definida para ambas preguntas anteriores)

class PaqueteMejorado(Paquete):
    def __init__(self, emisor, receptor, max_volumen):
        super().__init__(emisor, receptor, max_volumen)
        self.enviado = False

    def enviar(self):
        if not self.enviado:
            if self.emisor != self.receptor:
                super().enviar()
                print("El paquete ha sido enviado.")
                self.enviado = True
                return True
            else:
                print("El emisor y el receptor son la misma persona. No se puede enviar el paquete.")
                return False
        else:
            print("Este paquete ya ha sido enviado. No se puede enviar nuevamente.")
            return False

# Ejemplo de uso
paquete1 = PaqueteMejorado("Tienda Online", "Juan", 10)

paquete1.agregar_producto(1.5, 0.5)  # Producto 1
paquete1.agregar_producto(2.0, 1.0)  # Producto 2

paquete1.cerrar()  # Cerrar paquete

paquete1.enviar()  # Enviar paquete

paquete1.enviar()  # Intentar enviar de nuevo