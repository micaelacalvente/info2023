#ejemplo de una clase Perro class 
class Perro:
    #atributos
    def __init__(self, nombre, edad, color):
            self.nombre = nombre
            self.edad = edad
            self.color = color
    #metodos
    def ladrar(self):
        print("¡Guau, guau!")

    def comer(self):
        print("El perro está comiendo.")

    def dormir(self):
        print("El perro está durmiendo.")

#llamo los distintos metodos

#creo un objeto el cual pertenece a la clase "Perro"
caniche = Perro("lola", 5, "blanco")

#puedo imprimir sus atributos
print("Hola soy: " + caniche.nombre)

#puedo llamar sus metodos
caniche.ladrar()