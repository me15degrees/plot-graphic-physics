import matplotlib.pyplot as plt
import numpy as np

def integrate_acc_to_vel(v0,t0,a,t):
    v = a * (t - t0) + v0
    vel_function = print(f"v(t) = {v0} + {a} * (t - {t0})")
    
    return v, vel_function


def integrate_vel_to_pos(s0,t0,v,t):
    s = v * (t-t0) + s0
    pos_function = print(f"s(t) = {s0} + {v} * (t - {t0})")
    
    return s, pos_function


def main():
    t0 = [0,1,3,8,9] # condição inicial de tempo
    v0 = [0,0,4,4,0] # condição inicial de velocidade
    s0 = [0,1,4,24,26] # condição inicial de posição
    a = [0,2,0,-4,0] 
    
    size = 5
    
    interval = [(0,1),(1,3),(3,8),(8,9),(9,10)] # intervalos de tempo
    
    v = []
    s = []
    
    for i in range(size):
        print(f"\nPara o intervalo {i}: ")
        print(f"a(t) = {a[i]}")
        vf, _ = integrate_acc_to_vel(v0[i],t0[i],a[i],interval[i][1])
        v.append(vf)
        sf, _ = integrate_vel_to_pos(s0[i],t0[i],v[i],interval[i][1])
        s.append(sf)

main()
