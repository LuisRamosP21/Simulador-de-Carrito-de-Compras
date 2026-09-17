import catalogo
import carrito
import descuentos
import ticket

def mostrar_menu():
    print("\n=== SIMULADOR DE CARRITO DE COMPRAS ===")
    print("1. Ver catálogo de productos")
    print("2. Agregar producto al carrito")
    print("3. Ver carrito actual")
    print("4. Aplicar código de descuento")
    print("5. Generar ticket y finalizar compra")
    print("6. Salir")

def ejecutar():
    productos = catalogo.cargar_catalogo()
    mi_carrito = []
    descuento_aplicado = 0.0

    while True:
        mostrar_menu()
        opcion = input("\nSelecciona una opción (1-6): ").strip()

        if opcion == '1':
            catalogo.mostrar_catalogo(productos)
        elif opcion == '2':
            catalogo.mostrar_catalogo(productos)
            nombre_p = input("Nombre del producto a agregar: ").strip()
            cant = int(input("Cantidad: "))
            carrito.agregar_producto(mi_carrito, productos, nombre_p, cant)
        elif opcion == '3':
            carrito.mostrar_carrito(mi_carrito)
        elif opcion == '4':
            codigo = input("Ingresa el código de descuento: ").strip()
            descuento_aplicado = descuentos.validar_descuento(codigo)
        elif opcion == '5':
            if not mi_carrito:
                print("El carrito está vacío.")
            else:
                ticket.imprimir_ticket(mi_carrito, descuento_aplicado)
                break
        elif opcion == '6':
            print("¡Gracias por su visita!")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    ejecutar()