"""
Ejercicio 4

Se requiere un programa para determinar cu ́anto ahorrar ́a una persona en un a ̃no, si al final de cada
mes deposita variables cantidades de dinero; adem ́as, se requiere saber cu ́anto lleva ahorrado cada mes.

"""
#se comienza desde mes '0', asignandose tal valor a 'ahorro_acumulado' inicialmente
ahorro_acumulado = 0
#'meses_ahorro' representa la cantidad de meses que se lleva ahorrando
for meses_ahorro in range (1, 13, 1):
    #se "blanquea" valor de 'ahorro_mes' por cada realizacion de ciclo 
    ahorro_mes = 0
    print("Ingrese ahorro de mes", meses_ahorro)
    ahorro_mes = int(input())
    #se añade el valor 'ahorro_mes', el cual se renueva en cada ciclo, a 'ahorro_acumulado'
    ahorro_acumulado += ahorro_mes
    print("Se lleva", ahorro_acumulado, "pesos de ahorro acumulado hasta la fecha\n")
#una vez que variable 'ahorro_meses' cumple 12 repeticiones, se sale de ciclo for
print("El monto total ahorrado en un año fue de", ahorro_acumulado,"pesos\n")
