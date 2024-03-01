import math
#P: Precio de Suscripción
#U: Número de Usuarios
#Un : Usuario Normal
#Up : Usuario Premiun( equivale al 50% más de un usuario normal)
#Up : 1.5 * Up
#U = Usuario Normal + Usuario Premiun
#U = UN +1.5 * Up
#GT: Gastos Totales

#Solicitud de imputs
P = float(input("Ingrese el valor del Precio de suscripcion en pesos:\n>"))
Un = float(input("Ingrese el valor del Numero de Usuarios Normales:\n>"))
Up = float(input("Ingrese el valor del Numero de Usuarios Premium:\n>"))
GT = float(input("Ingrese el valor del Gasto Total en pesos:\n>"))

#formula de Utilidades
Utilidades = P *  Un + P * 1.5 * Up  - GT

print(f"Las ulilidades operacionales es de: {math.ceil(Utilidades)}")