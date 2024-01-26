import matplotlib.pyplot as plt
import numpy as np
from rich_menu import Menu

def menu():
    menu = Menu(
        "Gráfico 1 - s(t)",
        "Gráfico 2 - v(t)",
        "Gráfico 3 - a(t)" ,
        color="bold purple",
        rule_title="Física I",
        align="center",
        panel_title="escolha a modalidade",
        selection_char="->",
    )
    selected = menu.ask(screen=False)
    return selected

def vt(v0, t0, a, t):
    v = a * (t - t0) + v0
    return v, a  # Agora retorna a velocidade e a aceleração

def plot_const_functions(intervals, constants, ylabel="Y"):
    plt.figure(num=0, dpi=120)

    for i, interval in enumerate(intervals):
        t_values = np.linspace(interval[0], interval[1], 100)
        const_value = constants[i]
        plt.hlines(const_value, interval[0], interval[1], label=f'Intervalo {i+1}')
        if i < len(intervals) - 1:
            next_interval = intervals[i+1]
            plt.plot([interval[1], next_interval[0]], [const_value, constants[i+1]], color='blue')

    plt.legend()
    plt.xlabel('Tempo')
    plt.ylabel(ylabel)
    plt.show()

def main():
    size = 5
    t0 = [0, 1, 3, 8, 9]  # condição inicial de tempo
    v0 = [0, 0, 4, 4, 0]  # condição inicial de velocidade
    a = [0, 2, 0, -4, 0]
    interval = [(0, 1), (1, 3), (3, 8), (8, 9), (9, 10)]

    selection = menu()

    if selection == "Gráfico 1 - s(t)":
        # Lógica para o Gráfico 1 - s(t)
        pass

    elif selection == "Gráfico 2 - v(t)":
        plt.figure(num=0, dpi=120)

        for i in range(size):
            t_values = np.linspace(interval[i][0], interval[i][1], 10)
            v_values, _ = vt(v0[i], t0[i], a[i], t_values)
            plt.plot(t_values, v_values, label=f'Intervalo {i+1}')

        plt.legend()
        plt.xlabel('Tempo')
        plt.ylabel('Velocidade')
        plt.show()

    elif selection == "Gráfico 3 - a(t)":
        plot_const_functions(interval, a, ylabel="Y")

if __name__ == "__main__":
    main()
