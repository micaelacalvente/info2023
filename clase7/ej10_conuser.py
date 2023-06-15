class Mate():
    #constructor
    def __init__(self, cebadas, estado):
        self.cebadas = cebadas
        self.estado = estado
        self.max_cebadas = 20

    #metodos
    def cebar(self):
        if self.estado.lower() == "lleno":
            raise Exception("¡Cuidado! ¡Te quemaste!")
        self.estado = "lleno"

    def beber(self):
        if self.estado.lower() != "lleno":
            raise Exception("El mate está vacío!")
        else:
            if self.cebadas > 0:
                self.max_cebadas -= 1
            if self.max_cebadas == 0:
                print("Advertencia el mate esta lavado")
            self.estado = "vacio"

def mostrar_menu():
    print("1. cebar")
    print("2. beber")
    print("0. salir")

mate = Mate(0, "vacio") #crear instancia de clase Mate con 5 cebadas y estado "vacio"

while True:
    mostrar_menu()
    opcion = int(input("seleccione una opcion: "))

    if opcion == 1:
        try:
            mate.cebar() #intento cebar el mate
            print("Se cebo el mate correctamente")
        except Exception as e:
            print(str(e)) #capturar y mostrar cualquier excepcion que se lance
    elif opcion == 2:
        try:
            mate.beber()
            print("Que rico mate me tome")
        except Exception as e:
            print(str(e))
    elif opcion == 0:
        print("Hasta luego")
        break
    else:
        print("Opcion invalida")