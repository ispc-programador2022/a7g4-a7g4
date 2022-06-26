#COCIENTE .Retorna el cociente de 2 parámetros

param1=int(input("Por favor, ingrese el primer número que desea dividir: "))
param2=int(input("Por favor, ingrese el segundo número por el cual dividir: "))

def cociente(param1, param2):
    return param1 / param2

print("El resultado de su operación es: ",int(cociente(param1, param2)))
