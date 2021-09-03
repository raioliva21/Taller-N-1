"""
Ejercicio 8

Se requiere obtener el área de la figura en la forma A de la siguiente imagen. Para resolver este problema
se puede partir de que está formada por tres figuras: dos triángulos rectángulos, con H como hipotenusa
y R como uno de los catetos, que también es el radio de la otra figura, una semicircunferencia que forma
la parte circular (ver forma B).
"""

# se utliza libreria para dar con la operacion relativa al valor de altura, que requiere raiz
import math
unidad_medicion = input("Ingrese unidad de medicion\n")
cateto = int(input("Ingrese medida de cateto menor de uno de los dos triangulos rectangulo\n"))
hipotenusa = int(input("Ingrese hipotenusa de tal triangulo\n"))
if hipotenusa <= cateto:
    print("ERROR, hipotenusa no puede ser mayor a cateto en triangulo")
# cateto** + altura** = hipotenusa**   
altura = math.sqrt(hipotenusa**2 - cateto**2)
area_triangulo = (altura * cateto) / 2
# cateto de traingulo = radio de circulo
# a modo de evitar arbitriaridad por la aproximacion de numero pi, no se otorga valor a tal numero
area_circulo_sinPi= cateto**2
area_figuraA = (area_triangulo * 2) + (area_circulo_sinPi / 2)
print("El area de la figura de la forma A es de",area_figuraA,"pi",unidad_medicion) 

