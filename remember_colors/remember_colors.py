#/usr/bin/python3

from colorama import Fore, Style, Back
from tqdm import tqdm
import random
import sys
import signal
import time

# Función del Ctrl + C
def def_handler(sig, frame):
    print(Fore.RED + "\n\n[+] Saliendo ...\n" + Style.RESET_ALL)
    sys.exit(1)

# Ctrl + C
signal.signal(signal.SIGINT, def_handler)

# Variables Globales
pattern_colors = ['rojo', 'verde', 'azul', 'amarillo', 'cian', 'blanco', 'negro', 'marron', 'rosa', 'morado']
pattern_colors_map = {
        'rojo': "\x1b[31m",
        'verde': "\x1b[32m",
        'azul': "\x1b[34m",
        'amarillo': "\x1b[33m",
        'cian': "\x1b[36m",
        'blanco': "\x1b[37m",
        'negro': "\x1b[30m",
        'marron': "\x1b[38;2;139;69;19m",
        'rosa': "\x1b[95m",
        'morado': "\x1b[35m"
}
colors = []
points = 0
level = 1

# Funcion ver Baner:
def show_banner():
    banner = """
██████╗ ███████╗███╗   ███╗███████╗███╗   ███╗██████╗ ███████╗██████╗  
██╔══██╗██╔════╝████╗ ████║██╔════╝████╗ ████║██╔══██╗██╔════╝██╔══██╗
██████╔╝█████╗  ██╔████╔██║█████╗  ██╔████╔██║██████╔╝█████╗  ██████╔╝
██╔══██╗██╔══╝  ██║╚██╔╝██║██╔══╝  ██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗
██║  ██║███████╗██║ ╚═╝ ██║███████╗██║ ╚═╝ ██║██████╔╝███████╗██║  ██║
╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝╚══════╝╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝
                                                                      
 ██████╗ ██████╗ ██╗      ██████╗ ██████╗ ███████╗                    
██╔════╝██╔═══██╗██║     ██╔═══██╗██╔══██╗██╔════╝                    
██║     ██║   ██║██║     ██║   ██║██████╔╝███████╗                    
██║     ██║   ██║██║     ██║   ██║██╔══██╗╚════██║                    
╚██████╗╚██████╔╝███████╗╚██████╔╝██║  ██║███████║                    
 ╚═════╝ ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝ 
    """
    print(banner)

# Funcion limpiar pantalla
def clear_screen():

    print("\033c", end="")
    time.sleep(0.5)

def rules():
    print("\x1b[37m" + "\n[i] Reglas:\n")
    print("\t[1] Tienes que intentar adivinar todos los colores que salen en el juego.")
    print("\t[2] Saldran los colores de dos en dos en caso de que hayas introducido 2 en la primera pregunta (si has introducido 5, saldrán de cinco en cinco.")
    print("\t[3] Supongamos que has elegido de tres en tres. Primeramente saldrán 3 colores, por lo que los introduces en el orden que salieron")
    print("\t[4] Después saldrán otros tres colores, por lo que tienes que introducir los tres colores que salieron antes más los nuevos que salieron")
    print("\t[+] Espero que disfrutes del juego :) <3" + Style.RESET_ALL)

# Función generadora de colores
def color_generator(num_combinations):

    #p1 = log.progress("Colores")
    user_counter = int(1)

    for i in range(num_combinations):
        rand_color = random.choice(pattern_colors)
        colors.append(rand_color)

        actual_color = colors[-1]

        color_code = pattern_colors_map.get(actual_color, Fore.RESET)
        print(f"[{user_counter}] " + color_code + actual_color + Style.RESET_ALL)

        time.sleep(1)
        user_counter += 1

    return colors

# Función donde el usuario adivinará el color
def guess_color(colors, points):
   
    for idx, color in enumerate(colors, start=1):
        user_input = input("[+] Introduce el color de la posición %d   " % idx).lower()

        # Validar que el color ingresado sea uno de los colores válidos
        while user_input not in pattern_colors:
            print(Fore.YELLOW + "[!] Color inválido. Los colores válidos son:", ", ".join(pattern_colors) + Style.RESET_ALL)
            user_input = input("[+] Introduce el color de la posición %d  " % idx).lower()

        if color == user_input:
            points += 1
            print("[+] ¡Genial! Puntos totales: %d" % points)
        else:
            combinacion_incorrecta(colors, points)

def combinacion_incorrecta(colors, points):
    print(Fore.RED + "\n[✘] Perdiste con un total de %d puntos :( ..." % points + Style.RESET_ALL)
    print(Fore.RED + "\n[!] La combinación era:", ", ".join(colors))
    sys.exit(0)
    
# Función Main
if __name__ == '__main__':
   
    clear_screen()
    show_banner()

    rules()

    print("\n[] Nivel %d" % level + Style.RESET_ALL)
    
    counter = input("\n¿Con cuantas combinaciones quieres que muestre?   ")
    print("")
    counter = int(counter)

    while True:
        colors = color_generator(counter)
        clear_screen()
        guess_color(colors, points)
