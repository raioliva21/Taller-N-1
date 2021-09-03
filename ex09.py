# se utliza libreria para la operacion relacionada a variable 'distancia', que involucra raiz 
import math
unidad_medida = input("Ingrese la unidad de medida\n")
print("Ingrese las coordenadas solicitdados de las puntos (x1,y1) y (x2,y2)")
x1 = int(input("X1: "))
y1 = int(input("y1: "))
x2 = int(input("X2: "))
y2 = int(input("y2: "))
distancia = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
print("la distancia entre ambas puntos es",distancia, unidad_medida)