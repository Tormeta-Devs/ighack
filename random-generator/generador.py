import itertools
import random
import os

# Preguntar si se incluirán caracteres especiales
caracteres_especiales = input("¿Desea incluir caracteres especiales? (s/n): ")

if caracteres_especiales.lower() == "s":
    # Definir los caracteres que se combinarán, incluyendo caracteres especiales
    caracteres = "abcdefghijklmnopqrstuvwxyz!#$%&()*+,-./:;<=>?@[\\]^_`{|}~"
    caracteres_mayus = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numeros = "0123456789"
else:
    # Definir los caracteres que se combinarán, sin caracteres especiales
    caracteres = "abcdefghijklmnopqrstuvwxyz"
    caracteres_mayus = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numeros = "0123456789"

# Pedir la cantidad de letras mayúsculas y minúsculas
cant_mayus = int(input("Ingrese la cantidad de letras mayúsculas que desea incluir: "))
cant_minus = int(input("Ingrese la cantidad de letras minúsculas que desea incluir: "))

# Pedir la cantidad de números que se incluirán
cant_numeros = int(input("Ingrese la cantidad de números que desea incluir: "))

# Pedir la cantidad de combinaciones a generar
cant_combinaciones = int(input("Ingrese la cantidad de combinaciones que desea generar: "))

# Calcular la longitud total de cada combinación
longitud = cant_mayus + cant_minus + cant_numeros

# Crear un directorio "Generated" en el directorio anterior
dir_path = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
generated_dir = os.path.join(dir_path, "Generated")
os.makedirs(generated_dir, exist_ok=True)

# Generar múltiples combinaciones
for i in range(cant_combinaciones):
    # Elegir al azar los caracteres que se utilizarán en cada combinación
    caracteres_comb = [random.choice(caracteres) for i in range(longitud-cant_mayus-cant_minus-cant_numeros)]
    caracteres_mayus_comb = [random.choice(caracteres_mayus) for i in range(cant_mayus)]
    caracteres_minus_comb = [random.choice(caracteres) for i in range(cant_minus)]
    numeros_comb = [random.choice(numeros) for i in range(cant_numeros)]

    # Combinar todos los caracteres
    caracteres_comb.extend(caracteres_mayus_comb)
    caracteres_comb.extend(caracteres_minus_comb)
    caracteres_comb.extend(numeros_comb)

    # Mezclar los caracteres para generar combinaciones únicas
    random.shuffle(caracteres_comb)

    # Convertir la lista de caracteres en una cadena
    combinacion = ''.join(caracteres_comb)

    # Escribir la combinación en el archivo "generated.txt" en la carpeta "Generated"
    file_path = os.path.join(generated_dir, "generated.txt")
    with open(file_path, "a") as archivo:
        archivo.write(combinacion + "\n")

print(f"Se han generado {cant_combinaciones} combinaciones en el archivo 'generated.txt' en la carpeta 'Generated'.")
