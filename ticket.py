import random
from datetime import date

def generar_ticket(carrito: list, catalogo: dict, total: float) -> tuple:
    """
    Despliega el resumen de compra en consola y retorna una tupla inmutable.
    """
    if len(carrito) == 0:  
        print("Carrito vacío. No se puede imprimir ticket.")  
        return None

    folio = f"F{random.randint(100, 999)}"
    fecha_hoy = str(date.today())

    print("\n" + "=" * 38)
    print("        PANADERÍA - TICKET DE VENTA      ")
    print("=" * 38)
    print(f"Folio: {folio} | Fecha: {fecha_hoy}")
    print("-" * 38)

    for item in carrito:
        id_prod = item[0]  
        cantidad = item[1]  
        nombre = catalogo[id_prod]["nombre"]  
        precio = catalogo[id_prod]["precio"]  
        importe = cantidad * precio  
        print(f"{cantidad}x {nombre:<16} ${precio:>5.2f} = ${importe:>6.2f}")

    print("-" * 38)
    print(f"TOTAL PAGADO: ${total:.2f}")
    print("=" * 38)
    print("      ¡Gracias por su compra!            \n")

    return (folio, fecha_hoy, total)