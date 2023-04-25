# Escribir un programa que pida al usuario dos números y muestre por pantalla la suma de ellos solo si ambos son pares.

n1 = int(input("Ingresa el primer numero: "))
n2 = int(input("Ingresa el segundo numero: "))

if n1 % 2 == 0 and n2 % 2 == 0:
    print(f"La suma de {n1} + {n2} =", n1 + n2)
else:
    print("Los numeros no son pares")