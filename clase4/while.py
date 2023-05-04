# WHILE // MIENTRAS

# while [condicion/es]
#    ACCION
# el codigo se ejecuta repetitivamente, hasta que la condicion sea falsa

tope = int(input("Ingrese un numero: "))
i = 1

while (i < tope):
    print(i)
    i += 1   # i = i + 1 #terminar el ciclo


# y si queres seguir?
seguir = "SI"
while (seguir == "SI"):
    tope = int(input("Ingrese un numero: "))
    i = 1

    while (i < tope):
        print(i, end=" ")
        i += 1
    
    print("\nTermine") # \n new line  \t tab
    seguir = input("quiere empezar de nuevo? ").upper() #transforma a mayusculas

print("Adios :)")

