def generar_ticket(carrito, catalogo, total):
    print("\n==================================")
    print("        TICKET DE COMPRA          ")
    print("==================================")
    for item in carrito:
        id_prod, cantidad = item
        if id_prod in catalogo:
            nombre = catalogo[id_prod]["nombre"]
            precio = catalogo[id_prod]["precio"]
            sub = precio * cantidad
            print(f"{nombre} x{cantidad}: ${sub:.2f}")
    print("----------------------------------")
    print(f"TOTAL A PAGAR: ${total:.2f}")
    print("==================================\n")