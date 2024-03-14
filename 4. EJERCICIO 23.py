#Capitulo 4. Ejercicio propuesto 23

import math

def resolver_ecuacion_segundo_grado(A, B, C):
    discriminante = B ** 2 - 4 * A * C
    
    if discriminante > 0:
        s1 = (-B - math.sqrt(discriminante)) / (2 * A)
        s2 = (-B + math.sqrt(discriminante)) / (2 * A)
        print(f"Las soluciones de la ecuación son: {s1} y {s2}")
    
    elif discriminante == 0:
        sln = -B / (2 * A)
        print(f"La ecuación tiene una única solución: {sln}")
    
    else:
        print("La ecuación tiene soluciones complejas.")

A = float(input("Ingrese el valor de A: "))
B = float(input("Ingrese el valor de B: "))
C = float(input("Ingrese el valor de C: "))

resolver_ecuacion_segundo_grado(A, B, C)

