# Escribir un programa que pida al usuario un carácter y muestre por pantalla si es una letra mayúscula, una letra minúscula, un número o un carácter especial.

caracter = input("Ingresa un caracter: ")
if caracter.isupper(): #pregunta si es mayuscula
    print("El caracter es una letra mayuscula")
elif caracter.islower(): #pregunta si es minuscula
    print("El caracter es una letra minuscula")
elif caracter.isdigit(): #pregunta si es un digito
    print("El caracter es un numero")
else:
    print("El caracter es especial")