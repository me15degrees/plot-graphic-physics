import numpy as np
import matplotlib.pyplot as plt
import create_arrays as cta
from rich_menu import Menu

def menu():
    menu = Menu(
        "Gráfico 1 - s(t)",
        "Gráfico 2 - v(t)",
        "Gráfico 3 - a(t)",
        "Sair",
        color="bold purple",
        rule_title="Física I",
        align="center",
        panel_title="Escolha a modalidade",
        selection_char="->",
    )
    selected = menu.ask(screen=False)
    if selected == "Sair":
        exit()
    return selected

def trapezoidal_integration(x, y):
    n = len(x)
    area = 0
    for i in range(1, n):
        delta_x = x[i] - x[i-1]
        avg_height = (y[i] + y[i-1]) / 2
        area += delta_x * avg_height
    return area


def plot_position():

    x_points = cta.xpos
    y_points = cta.ypos

    x, y = zip(*sorted(zip(x_points, y_points)))

    area = trapezoidal_integration(x, y)

    plt.plot(x, y, 'bo-', label='Pontos de Dados')

    plt.title('Integração Numérica com Método do Trapézio')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()


    plt.show()

def plot_velocity():

    x_points = cta.xvel
    y_points = cta.yvel

    x, y = zip(*sorted(zip(x_points, y_points)))

    plt.plot(x, y, 'bo-', label='Pontos de Dados')

    plt.title('Integração Numérica com Método do Trapézio')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()

    plt.show()

def plot_acceleration():
    # Pontos fornecidos
    x_points = cta.xace
    y_points = cta.yace

    x, y = zip(*sorted(zip(x_points, y_points)))

    plt.plot(x, y, 'bo-', label='Pontos de Dados')

    plt.title('Integração Numérica com Método do Trapézio')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()

    plt.show()

def main():
   
    while True:
        selection = menu()

        if selection == "Gráfico 1 - s(t)":
            plot_position()
        elif selection == "Gráfico 2 - v(t)":
            plot_velocity()
        elif selection == "Gráfico 3 - a(t)":
            plot_acceleration()

if __name__ == "__main__":
    main()