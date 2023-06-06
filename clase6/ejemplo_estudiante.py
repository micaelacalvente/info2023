#Definir clase/molde (estructura)
class Estudiante:
    #definir atributos/constructor
    def __init__(self, nom, e):
        self.nombre = nom
        self.edad = e
    
    #definicion metodos
    def mostrar_nombre(self):
        return f"Mi nombre es: {self.nombre}"
    
e1 = Estudiante("Lucas", 22)
e2 = Estudiante("Roberto", 26)
e3 = Estudiante("Paula", 19)

# SIN CLASES DEBERIAMOS GUARDAR ESTO DE ESTA MANERA:
# estudiantes = { edad: 19, nombre: Paula}

print(e3.mostrar_nombre())