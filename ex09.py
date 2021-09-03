"""
Ejercicio 9
Se requiere obtener la distancia entre dos puntos en el plano cartesiano.
Para resolver este problema es necesario conocer las coordenadas de cada punto (X, Y), y con esto
poder obtener el cateto de abscisas (X 1 y X 2 ) y el de ordenadas (Y 1 e Y 2 ), y mediante estos valores
obtener la distancia entre P 1 y P 2 , utilizando el teorema de Pitágoras.
"""

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
