"""Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que
es una persona) y cantidad (puede tener decimales). El titular será obligatorio y
la cantidad es opcional.

mostrar(): Muestra los datos de la cuenta.
ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad
introducida es negativa, no se hará nada.
retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en
números rojos.
"""

class Cuenta():
    def __init__(self, titular, cantidad=0.0):
        self.titular = titular
        self.cantidad = cantidad

    def mostrar(self):
        print("Titular: ", self.titular)
        print("Cantidad: ", self.cantidad)
    
    def ingresar(self, cantidad):
        if cantidad > 0:
            self.cantidad += cantidad
    
    def retirar(self, cantidad):
        self.cantidad -= cantidad

c1 = Cuenta("Micaela", 1200)
c1.mostrar()

retirar = float(input(f"Ingrese el monto a retirar: "))
c1.retirar(retirar)
c1.mostrar()