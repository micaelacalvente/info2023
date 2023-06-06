class Persona:
    #constructor
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    #metodo
    def saludar(self):
        print(f"Hola mi nombre es {self.nombre} tengo {self.edad}")

persona1 = Persona("Juan", 25)
persona1.saludar()
persona2 = Persona("Micaela", 25)
persona2.saludar()