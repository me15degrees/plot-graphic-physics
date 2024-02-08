import numpy as np
import matplotlib.pyplot as plt
import create_arrays as cta

# Função para calcular a área sob a curva usando o método do trapézio
def trapezoidal_integration(x, y):
    n = len(x)
    area = 0
    for i in range(1, n):
        delta_x = x[i] - x[i-1]
        avg_height = (y[i] + y[i-1]) / 2
        area += delta_x * avg_height
    return area

# Pontos fornecidos
x_points = cta.xpos
y_points = cta.ypos


# Ordenar os pontos em ordem crescente de coordenada x
sorted_indices = np.argsort(x_points)
x, y = zip(*sorted(zip(x_points, y_points)))

# Calcular a área sob a curva
area = trapezoidal_integration(x, y)

# Plotar os pontos
plt.plot(x_points, y_points, 'bo-', label='Pontos de Dados')


# Adicionar rótulos e legendas
plt.title('Integração Numérica com Método do Trapézio')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

# Exibir o gráfico
plt.show()
