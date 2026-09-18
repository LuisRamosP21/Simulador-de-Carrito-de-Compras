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



REGLAS_DESCUENTO = {
    "porcentaje": 0.10,
    "3x2": 0.15,
    "sin_descuento": 0.0,
}


def aplicar_descuento(subtotal, tipo_descuento):
    """Aplica un descuento al subtotal según el tipo indicado."""
    if tipo_descuento not in REGLAS_DESCUENTO:
        print("Tipo de descuento no reconocido, no se aplica descuento.")
        return subtotal

    total = subtotal

    for clave, porcentaje in REGLAS_DESCUENTO.items():
        if clave == tipo_descuento:
            descuento = subtotal * porcentaje
            total = subtotal - descuento
            if descuento > 0:
                print(f"Descuento aplicado ({clave}): -${descuento:.2f}")

    return total
