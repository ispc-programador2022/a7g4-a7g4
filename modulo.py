#MODULO. Función módulo, retorna el módulo de 2 parámetros

v1=int(input("Ingresar el primer número que desea dividir: "))
v2=int(input("Ingresar el segundo número por el cual dividir: "))


def modulo(v1, v2):
    return v1 % v2


print("El módulo de su operación es:",float(modulo(v1, v2)))