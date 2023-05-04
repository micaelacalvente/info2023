print("Bienvenida")

while True:
    n1 = int(input("Ingrese el primer numero: "))
    n2 = int(input("Ingrese el segundo numero: "))

    print("Elija una opcion:")
    print("1-SUMA")
    print("2-RESTA")
    print("3-MULTIPLICAR")
    print("4-DIVIDIR")
    print("5-SALIR")
    op = int(input())

    if op == 1:
        resultado = n1 + n2
    elif op == 2:
        resultado = n1 - n2
    elif op == 3:
        resultado = n1 * n2
    elif op == 4:
        resultado = n1 // n2
    else:
        break #romper
    print("el resultado es: ", resultado)

print("Chau")
