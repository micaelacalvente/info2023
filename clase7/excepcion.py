comision_6 = ["Mica", "Rami", "Cris"]
print(comision_6)

#SIN MANEJO DE ERRORES
"""indice = int(input("Ingrese un indice: "))
print(comision_6[indice])"""

#CON MANEJO DE ERRORES
try:
    indice = int(input("Ingrese un indice: "))
    print(comision_6[indice])
except IndexError and ValueError:
    print("El indice ingresado no es valido")
else:
    print("Es un profe de la comision 6")
finally:
    print("Fin del programa")