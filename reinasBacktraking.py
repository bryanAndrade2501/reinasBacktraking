import re

CANT_REINAS = 8
posiciones = [0]*CANT_REINAS
global reina
reina = [None]*CANT_REINAS
global resultadosTotales
resultadosTotales = []
#contador soluciones
cont_soluciones = 0

def imprimir_tablero():
    global cont_soluciones
    x=y=0
    cont_soluciones +=1

    
    print('La solucion #%d es: \t'%cont_soluciones)
    for x in range (CANT_REINAS):
        for y in range(CANT_REINAS):
            if x == reina[y]:
                print('<' +str(x)+','+str(y)+'>',end='')
                posiciones[x]=(x,y)
            else:
               print('<NOREINA>',end='')
        print('\t')
    resultadosTotales.append(posiciones)
    print(posiciones)

def posicion_correcta(fila, columna):
    global reina 
    i=0
    ataque=0
    posicion_fila=posicion_columna=0
    while (ataque!=1) and i < columna:
        posicion_columna = abs(i-columna)
        posicion_fila = abs(reina[i]-fila)

        if reina[i] == fila or posicion_columna == posicion_fila:
            ataque = 1
        i+=1
    return ataque

def identificar_posicion_reina(k_etapa):
    global reina 
    i=0
    while i<CANT_REINAS:
        if posicion_correcta(i, k_etapa)!=1:
            reina[k_etapa]=i
            if k_etapa==7:
                imprimir_tablero()
            else:
                identificar_posicion_reina(k_etapa+1)
        i=i+1


identificar_posicion_reina(0)

print("\n")
print("Se han generado " + str(len(resultadosTotales)) + " resultados")
numero = int(input("Ingrese la solución que desea visualizar "))
print(resultadosTotales[numero])
