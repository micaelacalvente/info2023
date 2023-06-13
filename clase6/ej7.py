# Ejercicio 7: Bebidas Online
"""Vamos a administrar un ecommerce de bebidas.
En un depósito se guardan las bebidas a comercializar.
Estos productos son bebidas como agua mineral y gaseosas.
De los productos nos interesa saber su identificador (cada uno tiene uno
distinto), cantidad de litros, precio y marca.
Si es agua mineral nos interesa saber también el origen (Manantial, Ciudad, etc).
Si es una gaseosa queremos saber el porcentaje que tiene de azúcar y si tiene o
no alguna promoción (si la tiene tendrá un descuento del 10% en el precio)."""

"""Calcular precio de todas las bebidas: calcula el precio total de todos los
productos del almacén.
Calcular el precio total de una marca de bebida: dada una marca, calcular el
precio total de esas bebidas.
Agregar producto: agrega un producto, si el identificador esta repetido en
alguno de las bebidas, no se agregará esa bebida.
Eliminar un producto: dado un ID, eliminar el producto del depósito.
Mostrar información: mostramos para cada bebida toda su información"""

class Almacen():
    def __init__(self):
        self.lista_bebidas = []

    def agregar_bebida(self, bebida):
        if not isinstance(bebida, AguaMineral) and not isinstance(bebida, Gaseosa):
            print("Tipo de dato no permitido")
        for b in self.lista_bebidas:
            if b.id == bebida.id:
                print("Id ya existente")
        self.lista_bebidas.append(bebida)

    def obtener_total(self, marca=None):
        total = 0
        if marca is None:
            for b in self.lista_bebidas:
                total += b.get_precio()
        else:
            for b in self.lista_bebidas:
                if b.marca == marca:
                    total += b.get_precio()
        return total
    
    def eliminar_producto(self, id):
        for b in self.lista_bebidas:
            if b.id == id:
                self.lista_bebidas.remove(b)
                return
        print("No se encontró el producto que desea eliminar")
    
    def ver_info(self):
        for b in self.lista_bebidas:
            b.ver_info()


class Bebida():
    def __init__(self, id, litros, marca, precio):
        self.id = id
        self.litros = litros
        self.marca = marca
        self.precio = precio

    def get_precio(self):
        return self.precio
    
    def ver_info(self):
        print("ID: %s" % (self.id))
        print("litros: %s" % (self.litros))
        print("marca: %s" % (self.marca))
        print("precio: %s" % (self.precio))

class AguaMineral(Bebida):
    def __init__(self, id, litros, marca, precio, origen):
        Bebida.__init__(self, id, litros, marca, precio)
        self.origen = origen
    
    def ver_info(self):
        super().ver_info()
        print("origen: %s" % (self.origen))



class Gaseosa(Bebida):
    def __init__(self, id, litros, marca, precio, p_azucar, tiene_descuento):
        Bebida.__init__(self, id, litros, marca, precio)
        self.p_azucar = p_azucar
        self.tiene_descuento = tiene_descuento
        self.descuento = 0.1
    
    def get_precio(self):
        if self.tiene_descuento:
            return self.precio * (1 - self.descuento)
        return self.precio
    
    def ver_info(self):
        super().ver_info()
        print("p_azucar: %s %" % (self.p_azucar))
        print("tiene descuento: %s %" % ("Si" if self.tiene_descuento else "No"))
        print("descuento %s %" % (self.descuento))

a = Almacen()

x = AguaMineral(id=1, litros=2, marca="unaMarca", precio=12, origen="Manatial")
a.agregar_bebida(x)
a.ver_info()