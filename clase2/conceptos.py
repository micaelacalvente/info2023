# condicional simple
comision = 6
if comision == 6:
    print("Hola comision 6")



# condicional multiple
comision = 6
ciudad = "Saenz Peña"

if comision == 6 and ciudad == "Saenz Peña":
    print("Saludos desde el info comision 6 saenzpeñicola")

if comision == 6 or ciudad == "Saenz Peña":
    print("Saludos desde el info")



# condicional alternativo o doble
n = 11
if n % 2 == 0:
    print(n, "es un número par")
else:
    print(n, "es un numero impar")



# condicional alternativo multiple
nota = float(input("Ingresa una nota: "))

if nota >= 9:
    print("Sobresaliente")
elif nota >= 7:
    print("Notable")
elif nota >= 6:
    print("Bien")
elif nota >= 5:
    print("Suficiente")
else:
    print("Insuficiente")