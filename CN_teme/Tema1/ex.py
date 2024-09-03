import math
import random
import numpy as np

p = 1
u = pow(10, -p)
while 1 + u != 1:
    p+=1
    u = pow(10, -p)

print(u)


x = 1.0
y = u/10
z = u/10
if((x + y)+z) != (x+(y + z)):
    print("Nu este asociativa")
else:
    print("Este asociativa")



x = random.uniform(1, 100000)
y = random.uniform(1, 100000)
z = random.uniform(1, 100000)   
i=0
while(((x * y)*z) == (x*(y * z))):
    x = random.uniform(1, 100000)
    y = random.uniform(1, 100000)
    z = random.uniform(1, 100000)
    i+=1
print(x," ", y," ", z)
print()
print(i)



def T_4(a):
    return (105 * a - 10 * a**3) / (105 - 45 * a**2 + a**4)

def T_5(a):
    return (945 * a - 105 * a**3 + a**5) / (945 - 420 * a**2 + 15 * a**4)

def T_6(a):
    return (10395 * a - 1260 * a**3 + 21 * a**5) / (10395 - 4725 * a**2 + 210 * a**4 - a**6)

def T_7(a):
    return (135135 * a - 17525 * a**3 + 378 * a**5 - a**7) / (135135 - 62370 * a**2 + 3150 * a**4 - 28 * a**6)

def T_8(a):
    return (2027025 * a - 270270 * a**3 + 6930 * a**5 - 36 * a**7) / (2027025 - 945945 * a**2 + 51975 * a**4 - 6300 * a**6 + a**8)

def T_9(a):
    return (34459425 * a - 4729725 * a**3 + 135135 * a**5 - 990 * a**7 + a**9) / (34459425 - 16216200 * a**2 + 945945 * a**4 - 13860 * a**6 + 45 * a**8)


# Lista de functii
functions = [T_4, T_5, T_6, T_7, T_8, T_9]


# Generam numerele aleatorii
random_numbers = [random.uniform(-math.pi/2, math.pi/2) for _ in range(10000)]


# Calculam valorile fiecarei functii la aceste puncte
values = [[f(a) for a in random_numbers] for f in functions]
errors = [np.abs(np.tan(random_numbers) - v) for v in values]


hierarchy_indices = np.argsort(np.mean(errors, axis=1))
hierarchy = [functions[i].__name__ for i in hierarchy_indices]


# Gasim cele trei functii care ofera cele mai bune aproximatii
best_function_indices = hierarchy_indices[:3]
best_functions = [functions[i].__name__ for i in best_function_indices]




print(hierarchy)
print()
print(best_functions)

##########

# Definim funcțiile S si C


def T(n, a):
    functions = {4: lambda a: T_4(a),
                 5: lambda a: T_5(a),
                 6: lambda a: T_6(a),
                 7: lambda a: T_7(a),
                 8: lambda a: T_8(a),
                 9: lambda a: T_9(a)}

    if n in functions:
        return functions[n](a)


def S(n, a):
    return (1 - T(n, (2*a - math.pi)/4)**2) / (1 + T(n, (2*a - math.pi)/4)**2)

def C(n, a):
    return (1 - T(n, a/2)**2) / (1 + T(n, a/2)**2)

a = math.pi/4
n = 7

print("Aprox sin:")
print()
print(S(n, a))
sinreal=math.sin(a)
error = abs(sinreal - S(n, a))
print()
print(error)

print()

print("Aprox cos:")
print()
print(C(n, a))