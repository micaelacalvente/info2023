"""Un atributo para la cantidad de cebadas restantes hasta que se lava el mate
(representada por un número).
Un atributo para el estado (lleno o vacío).
El constructor debe recibir como parámetro n, la cantidad máxima de cebadas
en base a la cantidad de yerba vertida en el recipiente.
Un método cebar, que llena el mate con agua. Si se intenta cebar con el mate
lleno, se debe lanzar una excepción que imprima el mensaje ¡Cuidado! ¡Te
quemaste!
Un método beber, que vacía el mate y le resta una cebada disponible. Si se
intenta beber un mate vacío, se debe lanzar una excepción que imprima el
mensaje. El mate está vacío!
Es posible seguir cebando y bebiendo el mate aunque no haya cebadas
disponibles. En ese caso la cantidad de cebadas restantes se mantendrá en 0,
y cada vez que se intente beber se debe imprimir un mensaje de aviso:
Advertencia: "el mate está lavado", pero no se debe lanzar una excepción."""

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
    
mate = Mate(5, "vacio") #crear instancia de clase Mate con 5 cebadas y estado "vacio"

try:
    mate.cebar() #intento cebar el mate
    print("Se cebo el mate correctamente")
except Exception as e:
    print(str(e)) #capturar y mostrar cualquier excepcion que se lance

try:
    mate.beber()
    print("Que rico mate me tome")
except Exception as e:
    print(str(e))


