import math
import numpy as np
import random
import sys

eps = 10**(-8)

def P1():
    return [1.0, -6.0, 11.0, -6.0]

def P2():
    return [1.0, -55.0/42.0, -1.0, 49.0/42.0, -6.0/42.0]

def P3():
    return  [1.0, -38.0/8.0, 49.0/8.0, -22.0/8.0, 3.0/8.0]

def P4():
    return [1.0, -6.0, 13.0, -12.0, 4.0]

def interval(P):
    return (np.abs(P[0]) + max(np.abs(P))) / np.abs(P[0])

def horner(P, x):
    n = len(P)
    rezultat = P[0]
    for i in range(1, n):
        rezultat = rezultat * x + P[i]
    return rezultat

def Muller(P, R, kmax):
    radacini = []
    stanga = -R
    crestere = 0.05
    
    while stanga <= R:
        x0 = random.uniform(stanga, stanga + crestere) 
        x1 = random.uniform(stanga, stanga + crestere) 
        x2 = random.uniform(stanga, stanga + crestere) 
        dx = 0
        flag = 0
        while True:
            k=3
            h0 = x1 - x0
            h1 = x2 - x1

            delta0 = (horner(P, x1) - horner(P, x0))/ h0
            delta1 = (horner(P, x2) - horner(P, x1))/ h1
            
            a = (delta0 - delta1) / (h1 + h0)
            b = a * h1 + delta1
            c = horner(P, x2)
            
            if b**2 - 4*a*c <0:
                break
            
            if b <= 0:
                semn = -1
                
            else:
                semn = 1
                
            dx = (2*c) / (b + semn * b * (b**2 - 4*a*c)**(0.5))
            
            x3 = x2 - dx
            k += 1
            
            x0 = x1
            x1 = x2
            x2 = x3
            
            flag = 1
            
            if np.abs(dx) < eps or k > kmax or np.abs(dx) > 10**(8):
                break
                
            
        if np.abs(dx) < eps and flag == 1:
            gasit = 0
            for rad in radacini:
                if np.abs(x3 - rad) < eps:
                    gasit = 1
                    break
            if gasit == 0:
                radacini.append(x3)
        stanga += crestere
    return radacini

def rulare():
    kmax = 300000
    x0=2
    x1=1
    x2=3
    initial_point = [x0, x1, x2]
    
    R = interval(P1())
    print(f"\nThe interval [-R,R] is: [{-R}, {R}]")
    radacini = Muller(P1(), R, kmax )
    # print(radacini)
    
    for rad in radacini:
        if np.abs(horner(P1(), rad)) < eps:
            print(horner(P1(), rad), "  ", rad)
            with open("roots.txt", "a") as file:
                file.write(str(rad) + " ")
    print(radacini)
    # print(horner(P1(), 4))

rulare()