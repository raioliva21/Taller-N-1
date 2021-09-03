"""
Ejercicio 7

El buen gordito” ofrece hamburguesas sencillas, dobles y triples, las cuales tienen un costo de $2000,
$2500 y $3000 respectivamente. La empresa acepta tarjetas de cr ́edito con un cargo de 5 % sobre la
compra. Suponiendo que los clientes adquieren solo un tipo de hamburguesa, realice un algoritmo para
determinar cu ́anto debe pagar una persona por N hamburguesas.

"""
#se permite seleccionar unicamente un tipo de hamburguesa 
print("Ingrese <s> para hamburguesa sencilla ($2000 c/u)")
print("Ingrese <d> para hamburguesa doble ($2500 c/u)")
tipo_hamburguesa = input("Ingrese <t> para hamburguesa triple ($3000 c/u)\n")
if tipo_hamburguesa == "s":
    costo_hamburguesa = 2000
elif tipo_hamburguesa == "d":
    costo_hamburguesa = 2500
elif tipo_hamburguesa == "t":
    costo_hamburguesa = 3000
else:
    print("ERROR, ingrese caracter valido")
cantidad_hamburguesas = int(input("Cantidad de hamburguesas a llevar: "))
costo_total = costo_hamburguesa * cantidad_hamburguesas
print("Ingrese forma de pago")
print("<1> para pago con efectivo")
print("<2> para pago con tarjeta de debito")
tipo_pago = int(input("<3> para pago con tarjeta de credito (se adiciona cargo de 5/100 sobre la compra)\n"))
#si opcion de pago es igual a 3, entonces se aplica adicion de 5% sobre el costo de pedido
if tipo_pago == 3:
    costo_total = costo_total + (costo_total * 5/100)
print("El costo de hamburguesa es de", costo_total,"pesos")
