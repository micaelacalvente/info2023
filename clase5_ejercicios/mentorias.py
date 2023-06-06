"""
-Crea una función llamada 
imprimir_pares que tome un número entero como
parámetro y imprima todos los números pares desde 
1 hasta ese número.
"""

def imprimir_pares(numero):
    for num in range(2, numero + 1, 2):
        print(num)

imprimir_pares(10)