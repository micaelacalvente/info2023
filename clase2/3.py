# Escribir un programa que pida al usuario dos números y muestre por pantalla cuál de ellos es mayor.

num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
if num1 > num2:
    print(num1, "es mayor que", num2)
elif num1 < num2:
    print(num2, "es mayor que", num1)
else:
    print("Los dos números son iguales")