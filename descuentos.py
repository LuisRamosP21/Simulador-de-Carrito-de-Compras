# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 23:02:11 2026

@author: ARELY
"""
# -*- coding: utf-8 -*-
"""
Módulo: Cálculo de Subtotal y Aplicación de Descuentos
Integrante: Arely
"""

# Diccionario con reglas de descuento
reglas_descuento = {
    "estudiante": {"porcentaje": 0.20},   # 20% de descuento
    "cupon15": {"porcentaje": 0.15},
    "combo_desayuno": {"porcentaje": 0.20}
}


def calcular_subtotal(carrito, catalogo):
    """Calcula el costo acumulado de los productos en el carrito."""
    subtotal = 0.0
    for item in carrito:
        id_producto = item[0]
        cantidad = item[1]
        precio = catalogo[id_producto]["precio"]
        subtotal += precio * cantidad
    return subtotal


def aplicar_descuento(subtotal, tipo_descuento, carrito, catalogo):
    """Aplica promociones y cupones sobre el subtotal."""
    if tipo_descuento == "combo_desayuno":
        cant_pan = 0
        cant_bebida = 0

        for item in carrito:
            id_prod = item[0]
            cantidad = item[1]
            categoria = catalogo[id_prod].get("categoria", "").lower()

            if categoria == "pan":
                cant_pan += cantidad
            elif categoria == "bebida":
                cant_bebida += cantidad

        if cant_pan >= 4 and cant_bebida >= 2:
            porcentaje = reglas_descuento["combo_desayuno"]["porcentaje"]
            descuento = subtotal * porcentaje
            print(f"¡Combo aplicado! ({cant_pan} panes y {cant_bebida} bebidas). Ahorro: -${descuento:.2f}")
            return subtotal - descuento
        else:
            print("No cumples el combo (Requiere 4 panes y 2 bebidas).")
            return subtotal

    elif tipo_descuento in reglas_descuento:
        porcentaje = reglas_descuento[tipo_descuento]["porcentaje"]
        descuento = subtotal * porcentaje
        print(f"Descuento del {int(porcentaje * 100)}% aplicado.")
        return subtotal - descuento

    else:
        print("Cupón no válido.")
        return subtotal
