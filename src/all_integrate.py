from sympy import symbols, integrate


def find_functions(acc_values, time_values):
    t, v0, s0 = symbols("t v0 s0")

    size = len(acc_values)

    for i in range(size):
        # Encontrar a função de velocidade e posição a partir da aceleração
        Vi_t, Si_t = integrate_acc_to_pos(acc_values[i], t, v0, s0)

        print(f"\nIntervalo que começa em {time_values[i]}s:")
        print(f"a(t) = {acc_values[i]}")
        print(f"v(t) = {Vi_t}")
        print(f"s(t) = {Si_t}")


def integrate_acc_to_pos(acceleration, t, v0, s0):
    Vi_t = integrate(acceleration, t) + v0
    Si_t = integrate(Vi_t, t) + s0

    return Vi_t, Si_t


def main():
    # Inserir aqui os valores de aceleração, tempo e posição
    acc_values = [0, 2, 0, -4, 0]
    interval = [(0, 1), (1, 3), (3, 8), (8, 9), (9, 10)]
    pos_values = [0, 0, 4, 8, 26]

    find_functions(time_values, pos_values)


main()
