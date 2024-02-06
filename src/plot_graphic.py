from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np

largura = 19.2
altura = 10.8
fig = Figure(figsize=(largura,altura),dpi=100)
ax = fig.add_subplot()

def s_t(a, t0, s0, v0, t_values):
    """Calcula a posição em função do tempo"""
    return 0.5 * a * (t_values - t0)**2 + v0 * (t_values - t0) + s0

def v_t(v0, t0, a, t_values):
    """Calcula a velocidade em função do tempo"""
    return a * (t_values - t0) + v0

def plot_s_t(a, t0, s0, v0, interval):
    """Plota o gráfico de posição em função do tempo"""
    ax.clear()
    colors = plt.cm.viridis(np.linspace(0, 1, len(interval)))

    s0_list = [s0]

    for i, (t0_i, v0_i, a_i, color) in enumerate(zip(t0, v0, a, colors)):
        t_values = np.linspace(interval[i][0], interval[i][1], 100)
        s_values = s_t(a_i, t0_i, s0_list[-1], v0_i, t_values)
        s0_list.append(s_values[-1])
        ax.plot(t_values, s_values, label=f"Intervalo {i+1}", color=color)
    ax.legend()
    ax.set_xlabel("Tempo")
    ax.set_ylabel("Posição")
    ax.set_title("Gráfico 1 - Posição em função do tempo")
    ax.grid(True, linestyle='--', linewidth=0.5, color='gray', alpha=0.7)
    ax.scatter([0.5,3,8,9.8],[0,4,24,26]).set_color("black")
    return ax

def plot_v_t(v0, t0, a, interval):
    """Plota o gráfico de velocidade em função do tempo"""
    ax.clear()
    colors = plt.cm.viridis(np.linspace(0, 1, len(interval)))

    for i, (t0_i, v0_i, a_i, color) in enumerate(zip(t0, v0, a, colors)):
        t_values = np.linspace(interval[i][0], interval[i][1], 100)
        v_values = v_t(v0_i, t0_i, a_i, t_values)
        ax.plot(t_values, v_values, label=f"Intervalo {i+1}", color=color)
    ax.legend()
    ax.set_xlabel("Tempo")
    ax.set_ylabel("Velocidade")
    ax.set_title("Gráfico 2 - Velocidade em função do tempo")
    ax.grid(True, linestyle='--', linewidth=0.5, color='gray', alpha=0.7)
    
    return ax

def plot_a_t(intervals, constants, ylabel="Aceleração"):
    """Plota o gráfico de aceleração em função do tempo"""
    ax.clear()
     #Paleta de cores do Matplotlib
    colors = plt.cm.viridis(np.linspace(0, 1, len(intervals)))
    for i, (interval, const_value, color) in enumerate(zip(intervals, constants, colors)):
        ax.hlines(const_value, interval[0], interval[1], color=color, label=f"Intervalo {i+1}")
        if i < len(intervals) - 1:
            next_interval = intervals[i + 1]
            ax.plot([interval[1], next_interval[0]], [const_value, constants[i + 1]], color=color)

    ax.legend()
    ax.set_xlabel("Tempo")
    ax.set_ylabel(ylabel)
    ax.set_title("Gráfico 3 - Aceleração em função do tempo")
    ax.grid(True, linestyle='--', linewidth=0.5, color='gray', alpha=0.7)
    

def selec(selection):
    size = 5
    t0 = [0, 1, 3, 8, 9]
    v0 = [0, 0, 4, 4, 0]
    a = [0, 2, 0, -4, 0]
    interval = [(0, 1), (1, 3), (3, 8), (8, 9), (9, 10)]

    if selection == 1:
        plot_s_t(a, t0, 0, v0, interval)
            
    elif selection == 2:
        plot_v_t(v0, t0, a, interval)

    elif selection == 3:
        plot_a_t(interval, a, ylabel="Aceleração")
