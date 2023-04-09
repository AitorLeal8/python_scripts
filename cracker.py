import hashlib
import sys

# verifies if the dictionary argument was passed
if len(sys.argv) < 2: 
    print("Error: you must pass the dictionary as an argument")
    sys.exit(1) 

diccionario = (sys.argv[1]) # saves the dictionary in a variable

input_hash = input("Introduce el hash md5: ")
encontrada = False 

try:
    diccionario_file = open(diccionario, "r") # opens the dictionary
except:
    print("No se puede abrir el diccionario") # if the dictionary cannot be opened, an error message is shown
    quit()

for word in diccionario_file:
    palabra_formateada = word.encode('utf-8') # formats the word to utf-8 so it doesn't cause an error
    palabra_hasheada = hashlib.md5(palabra_formateada.strip()).hexdigest() # hashes the word, removes spaces and converts to hexadecimal

    if palabra_hasheada == input_hash:
        print("La contraseña es: " + word)
        encontrada = True
        break

if not encontrada:
    print("Contraseña no encontrada en el diccionario")

