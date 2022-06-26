#7- función radicación, retorna la raiz del primero respecto del segundo parámetros.
a=int(input("Ingresar el número que desea sacar la raíz cuadrada "))
b=int(input("Ingresar el número de la raiz: "))

def raiz(a, b):
    c=pow(a,1/b)

    return c

print("El resultado de su operación es: ",float(raiz(a, b)))
