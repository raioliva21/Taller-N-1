"""
Ejericio 6

Un estacionamiento requiere determinar el cobro que debe aplicar a las personas que lo utilizan. Con-
sidere que el cobro es con base en las horas que lo disponen y que las fracciones de hora se toman como
completas. Cree un programa que realice el cobro del estacionamiento

"""
#se cobran $1500 por hora de estacionamiento
#se solicita ingresar tiempo en estacionamiento en minutos
tiempo_estacionado = int(input("Ingrese tiempo (minutos) en estacionamiento\n"))
#se calcula el modulo al dividir 'tiempo_estacionado' por 60 (minutos) equivalente a una hora
#si modulo es diferete a cero, entonces el valor de tiempo estacionado (en horas) es decimal
if tiempo_estacionado % 60 != 0:
    #se aproxima por defecto valor de cuociente, y luego se aumenta en una unidad
    tiempo_estacionado = (tiempo_estacionado // 60) + 1
else:
    #al ser cantidades enteras de horas en estacionamiento 
    tiempo_estacionado = tiempo_estacionado / 60
print("El final de estacionamiento es de", tiempo_estacionado * 1500,"pesos")
