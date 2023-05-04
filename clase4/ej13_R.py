numero = int(input("Ingresar un numero: "))
piramide = ""

i = 1
while i <= numero:
    piramide += "*"*i+"\n"
    i += 1

print(piramide)