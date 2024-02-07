from scipy.integrate import quad
import numpy as np

"""# Função de posição
def position_function(t):
    # Substitua esta função pela sua função de posição
    return t**2

# Função de velocidade
def velocity_function(t):
    # Substitua esta função pela sua função de velocidade
    return 2 * t"""

# Função de aceleração
def acceleration_function(acc):
    return acc

# Função para calcular a integral numérica
def calculate_integral(func, lower_limit, upper_limit):
    result, _ = quad(func, lower_limit, upper_limit)
    return result

# Definindo os limites de integração


def main():
    acc_values = [0, 2, 0, -4, 0]
    time_intervals = [(0, 1), (1, 3), (3, 8), (8, 9), (9, 10)]
    size = len(acc_values)
    
    for i in range(size):
        lower_limit = time_intervals[i][0]
        upper_limit = time_intervals[i][1]

    acceleration_integral = calculate_integral(acceleration_function, lower_limit, upper_limit)
    #velocity_integral = calculate_integral(velocity_function, lower_limit, upper_limit)
    #position_integral = calculate_integral(position_function, lower_limit, upper_limit)

    # Exibindo os resultados
    #print(f'Integral da função de posição: {position_integral}')
    #print(f'Integral da função de velocidade: {velocity_integral}')
    print(f'Integral da função de aceleração: {acceleration_integral}')
