# Escribe un programa que pida al usuario una cadena de texto y luego imprima la misma cadena pero con todas las vocales en mayúscula.

texto = input("Ingrese una cadena de texto: ")
texto_modificado = ""

for letra in texto:
    if letra in "aeiouAEIOU":
        texto_modificado += letra.upper()
    else:
        texto_modificado += letra

print(texto_modificado)
