#usar ambos al mismo tiempo
def super_suma(*args, **kwargs):
    resultado = 0
    for arg in args:
        resultado += arg
    print(resultado)

    for clave, valor in kwargs.items():
        print(f"Bien hecho! {clave}, {valor}")

super_suma(2+2+2+2+2+2+2+2, Profe = "Mica")

