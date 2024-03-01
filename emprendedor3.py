import math
#Paan: Precio de Suscripción por mes año anterior
#Uaan: Número de Usuario por mes año anterior
#GTaan: Gastos Totales por mes año anterior
#Paa: Precio de Suscripción por mes año actual
#Uaa: Número de Usuario por mes año actual
#GTaa: Gastos Totales por mes año actual

#Solicitud de imputs por mes año anterior
Paan = float(input("Ingrese el valor del Precio de suscripcion en $ por mes año anterior:\n>"))
Uaan = float(input("Ingrese el valor del Numero de Usuarios por mes año anterior:\n>"))
GTaan = float(input("Ingrese el valor del Gasto Total en $ por mes año anterior:\n>"))
#Solicitud de imputs año actual
Paa = float(input("Ingrese el valor del Precio de suscripcion en $ por mes año actual:\n>"))
Uaa = float(input("Ingrese el valor del Numero de Usuarios por mes año actual:\n>"))
GTaa = float(input("Ingrese el valor del Gasto Total en $ por mes año actual:\n>"))
#formula de Utilidades año anterior
Utilidadesaan = (Paan * Uaan - GTaan) * 12
#formula de Utilidades año actual
Utilidadesaa = (Paa * Uaa - GTaa) *12

print(f"Las ulilidades operacionales es de: {math.ceil(Utilidadesaan)}")
print(f"Las ulilidades operacionales es de: {math.ceil(Utilidadesaa)}")

#a = Razon entre utilidades del año anterior y año actual
resultado = (Utilidadesaan/Utilidadesaa)

# :.2f indica que debe mostrar un float con 2 decimales y cualquier parte entera
formatted = "La cantidad en $ es: {:.2f}".format(resultado)

print(formatted)