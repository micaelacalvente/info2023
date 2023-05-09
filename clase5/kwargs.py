# argumentos indeterminados nombre
# KWARGS

def indeterminado_nombre(**kwargs):
    print(kwargs)

print("Asistencia")
indeterminado_nombre(nombre="Micaela", edad=24, comision="6")
print()
indeterminado_nombre(nombre="Lucas", edad=23, comision="6")

