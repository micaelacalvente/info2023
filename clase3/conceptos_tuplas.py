# TUPLAS ( )

#empaquetar
tupla = (1, 2, 3)
tupla2 = 1, 2, 3
tupla3 = 1,

#desempaquetar
uno, dos, tres = tupla
print(uno, dos, tres)

#indexacion
print(tupla2[2:])

#cuenta el numero de veces que el elemento x esta en la tupla
n = (1, 1, 1, 0, 0, 0)
print(n.count(1))

#retorna el indice mas pequeño del elemento x
print(n.index(0))

#conversion lista a tupla
lista = ["hola", "como", "va"]
tupla_nueva = tuple(lista)

#conversion tupla a lista
t = ("otra", "conversion")
lista_nueva = list(t)