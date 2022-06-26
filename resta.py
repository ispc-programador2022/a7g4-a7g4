#RESTA. función resta, retorna la resta de 2 parámetros.

valor_1=int(input("Ingrese el primer número que desea restar: "))
valor_2=int(input("Ingrese el segundo número por el cual desea restar: "))

def resta (valor_1, valor_2):
    return valor_1 - valor_2

print("El resultado de su operación es:: ",resta(valor_1, valor_2))
