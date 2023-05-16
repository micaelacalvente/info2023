def imprimir_pares(num):
    cont = 2
    while cont <= num:
        print(cont)
        cont += 2

num = int(input("Ingrese un numero entero: \n"))
imprimir_pares(num)