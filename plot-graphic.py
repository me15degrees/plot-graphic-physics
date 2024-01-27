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


def st(a, t0, s0, v0, t_values):
    """position by time"""
    s_values = 0.5 * a * (t_values - t0) ** 2 + v0 * (t_values - t0) + s0
    return s_values


def vt(v0, t0, a, t_values):
    v_values = a * (t_values - t0) + v0
    return v_values, a


def plot_acc(intervals, constants, ylabel="Aceleração"):
    plt.figure(num=0, dpi=120)

    for i, interval in enumerate(intervals):
        const_value = constants[i]
        plt.hlines(
            const_value,
            interval[0],
            interval[1],
            label=f"Intervalo {i+1}",
            color="orange",
        )
        if i < len(intervals) - 1:
            next_interval = intervals[i + 1]
            plt.plot(
                [interval[1], next_interval[0]],
                [const_value, constants[i + 1]],
                color="orange",
            )
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
            plt.figure(num=0, dpi=120)

            s0 = [0]
            for i in range(size):
                t_values = np.linspace(interval[i][0], interval[i][1], 10)
                s_values = st(a[i], t0[i], s0[i], v0[i], t_values)
                s0.append(s_values[-1])
                plt.plot(t_values, s_values, label=f"Intervalo {i+1}", color="blue")

            plt.legend()
            plt.xlabel("Tempo")
            plt.ylabel("Posição")
            plt.show()

        elif selection == "Gráfico 2 - v(t)":
            plt.figure(num=0, dpi=120)

            for i in range(size):
                t_values = np.linspace(interval[i][0], interval[i][1], 10)
                v_values, _ = vt(v0[i], t0[i], a[i], t_values)
                plt.plot(t_values, v_values, label=f"Intervalo {i+1}", color="blue")

            plt.legend()
            plt.xlabel("Tempo")
            plt.ylabel("Velocidade")
            plt.show()

        elif selection == "Gráfico 3 - a(t)":
            plot_acc(interval, a, ylabel="Aceleração")

        elif selection == "Todos":
            plt.figure(num=0, dpi=120)

            s0 = [0]
            for i in range(size):
                t_values = np.linspace(interval[i][0], interval[i][1], 10)
                s_values = st(a[i], t0[i], s0[i], v0[i], t_values)
                s0.append(s_values[-1])
                plt.plot(t_values, s_values, label=f"Intervalo {i+1}", color="blue")

            for i in range(size):
                t_values = np.linspace(interval[i][0], interval[i][1], 10)
                v_values, _ = vt(v0[i], t0[i], a[i], t_values)
                plt.plot(t_values, v_values, label=f"Intervalo {i+1}", color="red")

            plt.legend()
            plt.show()


if __name__ == "__main__":
    main()
