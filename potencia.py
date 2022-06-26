#6-POTENCIA. función potencia, retorna la potencia del primero elevado al segundo parámetros.

a1=int(input("Ingresar el número que desea potenciar: "))
a2=int(input("Ingresar el número por el cual desea elevar el primer valor: "))

def potencia(a1, a2):
    return a1 ** a2

print("El resultado de su operación es:",int(potencia(a1, a2)))
