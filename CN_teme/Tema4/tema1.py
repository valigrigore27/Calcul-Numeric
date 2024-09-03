
eps=10**(-8)

def citeste_1(fisier):
    matrice_economica = []
    verificare = 0

    with open(fisier, 'r') as f:
        linii = f.readlines()
        numar_linii = int(linii[0])  
        for linie in linii[1:]:  
            linie = linie.replace(" ", "")
            valori = linie.split(',')
            if int(valori[1]) == int(valori[2])  and abs(float(valori[0])) > eps :    
                verificare += 1
            indice_linie = int(valori[1])  
            tuplu_valori = (float(valori[0]), int(valori[2]))
            if len(matrice_economica) <= indice_linie:
                matrice_economica.extend([[]] * (indice_linie + 1 - len(matrice_economica)))
            matrice_economica[indice_linie].append(tuplu_valori) 
    if verificare == numar_linii:
        return matrice_economica, numar_linii, 0
    else:
        return matrice_economica, numar_linii, 1

def citeste_b(fisier):
    vector = []

    with open(fisier, 'r') as f:
        linii = f.readlines()
        numar_linii = int(linii[0])  
        for linie in linii[1:numar_linii + 1]:  #
            valori = linie.strip().split(',') 
            for valoare in valori:
                if valoare.strip():  
                    vector.append(float(valoare))  

    return vector, numar_linii

def citeste_2(fisier):
    valori = []
    ind_col = []
    inceput_linii= []
    verificare = 0
    index = -1
    t = 0

    with open(fisier, 'r') as f:
        linii = f.readlines()
        numar_linii = int(linii[0])  
        for linie in linii[1:]:
            t += 1  
            linie = linie.replace(" ", "")
            termeni = linie.split(',')
            indice_linie = int(termeni[1])  
            if int(termeni[1]) == int(termeni[2]) and abs(float(termeni[0]))>eps:    
                verificare += 1
            valori.append(float(termeni[0]))
            ind_col.append(int(termeni[2]))
            if indice_linie != index :
                inceput_linii.append(int(t))
                index = indice_linie

    t += 1 
    inceput_linii.append(int(t))
    if verificare == numar_linii:
        return valori, ind_col , inceput_linii , 0
    else:
        return valori, ind_col , inceput_linii , 1
    
def Gauss_Seidel1(matrice_economica, b, numar_linii, kmax):
    x = [0.0] * numar_linii
    k=0
    while True:
        eroare = 0
        for i in range(numar_linii):
            old_x = x[i]
            suma = 0
            for j in range(len(matrice_economica[i])):
                if i != matrice_economica[i][j][1]:
                    suma += matrice_economica[i][j][0] * x[matrice_economica[i][j][1]]
                else:
                    element_diagonala = matrice_economica[i][j][0]
            if element_diagonala is None:
                raise ValueError("Diagonal element not found or initialized.")
            x[i] = (b[i] - suma) / element_diagonala
            eroare += abs(old_x - x[i])
        
        k += 1
        if eroare < eps or k > kmax or eroare > 10**(8):
            break
    #return x , k
    if eroare < eps:
        return x , k
    else:
        return "divergenta" , -1  

def Gauss_Seidel2(valori, ind_col , inceput_linii, b,  kmax):
    
    x = [0.0] * len(valori)
    k=0
    while True:
        eroare = 0
        for i in range(1, len(inceput_linii)+1):
            old_x = x[i-1]
            suma = 0
            for j in range(inceput_linii[i-1]-1, inceput_linii[i]-1):
                element_diagonala = 1
                if i-1 != ind_col[j]:
                    suma += valori[j] * x[ind_col[j]]
                else:
                    element_diagonala = 1
                    
                if element_diagonala is None:
                    raise ValueError("Diagonal element not found or initialized.")
                
                x[i-1] = (b[i-1] - suma) / element_diagonala
                eroare += abs(old_x - x[i-1])   
                
            k += 1
            if eroare < eps or k > kmax or eroare > 10**(9):
                break
        return x , k
        if eroare < eps:
            return x , k
        else:
            return "divergenta"
        
def Gauss_Seidel3(valori, ind_col, inceput_linii, b, kmax):
    numar_linii = len(inceput_linii) - 1
    x = [0.0] * numar_linii
    k = 0
    while True:
        eroare = 0
        for i in range(numar_linii):
            old_x = x[i]
            suma = 0

            start_index = inceput_linii[i]-1
            end_index = inceput_linii[i + 1]-1 if i + 1 < numar_linii else len(valori)

            for j in range(start_index, end_index):
                if i != ind_col[j]:  
                    suma += valori[j] * x[ind_col[j]]
                else:
                    element_diagonala = valori[j]
 


            x[i] = (b[i] - suma) / element_diagonala

            eroare += abs(old_x - x[i])

        k += 1

        if eroare < eps or k > kmax or eroare > 1e9:
            break

    if eroare < eps:
        return x, k
    else:
        return "divergenta"
            
def norma1(matrice_economica, b, x, n):
    res = [0] * len(b)
    for i in range(n):
        for val, col in matrice_economica[i]:
            res[i] += val * x[col]
    for i in range(len(res)):
        res[i] -= b[i]
    return max(abs(val) for val in res)

def norma2(valori, ind_col, inceput_linii, x, b):
    n = len(inceput_linii) - 1
    norm = [0] * len(b)
    for i in range(n):
        for j in range(inceput_linii[i] - 1, inceput_linii[i + 1] - 1):
            norm[i] += valori[j] * x[ind_col[j]]
        
        for i in range(len(norm)):
            norm[i] -= b[i]
        return max(abs(val) for val in norm)
    
def norma3(valori, ind_col, inceput_linii, b, x):
    n = len(b)  # Numărul de ecuații
    res = [0.0] * n

    # Calculăm reziduurile R = A*x - b folosind lista CSR
    for i in range(n):
        start_index = inceput_linii[i]-1
        end_index = inceput_linii[i + 1]-1 if i + 1 < len(inceput_linii) else len(valori)

        for j in range(start_index, end_index):
            col = ind_col[j]
            val = valori[j]
            res[i] += val * x[col]

        res[i] -= b[i]

    norma= (sum(r ** 2 for r in res))** 0.5 

    return norma    

#bonus


        
def bonus():
    # matrice_economica = citeste_1('a.txt')[0]
    # n = citeste_1('a.txt')[1]
    # b = citeste_1('b.txt')[0]
    
    # aplusb = citeste_1('aplusb.txt')[0]
    
    # C = suma(matrice_economica, n, b)
    # equal = compare(C, aplusb, n)
    # if equal:
    #     print("Matricele sunt egale")
    # else:
    #     print("Matricele nu sunt egale")
    
    matrice_economica, n ,z1 = citeste_1('a.txt')
    b , m, z2 = citeste_1('b.txt')
    
    aplusb , p, z3= citeste_1('aplusb.txt')
    if n == m and m == p:
        C = suma(matrice_economica, b, n)
        equal = compare(C, aplusb, n)
        if equal:
            print("Matricele sunt egale")
        else:
            print("Matricele nu sunt egale")
    else:
        print("Matricele nu sunt egale")       

def rulare():
    a_file = "a_5.txt"
    b_file = "b_5.txt"
    matrice_economica , n, are_elem_nule = citeste_1(a_file)
    b, m = citeste_b(b_file)
    valori, ind_col , inceput_linii , are_elem_nule2 = citeste_2(a_file)
    
    print("MATRICEA ECONOMICA: ", matrice_economica)
    # print("VECTORUL B: ", b)
    # print("VALORI:", valori)
    # print("INDICE COLOANA: ", ind_col)
    # print("INCEPUT LINII: ", inceput_linii)
    print("#################################################################################################################################")

    #Prima memorare
    if are_elem_nule == 1:
        print("nu convine")
    #else:
        #x1, k = (Gauss_Seidel1(matrice_economica, b, n, 10000))
        #print("SOLUTIA X: ", x1)
    
    print("Norma 1: ")
    #print(norma1(matrice_economica, b, x1, n))
    
    print("#################################################################################################################################")
    
    #A doua memorare
    if are_elem_nule2 == 1:
        print("nu convine")
    #else:
        #x2, k2 = (Gauss_Seidel3(valori, ind_col, inceput_linii, b, 10000))
        # print("SOLUTIA X: ", x2)

    print("Norma 2: ")
    #print(norma1(matrice_economica, b, x2, n))
    print("#################################################################################################################################")
    
    bonus()
    
    
rulare()