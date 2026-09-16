# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 21:37:51 2026

@author: marie
"""
catalogo = {
    "p1": {"nombre":"Pan de muerto ", "precio":40, "categoria": "panaderia", "stock":50},
    "p2": {"nombre":"Dona de chocolate","precio":20, "categoria": "panaderia","stock":30 },
    "p3": {"nombre":"Dona de azucar", "precio": 16, "categoria": "panaderia", "stock":25},
    "p4": {"nombre": "Concha de chocolate", "precio": 25, "categoria": "panaderia", "stock":45},
    "p5": {"nombre": "Concha de vainilla", "precio": 25, "categoria": "panaderia","stock":40},
    "p6": {"nombre": "Oreja", "precio": 25, "categoria": "panaderia","stock":35},
    "p7": {"nombre": "polvoron", "precio": 25, "categoria": "panaderia", "stock":35},
    "p8": {"nombre": "Rol de canela", "precio":30, "categoria": "panaderia","stock":40},
    "p9": {"nombre": "Empanada de zarzamora", "precio":30, "categoria": "panaderia","stock":35 },
    "p10": {"nombre": "Empanada de fresa", "precio": 30, "categoria": "panaderia", "stock":40},
    "p11": {"nombre":"Chocolate con leche", "precio":40, "categoria": "bebida", "stock":40},
    "p12": {"nombre":"Arroz con leche","precio":45, "categoria": "bebida","stock":35},
    "p13": {"nombre":"Capuccino", "precio": 45, "categoria": "bebida", "stock":45},
    "p14": {"nombre": "Cafe de olla", "precio": 35, "categoria": "bebida", "stock":40},
    "p15": {"nombre": "Champurrado", "precio": 35, "categoria": "bebida", "stock":40},
    "p16": {"nombre": "Cafe americano", "precio": 35, "categoria": "bebida", "stock":40},
    }

def mostrar_catalogo():
    print("\n" + "="*40)
    print("MENÚ")
    print("\n PANADERÍA" )
    for produ, info in catalogo.items():
        if info.get("categoria") == "panaderia":
            print(f"  ({produ}) {info['nombre']} - ${info['precio']} - Disponible: {info['stock']}")
            
    print("\n BEBIDAS" )
    for produ, info in catalogo.items():
        if info.get("categoria") == "bebida":
            print(f"  ({produ}) {info['nombre']} - ${info['precio']} - Disponible: {info['stock']}")
    
print("-" * 40)
mostrar_catalogo()




