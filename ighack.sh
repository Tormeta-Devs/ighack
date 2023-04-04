#!/bin/bash

clear
echo -e "\033[1;32m"
figlet -f slant "Password Cracker" | lolcat

read -p "¿En qué idioma prefieres comunicarte? (es/en): " lang

case "$lang" in
  "es") 
    clear
    echo -e "\033[1;32m"
    figlet -f slant "Hackeador de contraseñas" | lolcat
    echo ""
    echo "¿Cómo quieres generar tu contraseña?
    1. Diccionario personalizado
    2. Diccionario predeterminado
    3. Aleatoriamente"

    read -p "Ingresa tu elección: " choice

    case "$choice" in
      "1") 
        read -p "Ingresa la ruta del archivo de diccionario personalizado (.txt): " dictionary_file
        clear
        cd random-generator
        python dictionary.py -f $dictionary_file
        cd ..
        password_file=$dictionary_file
        ;;
      "2")
        echo "¿Quieres generar combinaciones con el diccionario predeterminado?"
        read -p "Ingresa 's' para Sí o cualquier otra cosa para No: " combinations

        if [ "$combinations" == "s" ]; then
          clear
          cd random-generator
          python diccionario.py
          cd ..
          password_file="random-generator/Generated/generated.txt"
        else
          password_file="random-generator/pass.txt"
        fi
        ;;
      "3") 
        clear
        cd random-generator
        python generador.py
        cd ..
        password_file="random-generator/Generated/generated.txt"
        ;;
      *) 
        echo "Opción inválida. Saliendo del script."
        exit 1
        ;;
    esac
    ;;
  "en")
    clear
    echo -e "\033[1;32m"
    figlet -f slant "Password Cracker" | lolcat
    echo ""
    echo "How do you want to generate your password for hack?
    1. Custom dictionary
    2. Default dictionary
    3. Randomly"

    read -p "Enter your choice: " choice

    case "$choice" in
      "1")
        read -p "Enter the path to your custom dictionary file (.txt): " dictionary_file
        clear
        cd random-generator
        python dictionary.py -f $dictionary_file
        cd ..
        password_file=$dictionary_file
        ;;
      "2")
        echo "Do you want to generate combinations with the default dictionary?"
        read -p "Enter 'y' for Yes or anything else for No: " combinations

        if [ "$combinations" == "y" ]; then
          clear
          cd random-generator
          python dictionary.py
          cd ..
          password_file="random-generator/Generated/generated.txt"
        else
          password_file="random-generator/pass.txt"
        fi
        ;;
      "3")
        clear
        cd random-generator
        python generator.py
        cd ..
        password_file="random-generator/Generated/generated.txt"
        ;;
      *)
        echo "Invalid option. Exiting script."
        exit 1
        ;;
    esac
    ;;
  *)
    echo "Invalid language. Exiting script."
    exit 1
    ;;
esac

read -p "Please enter Instagram username: " username

echo "Executing"

instagram-py --username $username --password-list $password_file