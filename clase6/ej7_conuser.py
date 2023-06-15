class Almacen():
    def __init__(self):
        self.lista_bebidas = []

    def agregar_bebida(self, bebida):
        if not isinstance(bebida, AguaMineral) and not isinstance(bebida, Gaseosa):
            print("Tipo de dato no permitido")
            return
        for b in self.lista_bebidas:
            if b.id == bebida.id:
                print("Id existente")
                return
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
        print("No se encontró el producto con el ID especificado")

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
        print("CANTIDAD DE LITROS: %s" % (self.litros))
        print("MARCA: %s" % (self.marca))
        print("PRECIO: %s" % (self.precio))


class AguaMineral(Bebida):
    def __init__(self, id, litros, marca, precio, origen):
        super().__init__(id, litros, marca, precio)
        self.origen = origen

    def ver_info(self):
        super().ver_info()
        print("ORIGEN: %s" % (self.origen))


class Gaseosa(Bebida):
    def __init__(self, id, litros, marca, precio, p_azucar, tiene_descuento):
        super().__init__(id, litros, marca, precio)
        self.p_azucar = p_azucar
        self.tiene_descuento = tiene_descuento
        self.descuento = 0.1

    def get_precio(self):
        if self.tiene_descuento:
            return self.precio * (1 - self.descuento)
        return self.precio

    def ver_info(self):
        super().ver_info()
        print("PORCENTAJE DE AZUCAR: %s %" % (self.p_azucar))
        print("TIENE DESCUENTO: %s %" % ("Si" if self.tiene_descuento else "No"))
        print("DESCUENTO %s %" % (self.descuento))


a = Almacen()

while True:
    print("\n--- Menú ---")
    print("1. Agregar producto")
    print("2. Calcular precio de todas las bebidas")
    print("3. Calcular precio total de una marca de bebida")
    print("4. Eliminar un producto")
    print("5. Mostrar información")
    print("0. Salir")

    opcion = int(input("Ingrese el número de la opción que desea ejecutar: "))

    if opcion == 1:
        tipo_bebida = input("Ingrese el tipo de bebida (agua/gaseosa): ")
        id = input("Ingrese el ID de la bebida: ")
        litros = float(input("Ingrese la cantidad de litros: "))
        marca = input("Ingrese la marca: ")
        precio = float(input("Ingrese el precio: "))

        if tipo_bebida == "agua":
            origen = input("Ingrese el origen del agua mineral: ")
            bebida = AguaMineral(id, litros, marca, precio, origen)
        elif tipo_bebida == "gaseosa":
            p_azucar = float(input("Ingrese el porcentaje de azúcar: "))
            tiene_descuento = input("Tiene descuento (si/no): ")
            bebida = Gaseosa(id, litros, marca, precio, p_azucar, tiene_descuento.lower() == "si")
        else:
            print("Tipo de bebida no válido")
            continue

        a.agregar_bebida(bebida)

    elif opcion == 2:
        total = a.obtener_total()
        print("El precio total de todas las bebidas en el almacén es: %.2f" % total)

    elif opcion == 3:
        marca = input("Ingrese la marca de la bebida: ")
        total = a.obtener_total(marca)
        print("El precio total de las bebidas de la marca %s es: %.2f" % (marca, total))

    elif opcion == 4:
        id = input("Ingrese el ID del producto que desea eliminar: ")
        a.eliminar_producto(id)

    elif opcion == 5:
        a.ver_info()

    elif opcion == 0:
        print("¡Hasta luego!")
        break

    else:
        print("Opción no válida. Por favor, ingrese una opción válida.")