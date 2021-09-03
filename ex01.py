"""
Ejercicio 1

Realice un programa en Python para determinar cuanto se debe pagar por equis cantidad de ĺapices
considerando que si son 1000 o mas el costo es de 85 pesos; de lo contrario, el precio es de 90 pesos.

"""

lapices = int(input("Cantidad de lapices a comprar: "))
if lapices < 1000:
    costo_total = lapices * 90
else:
    costo_total = lapices * 85
print("El costo total de", lapices, "lapices es de", costo_total, "pesos")
