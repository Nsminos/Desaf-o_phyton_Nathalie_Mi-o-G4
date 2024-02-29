import math

#Ve = corresponde a la Velocidad de Escape en [m/s].
#g = corresponde a la constante gravitacional en [m/s2].
#r: Corresponde al radio del planeta en [m].
r = "Radio en km * 1000"
#Solicitud de imputs

g = float(input("Ingrese el valor de la constante gravitacional en m/s2:\n>"))
r = float(input("Ingrese el valor del radio del planeta en m"))

# formula de Velocidad de Escape
Ve = math.square(2 * g * r)
