"""
Ejercicio 2

inicialice una variable en None y si la palabra ingresada es “Hola” debe imprimir Chao, caso contrario
debe decir, no entiendo t ́u mensaje e imprimir el valor de la variable

"""
palabra = None
palabra = input("Hola mundo, dime algo\n")
if palabra == "hola":
    print("chao")
else:
    print("No entiendo tu mensaje,",palabra)
