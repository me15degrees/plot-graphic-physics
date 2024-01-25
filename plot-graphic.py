from sympy import symbols, integrate
import matplotlib.pyplot as plt
import numpy as np

def velocity_function(aceleracao, velocidade_inicial, t):
    t_sym = symbols('t')
    a = lambda t: aceleracao
    velocidade = velocidade_inicial + integrate(a(t_sym), t_sym)
    return velocidade

def plot_velocity_function(aceleracao, velocidade_inicial, intervalo):
    t_sym = symbols('t')
    a = lambda t: aceleracao
    velocidade = velocidade_inicial + integrate(a(t_sym), t_sym)

    # Criando uma função NumPy a partir da função simbólica
    velocity_np = np.vectorize(lambda t_val: velocidade.subs(t_sym, t_val).evalf())

    # Criando um array de valores de t para o intervalo dado
    t_values = np.linspace(intervalo[0], intervalo[1], 100)

    # Plotando a função
    plt.plot(t_values, velocity_np(t_values), label=f'a={aceleracao}, v0={velocidade_inicial}')

def main():
    v0 = [0, 0, 4, 4, 0]
    a = [0, 2, 0, -4, 0]
    t = [0, 1, 3, 8, 9]
    delta_t = [(0, 1), (1, 3), (3, 8), (8, 9), (9, 10)]
    size = len(v0)

    # Plotando as funções para cada intervalo
    for i in range(size):
        plot_velocity_function(a[i], v0[i], delta_t[i])

    # Adicionando legendas
    plt.legend()
    plt.xlabel('Tempo (t)')
    plt.ylabel('Velocidade (v)')
    plt.title('Funções de Velocidade')

    # Exibindo o gráfico
    plt.show()
