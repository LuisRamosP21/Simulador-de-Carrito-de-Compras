# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 19:25:03 2026

@author: Leo
"""

def agregar_producto(carrito, catalogo, id_producto, cantidad):
    #Producto no encontrado
    if id_producto not in catalogo:
        print("El producto no existe en el catálogo.")
        return carrito

    stock_disponible = catalogo[id_producto]["stock"]

    #Buscar si ya está en el carrito
    for i in range(len(carrito)):
        if carrito[i][0] == id_producto:
            nueva_cantidad = carrito[i][1] + cantidad
            
            #Stock insuficiente
            if nueva_cantidad > stock_disponible:
                print("La cantidad total supera el stock disponible.")
                return carrito
                
            carrito[i] = (id_producto, nueva_cantidad)
            print(f"Se actualizó la cantidad de '{catalogo[id_producto]['nombre'].strip()}'.")
            return carrito

    # Stock insuficiente en nuevo producto
    if cantidad > stock_disponible:
        print(f"Error: Solo hay {stock_disponible} piezas disponibles.")
        return carrito

    carrito.append((id_producto, cantidad))
    print("¡Se ha agregado correctamente al carrito!")
    return carrito


def eliminar_producto(carrito, id_producto):
    for i in range(len(carrito)):
        if carrito[i][0] == id_producto:
            carrito.pop(i)
            print(f"'{id_producto}' ha sido eliminado del carrito.")
            return carrito

    print("El producto no se encuentra en el carrito.")
    return carrito


def modificar_producto(carrito, catalogo, id_producto, nueva_cantidad):
    if nueva_cantidad <= 0:
        return eliminar_producto(carrito, id_producto)

    if id_producto not in catalogo:
        print("El producto no existe en el catálogo.")
        return carrito

    stock_disponible = catalogo[id_producto]["stock"]
    if nueva_cantidad > stock_disponible:
        print("La cantidad solicitada excede el stock.")
        return carrito

    for i in range(len(carrito)):
        if carrito[i][0] == id_producto:
            carrito[i] = (id_producto, nueva_cantidad)
            print("Stock actualizado")
            return carrito

    print("El producto no está en el carrito para modificar.")
    return carrito

def calcular_subtotal(carrito, catalogo):
    subtotal = 0
    for item in carrito:
        id_prod, cantidad = item
        if id_prod in catalogo:
            subtotal += catalogo[id_prod]["precio"] * cantidad
    return subtotal
