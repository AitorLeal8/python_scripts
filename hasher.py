import hashlib

def hash_string(string):
    if hashmode == "1":
        res = hashlib.sha256(string.encode()).hexdigest()
        return res
    elif hashmode == "2":
        res = hashlib.sha512(string.encode()).hexdigest()
        return res
    else:
        print("Mete un string")


print("1. SHA256")
print("2. SHA512")
hashmode = input("Mete un algoritmo:") #Input del algoritmo a usar

input_string = input("Mete un string a hashear:") #Input del string a hashear

print(hash_string(input_string)) #Llamada a la función con el string introducido por el usuario



