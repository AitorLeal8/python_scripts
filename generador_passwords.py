import random
import hashlib
import os

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+'


print('Generador de passwords')
print('======================')

npasswoprs = input("Cuantas password quieres generar?: ")
npasswoprs = int(npasswoprs)

length = input("Longitud de las passwords: ")
length = int(length)

print('\nAqui estan tus passwords hasheadas:')

passwords = []
raw_passwords = []
for i in range(npasswoprs):
    password = ''
    for j in range(length):
        password += random.choice(chars)
    hashed_password = hashlib.sha512(password.encode()).hexdigest()
    passwords.append(hashed_password)
    raw_passwords.append(password)
    print(hashed_password)

save = input("Quieres guardarlas en un archivo? (y/n)")
filename = "passwd.txt"
directory = "passwd"

if save.lower() == "y":
    if not os.path.exists(directory):
        os.makedirs(directory)
    os.chdir(directory)
    filepath = os.path.join(os.getcwd(), filename) # getcwd() = directorio actual, join() = une directorios

    if os.path.isfile(filepath): # Si el archivo ya existe, pregunta si se quiere sobreescribir
        print(f"El archivo {filepath} ya existe.")
        overwrite = input("Desea sobreescribirlo? (y/n)")
        if overwrite.lower() == "y":
            with open(filepath, "w") as f:
                for p in raw_passwords:
                    f.write(p + "\n")
                print(f"Las passwords se guardaron en el archivo {filepath}")

        if overwrite.lower() == "n": # Si no se quiere sobreescribir, se cierra el programa
            print("Las passwords no se guardaron en un archivo.")
            exit()

    else: # Si el archivo no existe, se crea
        with open(filepath, "w") as f:
            for p in raw_passwords:
                f.write(p + "\n") # Se escribe cada password en una linea
            print(f"Las passwords se guardaron en el archivo {filepath}")

else:
    print("Las passwords no se guardaron en un archivo.")
