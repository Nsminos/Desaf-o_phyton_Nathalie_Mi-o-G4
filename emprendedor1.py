import math
#P: Precio de Suscripción
#U: Número de Usuarios
#GT: Gastos Totales

#Solicitud de imputs
P = float(input("Ingrese el valor del Precio de suscripcion en pesos:\n>"))
U = float(input("Ingrese el valor del Numero de Usuarios:\n>"))
GT = float(input("Ingrese el valor del Gasto Total en pesos:\n>"))

#formula de Utilidades
Utilidades = P * U - GT

print(f"Las ulilidades operacionales es de: {math.ceil(Utilidades)}")