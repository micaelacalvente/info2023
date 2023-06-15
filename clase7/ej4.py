"""En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de
edad, por lo tanto hay que crear un método esTitularValido() que devuelve
verdadero si el titular es mayor de edad pero menor de 25 años y falso en
caso contrario.
Además la retirada de dinero sólo se podrá hacer si el titular es válido.
El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la
bonificación de la cuenta."""
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def esTitularValido(self):
        return 18 < self.edad < 25


class Cuenta:
    def __init__(self, titular, cantidad=0):
        self.titular = titular
        self.cantidad = cantidad

    def mostrar(self):
        print("Titular:", self.titular.nombre)
        print("Cantidad:", self.cantidad)

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.cantidad += cantidad

    def retirar(self, cantidad):
        self.cantidad -= cantidad


class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad=0, bonificacion=0):
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion

    def mostrar(self):
        print("Cuenta Joven")
        print("Titular:", self.titular.nombre)
        print("Cantidad:", self.cantidad)
        print("Bonificación:", self.bonificacion, "%")

    def retirar(self, cantidad):
        if self.titular.esTitularValido():
            super().retirar(cantidad)
        else:
            print("No se puede retirar dinero. Titular no válido.")


# Ejemplo de uso

# Crear una instancia de Persona con la edad del titular
edad_titular = 25
titular = Persona("Micaela", edad_titular)

# Crear una instancia de CuentaJoven con el titular y otros detalles
cuenta_joven = CuentaJoven(titular, 120000, 5)

# Mostrar la información de la cuenta
cuenta_joven.mostrar()

# Retirar dinero
retirar = float(input("Ingrese el monto a retirar: "))
cuenta_joven.retirar(retirar)
cuenta_joven.mostrar()

# Ingresar dinero
ing = float(input("Ingrese el monto a ingresar: "))
cuenta_joven.ingresar(ing)
cuenta_joven.mostrar()