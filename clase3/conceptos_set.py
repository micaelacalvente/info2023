# SET // CONJUNTO { }

# caracteristicas principales
## desordenado
## no permite duplicados

conjunto = {1, 1, 1, "holis", "que", "tal"}
print(conjunto)

#añadir un elemento a un conjunto
conjunto.add(5)
print(conjunto)

#toma como argumento una lista, tupla, string, conjunto, etc.
conjunto.update(["lista", "list"])
print(conjunto)

#elimina elementos del set
conjunto.discard("holis")
conjunto.remove("holis")

#asegurarme si un elemento esta en el conjunto
print(1 in conjunto)