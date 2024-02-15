import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import create_arrays as cta
from rich_menu import Menu


fig, ax = plt.subplots(figsize=(19.2, 10.8), dpi=100)


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
        delta_x = x[i] - x[i - 1]
        avg_height = (y[i] + y[i - 1]) / 2
        area += delta_x * avg_height
    return area


def plot_position(plot=False):
    x_points = cta.xpos
    y_points = cta.ypos

    x, y = zip(*sorted(zip(x_points, y_points)))

    area = trapezoidal_integration(x, y)
    ax.clear()
    ax.plot(x, y, "bo-", label="Pontos de Dados")

    ax.set_title("Integração Numérica com Método do Trapézio")
    ax.text(
        0.5,
        0.95,
        f"Área: {area[0]:.2f}",
        ha="center",
        va="center",
        fontsize=11,
        fontweight="bold",
        color="blue",
        transform=ax.transAxes,
    )
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend()

    if plot:
        plt.show()


def plot_velocity(plot=False):
    x_points = cta.xvel
    y_points = cta.yvel

    x, y = zip(*sorted(zip(x_points, y_points)))
    area = trapezoidal_integration(x, y)

    ax.clear()
    ax.plot(x, y, "bo-", label="Pontos de Dados")

    ax.set_title("Integração Numérica com Método do Trapézio")
    ax.text(
        0.5,
        0.20,
        f"Área: {area[0]:.2f}",
        ha="center",
        va="center",
        fontsize=11,
        fontweight="bold",
        color="blue",
        transform=ax.transAxes,
    )
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend()

    if plot:
        plt.show()


def plot_acceleration(plot=False):
    # Pontos fornecidos
    x_points = cta.xace
    y_points = cta.yace

    x, y = zip(*sorted(zip(x_points, y_points)))
    area = trapezoidal_integration(x, y)

    ax.clear()
    ax.plot(x, y, "bo-", label="Pontos de Dados")

    ax.set_title("Integração Numérica com Método do Trapézio")
    ax.text(
        0.5,
        0.95,
        f"Área: {area[0]:.2f}",
        ha="center",
        va="center",
        fontsize=11,
        fontweight="bold",
        color="blue",
        transform=ax.transAxes,
    )
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend()

    if plot:
        plt.show()


def main():
    selection = menu()

    if selection == "Gráfico 1 - s(t)":
        plot_position(True)
    elif selection == "Gráfico 2 - v(t)":
        plot_velocity(True)
    elif selection == "Gráfico 3 - a(t)":
        plot_acceleration(True)


def selec(selection):
    if selection == 1:
        plot_position()
    elif selection == 2:
        plot_velocity()
    elif selection == 3:
        plot_acceleration()


if __name__ == "__main__":
    main()