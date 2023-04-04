import itertools

# Abre el archivo de diccionario español
with open("diccionario.txt", "r", encoding="utf-8") as f:
    dictionary = [word.strip() for word in f.readlines()]

num_mayus = int(input("Ingrese la cantidad de letras mayúsculas: "))
num_minus = int(input("Ingrese la cantidad de letras minúsculas: "))
num_numeros = int(input("Ingrese la cantidad de números: "))
caracteres_especiales = input("¿Quiere añadir caracteres especiales? (s/n): ")

# Definir los caracteres a usar en las combinaciones
caracteres = "abcdefghijklmnopqrstuvwxyz"
caracteres_mayus = caracteres.upper()
numeros = "0123456789"
especiales = "!@#$%^&*()_+-=[]{}|;:,.<>?\"'\\/"

if caracteres_especiales.lower() == "s":
    caracteres += especiales

# Genera todas las posibles combinaciones
combinaciones = itertools.product(
    caracteres_mayus, repeat=num_mayus)  # letras mayúsculas
combinaciones = itertools.product(
    combinaciones, caracteres, repeat=num_minus)  # letras minúsculas
combinaciones = itertools.product(
    combinaciones, numeros, repeat=num_numeros)  # números
combinaciones = itertools.chain.from_iterable(combinaciones)
combinaciones = [''.join(comb) for comb in combinaciones]

# Filtra las combinaciones que están en el diccionario
combinaciones_validas = set(combinaciones).intersection(dictionary)

# Guarda las combinaciones válidas en un archivo
with open("generated.txt", "w", encoding="utf-8") as f:
    for comb in combinaciones_validas:
        f.write(comb + "\n")

# Crea una nueva carpeta y mueve el archivo generado a ella
import os
if not os.path.exists("Generated"):
    os.makedirs("Generated")
os.rename("generated.txt", os.path.join("Generated", "generated.txt"))
