# crear una función
def saludo(comision):
    """esta funcion devuelve un saludo
    
    Keyword arguments:
    comision -- el numero comision
    Return: 
    hola {numero} comision
    """
    
    print(f"Hola comision {comision}")

print("Bienvenido al mundo de las funciones")
saludo(6)
saludo(7)
print(saludo.__doc__)