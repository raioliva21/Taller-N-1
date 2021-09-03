"""
Ejercicio 3

Una multitienda tiene una promocion: a todos los trajes que tienen un precio superior a $10000 se les
aplicara un descuento de 15 %, a todos los demas se les aplicara solo 8 %. Realice un programa para
determinar el precio final que debe pagar una persona por comprar un traje y de cuanto es el descuento
que obtendra. Pida por lo menos ingresar 3 elementos

"""
#se asgina valor 0 a variable 'cantidad_trajes', cuyo valor ira incremenando una unidad en ciclo while
cantidad_trajes = 0
#se asigna caracter a variable 'decision' a modo de ingresar a ciclo while
decision = "s"
while decision != "n":
    cantidad_trajes += 1
    valor_traje = int(input("Ingrese valor de traje elegido\n"))
    if valor_traje <= 10000:
        valor_traje = valor_traje - valor_traje * 8/100
        print("Se aplica descuento de 8%\nValor de traje con descuento aplicado:", valor_traje)
    else:
        valor_traje = valor_traje - valor_traje * 15/100
        print("Se aplica descuento de 15%\nValor de traje con descuento aplicado:", valor_traje)
    # si la cantidad de trajes ingresados es mayor o igual a 3
    if cantidad_trajes > 2:
        decision = input("¿Desea seguir agregando prendas al carro? s/n\n")