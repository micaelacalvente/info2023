"""Crear una clase Tiempo, con atributos hora, minuto y segundo, que pueda ser
instanciada indicando: los tres atributos, sólo la hora y minuto, o sólo la hora.
Crear además los métodos necesarios para modificar la hora en cualquier
momento de forma manual. Mantenga la integridad de los datos en todo
momento definiendo de tipo “private”. Crear una clase prueba_tiempo que
prueba una hora concreta y la modifique a su gusto mostrándola por pantalla"""

class Tiempo():
    def __init__(self, hora=0, minuto=0, segundo=0):
        self._hora = hora
        self._minuto = minuto
        self._segundo = segundo
    
    def __str__(self):
        return f"Hora: {self._hora:02d}:{self._minuto:02d}:{self._segundo:02d}"
    
    def cambiar_hora(self, hora=None, minuto=None, segundo=None):
        if hora is not None:
            self._hora = hora
        if minuto is not None:
            self._minuto = minuto
        if segundo is not None:
            self._segundo = segundo
    
class PruebaTiempo():
    def __init__(self):
        self.tiempo = Tiempo()
    
    def __str__(self):
        return str(self.tiempo)

prueba = PruebaTiempo()

#modificar la hora
while True:
    op = int(input("Elegi una opción: \n1.Mostrar hora  \n2.Salir\n"))

    if op == 1:
        hora = int(input("Ingrese la hora: "))
        minuto = int(input("Ingrese los minutos: "))
        segundo = int(input("Ingrese los segundo: "))

        prueba.tiempo.cambiar_hora(hora, minuto, segundo)
        print(prueba)

    if op == 2:
        print("Adios!")
        break
        
