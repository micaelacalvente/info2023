# LISTAS [ ]

lista = ["Info", 6, 2023, True, False, 3.14]

#imprimir todos los elementos de una lista
print(lista)

#acceder a elementos en una lista
print(lista[0]) 

#acceder a un rango de elementos de la lista (slicing)
print(lista[1:4])
print(lista[:3])
print(lista[2:])

#acceder al ultimo elemento
print(lista[-1])

#modificar un elemento
lista[2] = "New"

#agregar un elemento a la lista
lista.append(8)

#eliminar un elemento de la lista
lista.remove(6)

#imprime el numero de elementos en una lista
print(len(lista))

#agrega elementos al final de la lista
lista.extend(["nuevo", "elemento"])

#agrega un elemento a una posicion especifica
lista.insert(2, "New")

#elimina el elemento de una posicion especifica y lo devuelve
print(lista.pop(2))

#elimina todos los elementos de una lista
print(lista.clear())

#devuelve la posicion de la primera aparición de un elemento en una lista
numeros = [1, 2, 3, 4, 2, 5]
print(numeros.index(2, 0, 8))

'''El método list.index devuelve el índice más bajo en el que se encuentre el elemento x en el bloque list[start:end]. 
Si el elemento x no se encuentra, el método devuelve un error de tipo ValueError. 
Si no se especifican los argumentos start o end, se toman como valores por defecto el comienzo y el final de la lista. '''

#devuelve el numero de veces que un elemento aparece en una lista
print(numeros.count(2))

#ordena los elementos de la lista
profes = ["Ramiro", "Micaela", "Cristian"]
profes.sort()
#devuelve el orden inverso
profes.sort(reverse=False)