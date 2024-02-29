import math

#Ve = corresponde a la Velocidad de Escape en [m/s].
#g = corresponde a la constante gravitacional en [m/s2].
#r: Corresponde al radio del planeta en [m].
#rp = "Radio del planeta en km * 1000"
rp = "Radio del planeta en km * 1000"
#Para r = 6371

#Solicitud de imputs

g = float(input("Ingrese el valor de la constante gravitacional en m/s2:\n>"))
r = float(input("Ingrese el valor del radio del planeta en m:\n>"))

# formula de Velocidad de Escape
Ve = (2 * g * r) ** (1/2)
print(f"Velocidad de Escape del planeta es: {math.ceil(Ve)}")

