"""
Situacion Profecionalizante
Ejercicio 13- función que devuelva la suma de las combinaciones posibles de los números generados
por la función genrnd tomados de a dos.

"""
from ejercicio_12 import genrnd

def summation():
    my_number_list = genrnd()
    print(my_number_list)
    s = 0
    
    for i in range(len(my_number_list)-1):
        for j in range(i+1, len(my_number_list)):
            s += my_number_list[i] + my_number_list[j]
    return s
print(summation())
