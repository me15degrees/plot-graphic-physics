from sympy import symbols, diff

def find_functions(acc_values, time_intervals, pos_values):
    t, v0, s0 = symbols("t v0 s0")

    size = len(acc_values)

    for i in range(size):
        # Encontrar a função de aceleração e velocidade a partir da posição
        Vd_t, Ad_t = differentiate(pos_values[i], t, v0, s0)

        print(f"\nIntervalo que começa em {time_intervals[i][0]}s e termina em {time_intervals[i][1]}s:")
        print(f"Posição: {pos_values[i]}")
        print(f"Velocidade: {Vd_t}")
        print(f"Aceleração: {Ad_t}")


def differentiate(value, t, v0, s0):
    Vd_t = diff(value, t) + v0
    Ad_t = diff(Vd_t, t) + s0

    return Vd_t, Ad_t


def main():
    # Inserir aqui os valores de aceleração, tempo e posição
    acc_values = [0, 2, 0, -4, 0]
    time_intervals = [(0, 1), (1, 3), (3, 8), (8, 9), (9, 10)]
    pos_values = [0, 0, 4, 8, 26]

    find_functions(acc_values, time_intervals, pos_values)

main()
