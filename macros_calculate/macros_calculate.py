#/usr/bin/python3

import signal, sys, time

def def_handler(sig, frame):
    print("\n\n[!] Saliendo ...\n")
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

# Variables Globales
peso = int()
fa = int()
opcion_etapa = int()

def tabla():
    # Saber la etapa en la que está y como de rápido quiere hacerlo
    print("\n\t|-------------------------------------------------------------------------------------|")
    print("\t|\t\tTipo          \t\t\t Volumen (%)\t     Definición (%)   |")                   
    print("\t|-------------------------------------------------------------------------------------|")
    print("\t| [1] Preservar el máximo musculo\t\t   + 0.10\t\t- 0.10        |")
    print("\t| [2] Perdida/Ganancia de peso más rápido\t   + 0.15\t\t- 0.20        |")
    print("\t| [3] Urgencia perder/ganar peso\t\t   + 0.20\t\t- 0.30        |")
    print("\t|-------------------------------------------------------------------------------------|")

def volumen(fa,peso):

    print("\n[+] Volumen")
    opcion_etapa = input("[?] ¿Como de rápido quieres ganar musculo? (1-3)   ")
    opcion_etapa = int(opcion_etapa)

    while opcion_etapa != 1 and opcion_etapa != 2 and opcion_etapa != 3:
        print("\n[!] Introduce una opcion disponible [1-3]")

        opcion_etapa = input("\n[?] ¿Como de rápido quieres ganar musculo? (1-3)   ")

    if opcion_etapa == 1:
        opcion_etapa = 0.10
    elif opcion_etapa == 2:
        opcion_etapa = 0.15
    elif opcion_etapa == 3:
        opcion_etapa = 0.20

    resultados(opcion_etapa,fa,peso)

def definicion(fa,peso):

    print("\n[+] Definición")
    opcion_etapa = input("[?] ¿Como de rápido quieres perder grasa? (1-3)   ")
    opcion_etapa = int(opcion_etapa)

    while opcion_etapa != 1 and opcion_etapa != 2 and opcion_etapa != 3:
        print("\n[!] Introduce una opcion disponible [1-3]")

        opcion_etapa = input("\n[?] ¿Como de rápido quieres perder grasa? (1-3)   ")

    if opcion_etapa == 1:
        opcion_etapa = -0.10
    elif opcion_etapa == 2:
        opcion_etapa = -0.2
    elif opcion_etapa == 3:
        opcion_etapa = -0.30

    resultados(opcion_etapa,fa,peso)

def resultados(opcion_etapa,fa,peso):

    gasto_calorico_dia = peso * 22 * fa
    deficit_superavit = gasto_calorico_dia * opcion_etapa
    kcal_total = gasto_calorico_dia + deficit_superavit

    # Imprimiendo las fórmulas
    print("\n[i] Fórmulas:")
    print("\tGasto Calórico / Día peso   %s * 22 * %s = %d" %(peso, fa, gasto_calorico_dia))
    print("\tSuperávit    %d * %s = %s" % (gasto_calorico_dia, opcion_etapa, deficit_superavit))
    print("\tKcal Totales   %d + %d" % (gasto_calorico_dia, deficit_superavit))

    # Imprimiendo los resultados totales
    print("\n[i] Resultados:")
    print("\t[+] Superávit: %d" % deficit_superavit )
    print("\t[+] Kcal Totales: %d" % kcal_total)

def macros():

    # Saber el peso
    peso = input("[?] ¿Cual es tu peso actual? (decimales con comas)   ")
    peso = int(peso)

    # Saber el Factor de Actividad
    print("\n\t|-----------------------------------------------------------------------------|")
    print("\t|   Tipo de Ejercicio\t\t\tDías\t\tFactor de Actividad   |")                   
    print("\t|-----------------------------------------------------------------------------|")
    print("\t| [1] Poco o ningun ejercicio\t\t  /\t\t\t1.20          |")
    print("\t| [2] Ejercicio Ligero\t\t\t1 - 3\t\t\t1.40          |")
    print("\t| [3] Ejercicio Moderado\t\t3 - 5\t\t\t1.60          |")
    print("\t| [4] Ejercicio Fuerte\t\t\t6 - 7\t\t\t1.80          |")
    print("\t| [5] Ejercicio muy fuerte\t      x2 / día\t\t\t2.00          |")
    print("\t|-----------------------------------------------------------------------------|")

    fa = input("\n[?] ¿Cual es tu Factor de Actividad (FA)? (1-5)   ")
    fa = int(fa)

    while fa != 1 and fa != 2 and fa != 3 and fa != 4 and fa != 5:
        print("\n[!] Introduce una opción correcta [1-5]")

        fa = input("\n[?] ¿Cual es tu Factor de Actividad (FA)? (1-5)   ")
        fa = int(fa)

    if fa == 1:
        fa = 1.20
    elif fa == 2:
        fa = 1.40
    elif fa == 3:
        fa = 1.60
    elif fa == 4:
        fa = 1.80
    elif fa == 5:
        fa = 2

    # Etapa actual Volumen/Definición
    etapa = input("\n[?] ¿En que etapa te encuentras actualmente? (Volumen[V]/Definición[D])   ")
    etapa = etapa.upper()
    
    while etapa != "V" and etapa != "D":
        print("\n[!] Introduce una opcion disponible [V/D]")
        etapa = input("\n[?] ¿En que etapa te encuentras actualmente? (Volumen[V]/Definición[D])   ")
        etapa = etapa.upper()

    tabla()

    if etapa == 'V':
        volumen(fa,peso)
    elif etapa == 'D':
        definicion(fa,peso)

if __name__ == '__main__':
    macros()
