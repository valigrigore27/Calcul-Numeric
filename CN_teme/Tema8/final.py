import numpy as np
import random


def F1(x, y):
    return x**2 + y**2 - 2*x - 4*y - 1

def F2(x, y):
    return 3*x**2 - 12*x + 2*y**2 + 16*y - 10

def F3(x, y):
    return x**2 - 4*x*y + 5*y**2 - 4*y + 3

def F4(x, y):
    return x**2*y - 2*x*y**2 + 3*x*y + 4



def grad_F_approx(x, y, F, h):
    G1 = (3*F(x, y) - 4*F(x - h, y) + F(x - 2*h, y)) / (2*h)
    G2 = (3*F(x, y) - 4*F(x, y - h) + F(x, y - 2*h)) / (2*h)
    return np.array([G1, G2])


def grad_F_analitic(x, y, F, h):
    
    if F == F1:
        grad_x = 2*x - 2 
        grad_y = 2*y - 4  
    elif F == F2:
        grad_x = 6*x - 12  
        grad_y = 4*y + 16 
    elif F == F3:
        grad_x = 2*x - 4*y  
        grad_y = -4*x + 10*y - 4 
    elif F == F4:
        grad_x = 2*x*y - 2*y**2 + 3*y  
        grad_y = x**2 - 4*x*y + 3*x 
        
    return np.array([grad_x, grad_y])




def calculate_eta(x, y, F, grad_F, beta):
    eta = 1
    p = 1

    grad = grad_F(x, y, F, 10**(-5))
    
    while p < 8 and F(x - grad[0], y - grad[1]) > F(x, y) - (eta/2) * ((grad[0]**2) + grad[1]**2 ) :
            eta *= beta
            p += 1

    return eta




def optimization_algorithm(initial_point, F, grad_F, h, kmax, epsilon ,param_eta):
    
    x, y = initial_point
    k = 0

    while True:
        grad = grad_F(x, y, F, h)
        
        eta = calculate_eta(x, y, F, grad_F, 0.8)
        if eta is not None:
            eta = param_eta
        else:
            eta = calculate_eta(x, y, F, grad_F_approx, 0.8)
            
        x -= eta * grad[0]
        y -= eta * grad[1]
        
        k += 1
        
        if k > kmax or eta * np.linalg.norm(grad) < epsilon or eta * np.linalg.norm(grad) > 10**10 :
            break
    
    #return(x,y,k)

    if eta * np.linalg.norm(grad) < epsilon:
        return (x, y, k)
    else:
        return "divergenta"









def rulare():
    
    a = random.uniform(-500, 500)
    b = random.uniform(-500, 500)
    

    initial_point = [a, b]
    


    
    epsilon=10**(-5)
    h=10**(-6)
    kmax=30000
    
    functions = [F1, F2, F3, F4]
    
    for function in functions:
        print(f"\nFunctia obiectiva: {function.__name__}")

        result1 = optimization_algorithm(initial_point, function, grad_F_approx, h , kmax, epsilon, 10**(-3))
        print("Punct de minim pentru formula aproximativa:", result1)
        result2 = optimization_algorithm(initial_point, function, grad_F_analitic, h , kmax, epsilon, 10**(-3))
        print("Punct de minim pentru formula analitica:", result2)
    
    
    
    
rulare()
