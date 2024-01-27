from sympy import symbols, integrate

def find_functions(acc_values, time_intervals):
    t, v0, s0 = symbols("t v0 s0")

    size = len(acc_values)

    for i in range(size):
        # Encontrar a função de velocidade e posição a partir da aceleração
        Vi_t, Si_t = integrate_acc_to_pos(acc_values[i], t, v0, s0, time_intervals[i])

        print(f"\nIntervalo que começa em {time_intervals[i][0]}s e termina em {time_intervals[i][1]}s:")
        print(f"a(t) = {acc_values[i]}")
        print(f"v(t) = {Vi_t}")
        print(f"s(t) = {Si_t}")


def integrate_acc_to_pos(acceleration, t, v0, s0, time_interval):
    # Calcular os valores iniciais de velocidade (v0) e posição (s0) para o intervalo de tempo
    v0_val = integrate(acceleration, t).subs(t, time_interval[0]) + v0
    s0_val = integrate(v0_val, t).subs(t, time_interval[0]) + s0
    # Integrar para obter as funções de velocidade e posição
    Vi_t = integrate(acceleration, t) + v0_val
    Si_t = integrate(Vi_t, t) + s0_val

    return Vi_t, Si_t


def main():
    # Inserir aqui os valores de aceleração, tempo e posição
    acc_values = [0, 2, 0, -4, 0]
    time_intervals = [(0, 1), (1, 3), (3, 8), (8, 9), (9, 10)]

    find_functions(acc_values, time_intervals)


main()
pos_values = [0, 0, 4, 8, 26]