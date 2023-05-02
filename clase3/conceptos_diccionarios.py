# DICCIONARIO { }
diccionario = {"Micaela": "SP", "Cristian": "SP", "Ramiro": "Resis"}
# clave = unica   |   valor = cualquier tipo de dato

#imprimir el valor de una clave
print(diccionario["Micaela"])

#cambiar valor de una clave
diccionario["Micaela"] = 24

print(diccionario.keys())

print(diccionario.values())

print(diccionario.items())

#elimina el ultimo item
diccionario.popitem()
print(diccionario)

#elimina un item en especifico
diccionario.pop("Micaela")
print(diccionario)