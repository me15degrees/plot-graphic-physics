import matplotlib.pyplot as plt
import numpy as np
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


def s_t(a, t0, s0, v0, t_values):
    """Calcula a posição em função do tempo"""
    return 0.5 * a * (t_values - t0) ** 2 + v0 * (t_values - t0) + s0


def v_t(v0, t0, a, t_values):
    """Calcula a velocidade em função do tempo"""
    return a * (t_values - t0) + v0


def plot_s_t(a, t0, s0, v0, interval):
    """Plota o gráfico de posição em função do tempo"""
    largura = 10
    altura = 6
    plt.figure(num=0, figsize=(largura, altura), dpi=120)

    colors = plt.cm.viridis(np.linspace(0, 1, len(interval)))

    s0_list = [s0]

    for i, (t0_i, v0_i, a_i, color) in enumerate(zip(t0, v0, a, colors)):
        t_values = np.linspace(interval[i][0], interval[i][1], 100)
        s_values = s_t(a_i, t0_i, s0_list[-1], v0_i, t_values)
        s0_list.append(s_values[-1])
        plt.plot(t_values, s_values, label=f"Intervalo {i+1}", color=color)

    plt.legend()
    plt.xlabel("Tempo")
    plt.ylabel("Posição")
    plt.title("Gráfico 1 - Posição em função do tempo")
    plt.grid(True, linestyle="--", linewidth=0.5, color="gray", alpha=0.7)
    plt.show()

    return s_values


def plot_v_t(v0, t0, a, interval):
    """Plota o gráfico de velocidade em função do tempo"""
    largura = 10
    altura = 6
    plt.figure(num=0, figsize=(largura, altura), dpi=120)

    colors = plt.cm.viridis(np.linspace(0, 1, len(interval)))

    for i, (t0_i, v0_i, a_i, color) in enumerate(zip(t0, v0, a, colors)):
        t_values = np.linspace(interval[i][0], interval[i][1], 100)
        v_values = v_t(v0_i, t0_i, a_i, t_values)
        plt.plot(t_values, v_values, label=f"Intervalo {i+1}", color=color)
    plt.legend()
    plt.xlabel("Tempo")
    plt.ylabel("Velocidade")
    plt.title("Gráfico 2 - Velocidade em função do tempo")
    plt.grid(True, linestyle="--", linewidth=0.5, color="gray", alpha=0.7)
    plt.show()

    return v_values


def plot_a_t(intervals, constants, ylabel="Aceleração"):
    """Plota o gráfico de aceleração em função do tempo"""
    largura = 10
    altura = 6
    plt.figure(num=0, figsize=(largura, altura), dpi=120)

    # Paleta de cores do Matplotlib
    colors = plt.cm.viridis(np.linspace(0, 1, len(intervals)))

    for i, (interval, const_value, color) in enumerate(
        zip(intervals, constants, colors)
    ):
        plt.hlines(
            const_value, interval[0], interval[1], color=color, label=f"Intervalo {i+1}"
        )
        if i < len(intervals) - 1:
            next_interval = intervals[i + 1]
            plt.plot(
                [interval[1], next_interval[0]],
                [const_value, constants[i + 1]],
                color=color,
            )

    plt.legend()
    plt.xlabel("Tempo")
    plt.ylabel(ylabel)
    plt.title("Gráfico 3 - Aceleração em função do tempo")
    plt.grid(True, linestyle="--", linewidth=0.5, color="gray", alpha=0.7)
    plt.show()


def main():
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


if __name__ == "__main__":
    main()
