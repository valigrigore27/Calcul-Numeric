
import math
import numpy as np




def calcul_b(matrice_a, vector_s):
    n=len(matrice_a)
    b = [0] * n
    for i in range(n):
        b[i]=sum(matrice_a[i][j] * vector_s[j] for j in range(n))
    return b

def afisare_solutie_b(x):
    print("Solutia b:")
    print([element for element in x])



# def householder(matrice_a, vector_b, eps):
#     n=len(matrice_a)

#     u = [0] * n

#     R=np.eye(n)
#     Q=np.copy(matrice_a)




#     for r in range(n):
        
#         q=sum( (matrice_a[i][r])**2 for i in range (r+1, n))
#         if q<= eps:
#             break

#         k= q**0.5

#         if matrice_a[r][r]>0:
#             k=-k

#         beta= q - k * matrice_a[r][r]

#         for o in range(n):
#             if o < r:
#                 u[o]=0
#             else:
#                 if o == r:
#                     u[o]= matrice_a[r][r]-k
#                 else:
#                     u[o]= matrice_a[o][r]

#         for j in range(r+1, n):
#             gamma= (sum( u[i] * matrice_a[i][j] for i in range(r+1, n))) / beta

#             for i in range(r, n):
#                 matrice_a[i][j] = matrice_a[i][j] - gamma * u[i]
            
#         matrice_a[r][r] = k
#         for i in range(r+1, n):
#             matrice_a[i][r] = 0
    
        
#         gamma = (sum( u[i] * vector_b[i] for i in range(r, n))) / beta

#         for i in range(r , n):
#             vector_b[i] = vector_b[i] - gamma * u[i]

#     return n

def householder_factorization(matrice_a, vector_b, eps, n):
    n = len(matrice_a)
    R = np.copy(matrice_a)
    Q = np.eye(n)

    for r in range(n -1):
        sigma = np.sum(R[r:, r]**2)
        if sigma < eps:
            break
        
        k = np.sqrt(sigma)
        if R[r, r] > 0:
            k = -k
        
        beta = sigma - k * R[r, r]
        u = np.zeros(n)
        u[r] = R[r, r] - k
        
        for i in range(r + 1, n):
            u[i] = R[i, r]
        
        for j in range(r, n):
            gamma = np.sum(u[r:] * R[r:, j]) / beta
            for i in range(r, n):
                R[i, j] -= gamma * u[i]
        
        # gamma = np.sum(u[r:] * vector_b[r:]) / beta
        # for i in range(r, n):
        #     vector_b[i] -= gamma * u[i]

        for j in range(n):
            gamma = np.sum(u[r:] * Q[r:, j]) / beta
            for i in range(r, n):
                Q[i, j] -= gamma * u[i]

    Q=np.transpose(Q)        

    return Q, R     


# def transpose(matrice_a):
#     return [[matrice_a[j][i] for j in range(len(matrice_a))] for i in range(len(matrice_a[0]))]

def transpose(matrix):
    n = len(matrix)
    m = len(matrix[0])
    transposed = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            transposed[j][i] = matrix[i][j]
    return transposed

def afisare_matrice(matrice_a):
    for i in range(len(matrice_a)):
        for j in range(len(matrice_a)):
            print(matrice_a[i][j], end=' ')
        print()
    print()

def multiply_matrices(matrix1, matrix2):
    n = len(matrix1)
    result = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result

def solutia_x(R, Qt, vector_b):
    n = len(R)
    x = [0.0] * n
    y = [0.0] * n

    
    for i in range(n):
        y[i]=sum(Qt[i][j] * vector_b[j] for j in range(n))
      

    for i in range(n- 1, -1, -1):
        suma = sum(R[i][j] * x[j] for j in range(i+1,n))
        x[i] = (y[i] - suma)/ R[i][i] 


    return x
    
def norma1(x, eps, matrice_a, vector_b):
    x_lib = np.linalg.solve(matrice_a, vector_b)
    z = [0] * len(x)
    n = len(matrice_a)
    for i in range(n):
        z[i] = (x_lib[i] - x[i])
        
    return np.sqrt(sum(z**2 for z in z))
    
    
def norma2(x, eps, matrice_a, vector_b):
    z = [0] * len(x)
    n = len(matrice_a)
    for i in range(n):
        z[i] = sum(matrice_a[i][j] * x[j] for j in range(n)) - vector_b[i]

    if eps > np.sqrt(sum(z**2 for z in z)):
        return np.sqrt(sum(z**2 for z in z))
    else:
        return "nu convine"
    
    
def norma3(eps, matrice_a, vector_b):
    x_lib = np.linalg.solve(matrice_a, vector_b)
    z = [0] * len(x_lib)
    n = len(matrice_a)
    for i in range(n):
        z[i] = sum(matrice_a[i][j] * x_lib[j] for j in range(n)) - vector_b[i]

    if eps > np.sqrt(sum(z**2 for z in z)):
        return np.sqrt(sum(z**2 for z in z))
    else:
        return "nu convine"
    
def norma_s(vector_s):
    z = [0] * len(vector_s)
    n = len(vector_s)
    for i in range(n):
        z[i] = (vector_s[i])
    return np.sqrt(sum(z**2 for z in z))

def norma4(eps, x, vector_s):
    z = [0] * len(x)
    n = len(x)
    for i in range(n):
        z[i] = (x[i] - vector_s[i])


    if eps > (np.sqrt(sum(z**2 for z in z))/norma_s(vector_s)):
        return (np.sqrt(sum(z**2 for z in z))/norma_s(vector_s))
    else:
        return "nu convine"
    
def norma5(eps, matrice_a, vector_b, vector_s):
    z = [0] * len(matrice_a)
    x_lib = np.linalg.solve(matrice_a, vector_b)
    n = len(matrice_a)
    for i in range(n):
        z[i] = (x_lib[i] - vector_s[i])
    
    if eps > (np.sqrt(sum(z**2 for z in z))/norma_s(vector_s)):
        return (np.sqrt(sum(z**2 for z in z))/norma_s(vector_s))
    else:
        return "nu convine"

def substitutie(Qt, R, j):
    
    n= len(Qt)
    x=[0]*n
    
    for i in range(n-1, -1, -1):
        suma=sum(x[k]* R[i][k] for k in range(i+1, n))
        x[i]=(Qt[i][j]-suma)/R[i][i]
    
    return x

def inversa(Qt,R):
    
    n= len(Qt)
    x=[0]*n
    #a_invers=([0]*n for _ in range(n))
    a_invers=np.zeros((n,n))
    for j in range(n):
       x=substitutie(Qt,R,j)
       for i in range(n):
           a_invers[i][j]=x[i]
    
    return a_invers
           
    
    

# def norma6( R , Qt, matrice_a):
#     A_lib = np.linalg.inv(matrice_a)
#     n=len(matrice_a)
    
#     C= inversa_QR(R, Qt) - A_lib 
#     norma_matriciala = 0
    
#     for j in range(n):
#         suma_absoluta = 0
    
#         for i in range(n):
#             suma_absoluta += abs(C[i][j])
#         norma_matriciala = max(norma_matriciala, suma_absoluta)

#     return norma_matriciala
    






def rulare():
    
    eps=10**(-6)
    # matrice_a = [
    #     [60, -72, -43],
    #     [80, 154, -99],
    #     [75, 310, 140]
    # ]
    # matrice_a=[
    #    [0 ,0, 4],
    #    [1, 2, 3],
    #    [0, 1, 2]
    # ]
    
    # matrice_a =[
    #     [1/3, 2/3, 2/3],
    #     [2/3, 1/3 ,-2/3],
    #     [-2/3, 2/3 ,-1/3]
    # ]
    
    matrice_a=[
       [0 ,0, 4],
       [1, 2, 3],
       [0, 1, 2]
    ]
    
    vector_s=[3, 2, 1]
    n=len(matrice_a)
    
    # n=10
    # matrice_a = np.random.uniform(-10, 10, size=(n, n))
    # vector_s = np.random.uniform(-10, 10, n)
    
    vector_b=calcul_b(matrice_a, vector_s)
    # vector_b = [60,80,75]
    
    afisare_solutie_b(vector_b)
    Q, R = householder_factorization(matrice_a, vector_b ,eps ,n)
    print("\nMatricea Q este:")
    afisare_matrice(Q)
    print("\nMatricea R este:")
    afisare_matrice(R)
    Qt=np.transpose(Q)
    print("Q transpus este:")
    afisare_matrice(Qt)
    x  =solutia_x(R, Qt, vector_b)
    print("Solutia x este:")
    print(x)
    print("Prima norma:")
    print(norma1(x, eps, matrice_a, vector_b))
    print()
    print("A doua norma:")
    print(norma2(x, eps, matrice_a, vector_b))
    print()
    print("A treia norma:")
    print(norma3(eps, matrice_a, vector_b))
    print()
    print("A patra norma:")
    print(norma4(eps, x, vector_s))
    print()
    print("A cincea norma:")
    print(norma5(eps, matrice_a, vector_b, vector_s))
    print()
    #afisare_matrice(inversa_QR(R, Qt))
    print("A sasea norma")
    #print(norma6(R, Qt, matrice_a))

    afisare_matrice(inversa(Qt, R))
    # y=substitutie(Qt, R ,0)
    # print(y)



rulare()