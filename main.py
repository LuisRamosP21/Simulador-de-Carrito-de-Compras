# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 11:23:27 2026

@author: Luis
"""

import catalogo
import carrito
import descuentos
import ticket


def main():
    cat = catalogo.cargar_catalogo()
    mi_carrito = []

    while True:
        print("\n--- MENÚ SIMULADOR DE CARRITO ---")
        print("1. Ver catálogo")
        print("2. Agregar producto")
        print("3. Eliminar producto")
        print("4. Ver total y pagar")
        print("5. Salir")

        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            catalogo.mostrar_catalogo(cat)

        elif opcion == "2":
            id_producto = input("ID del producto (ej. p1, p2): ").strip().lower()
            try:
                cantidad = int(input("Cantidad: "))
            except ValueError:
                print("Cantidad inválida.")
                continue
            mi_carrito = carrito.agregar_producto(mi_carrito, cat, id_producto, cantidad)

        elif opcion == "3":
            id_producto = input("ID del producto a eliminar (ej. p1): ").strip().lower()
            mi_carrito = carrito.eliminar_producto(mi_carrito, id_producto)

        elif opcion == "4":
            if not mi_carrito:
                print("El carrito está vacío.")
                continue
            subtotal = carrito.calcular_subtotal(mi_carrito, cat)
            print(f"Subtotal: ${subtotal:.2f}")
            tipo = input("Tipo de descuento (estudiante/cupon15/combo_desayuno/sin_descuento): ").strip()
            total = descuentos.aplicar_descuento(subtotal, tipo)
            ticket.generar_ticket(mi_carrito, cat, total)
            mi_carrito = []

        elif opcion == "5":
            print("Gracias por tu compra. ¡Hasta pronto!")
            break

        else:
            print("Opción no válida, intenta de nuevo.")


if __name__ == "__main__":
    main()