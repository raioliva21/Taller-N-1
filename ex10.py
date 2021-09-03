"""
Ejericio 10
Una empresa constructora vende terrenos con la forma A de la figura. Se requiere crear un programa
para obtener el área respectiva de un terreno de medidas de cualquier valor.
Para resolver este problema se debe identificar que la forma A está compuesta por dos figuras: un
triángulo de base B y de altura (A - C); y por otro lado, un rectángulo que tiene base B y altura C y
la suma de ambas áreas es el resultado final.
"""

unidad_medida = input("Ingrese unidad de medida\n")
# variable "base_figuras" refiere tanto a la base de triangulo como rectangulo (de igual medida)
base_figuras = int(input("Ingrese medida de la base del rectangulo (o triangulo)\n"))
altura_triangulo = int(input("Ingrese altura de triangulo\n"))
altura_rectangulo = int(input("Ingrese altura de rectangulo\n"))
area_triangulo = (base_figuras * altura_triangulo) / 2
area_rectangulo = (base_figuras * altura_rectangulo)
print("El area de la figura A es de",area_rectangulo + area_triangulo,unidad_medida)
