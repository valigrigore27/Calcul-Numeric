import random
import numpy as np


n = 4
eps = 10**-8


def factorizare_crout(a):
    n = len(a)
    
    for p in range(n):
        for i in range(p, n):
            #inferior triunghiulara L
            suma = sum(a[i][k] * a[k][p] for k in range(p))
            a[i][p] = a[i][p] - suma

        for i in range(p + 1, n):
            # superioară triunghiulara U
            suma = sum(a[p][k] * a[k][i] for k in range(p))
            a[p][i] = (a[p][i] - suma) / a[p][p]

    return a

    # for i in range(n):
    #     for k in range(i, n):
    #         #inferior triunghiulara L
    #         suma = sum(a[k][p] * a[p][i] for p in range(i))
    #         a[k][i] = a[k][i] - suma

    #     for k in range(i + 1, n):
    #         # superioară triunghiulara U
    #         suma = sum(a[i][p] * a[p][k] for p in range(i))
    #         a[i][k] = (a[i][k] - suma) / a[i][i]

    # return a




def afisare_L(matrice_a):
    print("Matricea L:")
    for i in range(len(matrice_a)):
        print([matrice_a[i][j] if j <= i else 0.0 for j in range(len(matrice_a[i]))])
    print()

def afisare_U(matrice_a):
    print("\nMatricea U:")
    for i in range(len(matrice_a)):
        print([1.0 if j == i else matrice_a[i][j] if j > i else 0.0 for j in range(len(matrice_a[i]))])
    print()

def afisare_matrice(matrice_a):
    for i in range(len(matrice_a)):
        for j in range(len(matrice_a)):
            print(matrice_a[i][j], end=' ')
        print()
    print()

def afisare_determinant(matrice_a):
    p=1.0
    for i in range(0, len(matrice_a)):
        p*=matrice_a[i][i]

    print("Si determinantul lui A este:" , p)
    print()


def afisare_matrice_b(matrice_b):
    print("vectorul b este:")
    print([element for element in matrice_b])
    print()




# for i in range(len(matrice_a)):
#    suma=sum(matrice_a[i][j]* x[j][0] for j in range(i))
#    x[i][0]=(b[i][0]-suma)/matrice_a[i][i]

def substitutie_directa(matrice_a, matrice_b):
    n = len(matrice_a)
    y = [0.0] * n

    for i in range(n):
        suma = sum(matrice_a[i][j] * y[j] for j in range(i))
        y[i] = (matrice_b[i] - suma) / matrice_a[i][i]

    return y


def substitutie_inversa(matrice_a, y):
    n = len(matrice_a)
    x = [0.0] * n

    for i in range(n - 1, -1, -1):
        suma = sum(matrice_a[i][j] * x[j] for j in range(i+1,n))
        x[i] = y[i] - suma 
    return x



def afisare_solutie_x(x):
    # Afișarea soluției x
    print("Solutia x:")
    print([element for element in x])


def norma(matrice_a, x, matrice_b, eps):
    z = [0] * len(matrice_a)
    for i in range(n):
        s = sum(matrice_a[i][j] * x[j] for j in range(n))
        z[i] = s - matrice_b[i]
    
    if eps > np.sqrt(sum(z**2 for z in z)):
        return np.sqrt(sum(z**2 for z in z))
    else:
        return np.sqrt(sum(z**2 for z in z))
    print()

def norma2(x, eps, copy_matrice_a, copy_matrice_b):
    x_lib = np.linalg.solve(copy_matrice_a, copy_matrice_b)
    z = [0] * len(x)
    for i in range(n):
        z[i] = (x[i] - x_lib[i])**2
        
    if eps > np.sqrt(sum(z**2 for z in z)):
        return np.sqrt(sum(z**2 for z in z))
    else:
        return "nu convine"
    print()


def norma3(x, eps, copy_matrice_a, copy_matrice_b):
    A_inversa = np.linalg.inv(copy_matrice_a)
    z = [0] * len(x)
    for i in range(n):
        s = sum(A_inversa[i][j] * copy_matrice_b[j] for j in range(n))
        z[i] = x[i] - s

    if eps > np.sqrt(sum(z**2 for z in z)):
        return np.sqrt(sum(z**2 for z in z))
    else:
        return "nu convine"
    print()





def rulare():

    matrice_a = [
    [1, 2, 1, 1],
    [1, 4, -1, 7],
    [4, 9, 5, 11],
    [1, 0, 6, 4]
    ]
    matrice_b = [0, 20, 18, 1]


    # matrice_a = np.random.uniform(-10, 10, size=(n, n))
    # matrice_b = np.random.uniform(-10, 10, n)


    copy_matrice_a = np.copy(matrice_a)
    copy_matrice_b = np.copy(matrice_b)

    # if(np.determinant)..
    
    factorizare_crout(matrice_a)
    afisare_matrice(matrice_a)
    afisare_matrice(copy_matrice_a)
    afisare_L(matrice_a)
    afisare_U(matrice_a)
    afisare_matrice(matrice_a)
    afisare_determinant(matrice_a)
    afisare_matrice_b(matrice_b)
    y = substitutie_directa(matrice_a, matrice_b)
    x = substitutie_inversa(matrice_a, y)
    x_lib = np.linalg.solve(copy_matrice_a, copy_matrice_b)
    afisare_solutie_x(x)
    print()
    afisare_solutie_x(x_lib)
    print()
    print(norma(copy_matrice_a, x_lib, copy_matrice_b, eps))
    print()
    print(norma2(x, eps, copy_matrice_a, copy_matrice_b))
    print()
    print(norma3(x, eps, copy_matrice_a, copy_matrice_b))
    print()
    



rulare()


