def es_divisible(n1, n2):
    if (n1 % n2) == 0:
        return True
    else: 
        return False

n1 = int(input("Ingrese dos numeros enteros: \n"))
n2 = int(input())

if es_divisible(n1, n2):
    print("son numeros divisibles entre si")
else:
    print("No son divisibles entre si")