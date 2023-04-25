# CONCEPTOS TEORICOS #
# con numeral se escriben los comentarios

# # # TIPOS DE DATOS
# NUMERICO
# entero - int
num = 10
print(type(10)) #type devuelve el tipo de dato

# decimal - float
num2 = 10.2
print(type(num2))

# string
nombre = "Micaela"
print(type(nombre))

# lógico / booleano
bool = True #verdadero
bool = False #falso
print(f"La variable bool, contiene el valor: {bool} y es del tipo {type(bool)}")



# # # OPERADORES MATEMATICOS

#int en el input se asegura de que se ingrese un num int
n1 = int(input("Introduce el primer número: "))
n2 = int(input("Introduce el segundo número: "))

suma = n1 + n2
resta = n1 - n2
multiplicacion = n1 * n2
division = n1 / n2 # / retorna un float y // retorna un int
modulo = n1 % n2 # retorna el resto de la division
potencia = n1 ** n2



# # # OPERADORES DE COMPARACION
# retornan un valor logico (True / False)

v1 = n1 > n2 # mayor que
v2 = n1 >= n2 # mayor o igual que
v3 = n1 < n2 # menor que
v4 = n1 <= n2 # menor o igual que
v5 = n1 == n2 # igual
v6 = n1 != n2 #distinto

#actuan sobre cualquier tipo de dato y retornan un valor logico



# # # OPERADORES LOGICOS
log1 = True
log2 = False

print(log1 and log2) #False 
print(log1 or log2) #True
print(not log1) #False

#actuan con valores logicos y retornan un valor logico
