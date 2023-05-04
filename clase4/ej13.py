# Escribe un programa que pida al usuario un número y luego imprima un triángulo de asteriscos con esa cantidad de filas.
num_filas = int(input("Ingrese un numero: "))

for f in range(num_filas):
    for c in range(f+1):
        print("*", end=" ")
    print()