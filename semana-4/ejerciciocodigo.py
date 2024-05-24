# Pregunta 1 Cada vez que vas al supermercado pides que te manden la boleta al correo. Luego de ir un par de veces decides
# descargar todas tus boletas. La información de cada boleta viene en un diccionario con el siguiente formato:

"""
    {'fecha_compra' : '30-05-22',
    'precio' : 12000,
    'productos' : {
        'Leche' : 2,
        'Chocolate': 1,
        'Arroz': 5
        }
    }
"""

# Es decir, la boleta es un diccionario con las keys: fecha_compra, precio y productos.

# - fecha_compra, es un string con la fecha de la compra 
# - precio es un entero con el precio final de la compra
# - productos es un diccionario, donde la key tiene el nombre de un producto comprado y el value es un int con la cantidad comprada de ese producto.

# Como ejemplo, la compra anterior fue realizada el 30-05-22, el precio total de esta compra fue de 12000 y se compraron 2 unidades de leche,
# 1 de chocolate y 5 de arroz.

# Al descargar las boletas, el programa te retorna una lista con varios diccionarios en el formato anterior, por ejemplo,
# si has realizado tres compras, entonces el programa te podría retornar:

boletas = [{'fecha_compra' : '29-05-22',
'precio' : 12000,
'productos' : {'Chocolate': 1,
'Mantequilla': 1,
'Huevos': 12,
'Pan' : 1}
},
{'fecha_compra' : '31-05-22',
'precio' : 2400,
'productos' : {'Pan': 1, 'Leche' : 2}
},
{'fecha_compra' : '01-06-22',
'precio' : 3000,
'productos' : {'Mantequilla': 2, 'Azucar' : 1}
}
]

# Una vez descargada esta información decides crear un programa que te de un resumen de tus compras. 

# PARTE 1
# Para esta parte deberás definir la función precio_total(boletas), la cual recibe como parámetro una lista de boletas en el formato anterior.
# La función deberá retornar el precio total de todas tus compras.

def precio_total(boletas):
    
    precio_total = 0
    
    for boleta in boletas:
        precio_total += boleta['precio']
    return precio_total
precio_total_ejemplo = precio_total(boletas)
print(f"Precio total de compras: {precio_total_ejemplo}")

print()
print("-----------------------------------------------------------------------------------------------------------------")
#-----------------------------------------------------------------------------------------------------------------------
print()

# Pregunta 2 Cada vez que vas al supermercado pides que te manden la boleta al correo. Luego de ir un par de veces decides
# descargar todas tus boletas. La información de cada boleta viene en un diccionario con el siguiente formato:

"""
    {'fecha_compra' : '30-05-22',
    'precio' : 12000,
    'productos' : {
        'Leche' : 2,
        'Chocolate': 1,
        'Arroz': 5
        }
    }
"""

# Es decir, la boleta es un diccionario con las keys: fecha_compra, precio y productos.

# - fecha_compra, es un string con la fecha de la compra 
# - precio es un entero con el precio final de la compra
# - productos es un diccionario, donde la key tiene el nombre de un producto comprado y el value es un int con la cantidad comprada de ese producto.

# Como ejemplo, la compra anterior fue realizada el 30-05-22, el precio total de esta compra fue de 12000 y se compraron 2 unidades de leche,
# 1 de chocolate y 5 de arroz.

# Al descargar las boletas, el programa te retorna una lista con varios diccionarios en el formato anterior, por ejemplo, si has realizado
# tres compras, entonces el programa te podría retornar:

boletas = [{'fecha_compra' : '29-05-22',
'precio' : 12000,
'productos' : {'Chocolate': 1,
'Mantequilla': 1,
'Huevos': 12,
'Pan' : 1}
},
{'fecha_compra' : '31-05-22',
'precio' : 2400,
'productos' : {'Pan': 1, 'Leche' : 2}
},
{'fecha_compra' : '01-06-22',
'precio' : 3000,
'productos' : {'Mantequilla': 2, 'Azucar' : 1}
}
]

# Una vez descargada esta información decides crear un programa que te de un resumen de tus compras. 

# PARTE 2
# Para esta parte deberás definir la función precio_mes(boletas), la cual recibe como parámetro una lista de boletas en el formato anterior.
# La función deberá retornar un diccionario, donde las keys son un string mes-año donde se haya realizado al menos una compra y el value es
# el precio total de compras realizadas en ese mes. Para el ejemplo anterior, esta función deberá retornar:

def precio_mes(boletas):
  precio_por_mes = {}
  for boleta in boletas:
    fecha_compra = boleta["fecha_compra"]

    mes_año = fecha_compra.split("-")[1:]
    mes_año = "-".join(mes_año)

    precio_boleta = boleta["precio"]

    if mes_año not in precio_por_mes:
      precio_por_mes[mes_año] = precio_boleta
    else:
      precio_por_mes[mes_año] += precio_boleta

  return precio_por_mes

precio_por_mes_ejemplo = precio_mes(boletas)
print(f"Precio total de compras por mes-año: {precio_por_mes_ejemplo}")

print()
print("-----------------------------------------------------------------------------------------------------------------")
#-----------------------------------------------------------------------------------------------------------------------
print()

# Pregunta 3 Cada vez que vas al supermercado pides que te manden la boleta al correo. Luego de ir un par de veces decides descargar
# todas tus boletas. La información de cada boleta viene en un diccionario con el siguiente formato:

"""
    {'fecha_compra' : '30-05-22',
    'precio' : 12000,
    'productos' : {
        'Leche' : 2,
        'Chocolate': 1,
        'Arroz': 5
        }
    }
"""

# Es decir, la boleta es un diccionario con las keys: fecha_compra, precio y productos.

# - fecha_compra, es un string con la fecha de la compra 
# - precio es un entero con el precio final de la compra
# - productos es un diccionario, donde la key tiene el nombre de un producto comprado y el value es un int con la cantidad comprada de ese producto.

# Como ejemplo, la compra anterior fue realizada el 30-05-22, el precio total de esta compra fue de 12000 y se compraron 2 unidades de leche,
# 1 de chocolate y 5 de arroz.

# Al descargar las boletas, el programa te retorna una lista con varios diccionarios en el formato anterior, por ejemplo,
# si has realizado tres compras, entonces el programa te podría retornar:

boletas = [{'fecha_compra' : '29-05-22',
'precio' : 12000,
'productos' : {'Chocolate': 1,
'Mantequilla': 1,
'Huevos': 12,
'Pan' : 1}
},
{'fecha_compra' : '31-05-22',
'precio' : 2400,
'productos' : {'Pan': 1, 'Leche' : 2}
},
{'fecha_compra' : '01-06-22',
'precio' : 3000,
'productos' : {'Mantequilla': 2, 'Azucar' : 1}
}
]

# Una vez descargada esta información decides crear un programa que te de un resumen de tus compras. 

# PARTE 3
# Para esta parte deberás definir la función productos_frecuentes(boletas), la cuál recibe como parámetro una lista de boletas
# en el formato anterior. La función deberá retornar un set con aquellos productos que estén en al menos el 50% de las boletas, es decir,
# aquellos productos que se compraron en la mitad de todas las compras o más. Para el ejemplo anterior, este set deberá contener:

def productos_frecuentes(boletas):
    
    frecuencia_productos = {}
    total_boletas = len(boletas)
    
    for boleta in boletas:
        productos = boleta['productos']
        for producto in productos:
            if producto in frecuencia_productos:
                frecuencia_productos[producto] += 1
            else:
                frecuencia_productos[producto] = 1
    
    productos_frecuentes = {producto for producto, frecuencia in frecuencia_productos.items() if frecuencia >= total_boletas / 2}
    
    return productos_frecuentes

print(productos_frecuentes(boletas))