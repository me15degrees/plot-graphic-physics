import numpy as np
import matplotlib.pyplot as plt
import create_arrays as cta
from matplotlib.figure import Figure

largura = 19.2
altura = 10.8
fig = Figure(figsize=(largura,altura),dpi=100)
ax = fig.add_subplot()

def trapezoidal_integration(x, y):
    n = len(x)
    area = 0
    for i in range(1, n):
        delta_x = x[i] - x[i-1]
        avg_height = (y[i] + y[i-1]) / 2
        area += delta_x * avg_height
    return area


def plot_position():

    ax.clear()
    
    x_points = cta.xpos
    y_points = cta.ypos

    x, y = zip(*sorted(zip(x_points, y_points)))

    area = trapezoidal_integration(x, y)

    ax.plot(x, y, 'bo-', label='Pontos de Dados')

    ax.set_title('Integração Numérica com Método do Trapézio')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.legend()

    return ax

def plot_velocity():

    ax.clear()
    
    x_points = cta.xvel
    y_points = cta.yvel

    x, y = zip(*sorted(zip(x_points, y_points)))

    ax.plot(x, y, 'bo-', label='Pontos de Dados')

    ax.set_title('Integração Numérica com Método do Trapézio')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.legend()

    return ax

def plot_acceleration():
    # Pontos fornecidos
    ax.clear()
    
    x_points = cta.xace
    y_points = cta.yace

    x, y = zip(*sorted(zip(x_points, y_points)))

    ax.plot(x, y, 'bo-', label='Pontos de Dados')

    ax.set_title('Integração Numérica com Método do Trapézio')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.legend()

    return ax

def selec(selection):
   
        if selection == 1:
            plot_position()
        elif selection == 2:
            plot_velocity()
        elif selection == 3:
            plot_acceleration()