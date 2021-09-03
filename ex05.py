"""
Ejercicio 5

Una empresa que contrata personal requiere determinar la edad de cada una de las personas que
solicitan trabajo, pero cuando se les realiza la entrevista solo se les pregunta el a ̃no en que nacieron.
Tambi ́en se requiere el promedio de edad de las personas contratadas.

"""
edad = int
decision = None
promedio_trabajador = 0
cantidad_personal = 0

while decision != 'n':
    cantidad_personal += 1
    ano_nacimiento = int(input("Ingrese año de nacimiento\n"))
    edad = 2021 - ano_nacimiento
    promedio_trabajador = (promedio_trabajador + edad) / cantidad_personal
    print("La edad del trabajador", cantidad_personal,"es de", edad,"años")
    print("El promedio de edad del total de trabajadores actuales es de", promedio_trabajador,"años")
    decision = input("¿Desea seguir añadiendo trabajadores? s/n\n")


