"""
Situacion Profecionalizante
Ejercicio 12 - función genrnd que retorna una lista con 50 números aleatorios.


"""
import random as rnd



def genrnd():
    new_list = [rnd.randint(0,100) for i in range(50)]
    return new_list

print(genrnd())



