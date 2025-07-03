# passgen.py - Generador de contraseñas seguras
# Este script genera contraseñas seguras y permite guardarlas con etiquetas.
# Este script ha sido generado por un modelo de IA y está diseñado para ser ejecutado en la terminal.
# Requiere Python 3.6 o superior.

import secrets
import string
import argparse
from datetime import datetime

# Función principal para generar la contraseña
def generar_contraseña(longitud, mayusculas, minusculas, numeros, simbolos):
    caracteres = ''
    if mayusculas:
        caracteres += string.ascii_uppercase
    if minusculas:
        caracteres += string.ascii_lowercase
    if numeros:
        caracteres += string.digits
    if simbolos:
        caracteres += string.punctuation

    if not caracteres:
        raise ValueError("Debe seleccionar al menos un tipo de carácter.")

    contraseña = ''.join(secrets.choice(caracteres) for _ in range(longitud))
    return contraseña

# Función para guardar la contraseña en un archivo
def guardar_contraseña(etiqueta, contraseña):
    with open("passwords.txt", "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} - {etiqueta}: {contraseña}\n")

# Función para leer contraseñas guardadas
def mostrar_contraseñas_guardadas():
    try:
        with open("passwords.txt", "r") as f:
            print("\n--- CONTRASEÑAS GUARDADAS ---")
            for linea in f:
                print(linea.strip())
    except FileNotFoundError:
        print("No hay contraseñas guardadas aún.")

# Función principal con argparse
def main():
    parser = argparse.ArgumentParser(description="Generador de contraseñas seguras")
    parser.add_argument('-l', '--longitud', type=int, default=12, help='Longitud de la contraseña (default=12)')
    parser.add_argument('-M', '--mayusculas', action='store_true', help='Incluir letras mayúsculas')
    parser.add_argument('-m', '--minusculas', action='store_true', help='Incluir letras minúsculas')
    parser.add_argument('-n', '--numeros', action='store_true', help='Incluir números')
    parser.add_argument('-s', '--simbolos', action='store_true', help='Incluir símbolos')
    parser.add_argument('-e', '--etiqueta', type=str, help='Etiqueta para identificar la contraseña')
    parser.add_argument('--ver', action='store_true', help='Mostrar contraseñas guardadas')

    args = parser.parse_args()

    if args.ver:
        mostrar_contraseñas_guardadas()
        return

    if not any([args.mayusculas, args.minusculas, args.numeros, args.simbolos]):
        print("⚠️  Seleccionando todos los tipos por defecto (mayúsculas, minúsculas, números)")
        args.mayusculas = args.minusculas = args.numeros = True

    try:
        contraseña = generar_contraseña(args.longitud, args.mayusculas, args.minusculas, args.numeros, args.simbolos)
        print(f"\n🔐 Contraseña generada: {contraseña}")

        if args.etiqueta:
            guardar_contraseña(args.etiqueta, contraseña)
            print(f"💾 Contraseña guardada con la etiqueta '{args.etiqueta}'")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
