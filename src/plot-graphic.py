import matplotlib.pyplot as plt
import numpy as np
from rich_menu import Menu

def menu():
    menu = Menu(
        "Gráfico 1 - s(t)",
        "Gráfico 2 - v(t)",
        "Gráfico 3 - a(t)",
        "Todos",
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

def s_t(a, t0, s0, v0, t_values):
    """Calcula a posição em função do tempo"""
    return 0.5 * a * (t_values - t0)**2 + v0 * (t_values - t0) + s0

def v_t(v0, t0, a, t_values):
    """Calcula a velocidade em função do tempo"""
    return a * (t_values - t0) + v0

def plot_s_t(a, t0, s0, v0, interval):
    """Plota o gráfico de posição em função do tempo"""
    plt.figure(num=0, dpi=120)

    s0_list = [s0]
    for i, (t0_i, v0_i, a_i) in enumerate(zip(t0, v0, a)):
        t_values = np.linspace(interval[i][0], interval[i][1], 100)
        s_values = s_t(a_i, t0_i, s0_list[-1], v0_i, t_values)
        s0_list.append(s_values[-1])
        plt.plot(t_values, s_values, label=f"Intervalo {i+1}", color="blue")

    plt.legend()
    plt.xlabel("Tempo")
    plt.ylabel("Posição")
    plt.show()

    return s_values

def plot_v_t(v0, t0, a, interval):
    """Plota o gráfico de velocidade em função do tempo"""
    plt.figure(num=0, dpi=120)

    for i, (t0_i, v0_i, a_i) in enumerate(zip(t0, v0, a)):
        t_values = np.linspace(interval[i][0], interval[i][1], 100)
        v_values = v_t(v0_i, t0_i, a_i, t_values)
        plt.plot(t_values, v_values, label=f"Intervalo {i+1}", color="pink")
    plt.legend()
    plt.xlabel("Tempo")
    plt.ylabel("Velocidade")
    plt.show()

    return v_values

def plot_a_t(intervals, constants, ylabel="Aceleração"):
    """Plota o gráfico de aceleração em função do tempo"""
    plt.figure(num=0, dpi=120)

    for i, (interval, const_value) in enumerate(zip(intervals, constants)):
        plt.hlines(const_value, interval[0], interval[1], label=f"Intervalo {i+1}", color="orange")
        if i < len(intervals) - 1:
            next_interval = intervals[i + 1]
            plt.plot([interval[1], next_interval[0]], [const_value, constants[i + 1]], color="orange")

    plt.legend()
    plt.xlabel("Tempo")
    plt.ylabel(ylabel)
    plt.show()

def main():
    size = 5
    t0 = [0, 1, 3, 8, 9]
    v0 = [0, 0, 4, 4, 0]
    a = [0, 2, 0, -4, 0]
    interval = [(0, 1), (1, 3), (3, 8), (8, 9), (9, 10)]

    while True:
        selection = menu()

        if selection == "Gráfico 1 - s(t)":
            plot_s_t(a, t0, 0, v0, interval)
            
        elif selection == "Gráfico 2 - v(t)":
            plot_v_t(v0, t0, a, interval)

        elif selection == "Gráfico 3 - a(t)":
            plot_a_t(interval, a, ylabel="Aceleração")

        elif selection == "Todos":
            plt.figure(num=0, dpi=120)

            for i, (t0_i, v0_i, a_i) in enumerate(zip(t0, v0, a)):
                t_values = np.linspace(interval[i][0], interval[i][1], 100)
                s_values = s_t(a_i, t0_i, 0, v0_i, t_values)
                plt.plot(t_values, s_values, label=f"Intervalo {i+1} - Posição", color="blue")

                v_values = v_t(v0_i, t0_i, a_i, t_values)
                plt.plot(t_values, v_values, label=f"Intervalo {i+1} - Velocidade", color="red")

            plt.legend()
            plt.show()

if __name__ == "__main__":
    main()
