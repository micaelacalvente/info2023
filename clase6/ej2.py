# SUPER CLASE
class Vehiculo():
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return "Color {}, {} ruedas".format( self.color, self.ruedas )

# SUB CLASE
class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        Vehiculo.__init__(self, color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return Vehiculo.__str__(self) + ", {} km/h, {} cc".format(self.velocidad, self.cilindrada)
    
class Camioneta(Coche):
    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.carga = carga
    
    def __str__(self):
        return super().__str__() + ", {} kg".format(self.carga)

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return super().__str__() + ", {}".format(self.tipo)
    
class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        super().__init__(color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return super().__str__() + ", {} km/h, {} cc".format(self.velocidad, self.cilindrada)

#FUNCION CATALOGAR 1
"""def catalogar(lista_vehiculos):
    for vehiculo in lista_vehiculos:
        print("Clase: {}".format(vehiculo.__class__.__name__))
        print("Atributos: {}".format(vehiculo))"""

#FUNCION CATALOGAR 2
def catalogar(lista_vehiculos, ruedas=None):
    if ruedas != None:
        vehiculos_filtro = [vehiculo for vehiculo in lista_vehiculos if vehiculo.ruedas == ruedas]
        print("Se han encontrado {} vehículos con {} ruedas:".format(len(vehiculos_filtro), ruedas))
        for vehiculo in lista_vehiculos:
            print("Clase: {}".format(vehiculo.__class__.__name__))
            print("Atributos: {}".format(vehiculo))
    else:
        for vehiculo in lista_vehiculos:
            print("Clase: {}".format(vehiculo.__class__.__name__))
            print("Atributos: {}".format(vehiculo))



# crear una lista de vehiculos
vehiculos = [
    Vehiculo("rojo", 4),
    Coche("azul", 4, 150, 1500),
    Camioneta("negro", 4, 180, 2000, 500),
    Bicicleta("amarillo", 2, "urbana"),
    Motocicleta("verde", 2, "dax", 100, 1000),
]

#LLAMO A LA FUNCION
catalogar(vehiculos)
