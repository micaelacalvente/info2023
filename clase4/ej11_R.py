numero = int(input("Ingresar un numero: "))
lista_numero = range(1, numero+1)
factorial = 0


i = 0
while i < len(lista_numero)-1:
    if factorial < 1:
        factorial = lista_numero[i]*lista_numero[i+1]
    else:
        factorial = factorial * lista_numero[i+1]
    
    i += 1

print(f"Factorial de {numero} es: {factorial}")