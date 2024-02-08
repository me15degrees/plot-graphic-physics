import matplotlib.pyplot as plt
from scipy.integrate import simpson
import create_arrays as gd

def plot(x, y):

    if len(x) < 2 or len(y) < 2:
        print("Erro: Não há pontos suficientes para calcular a integral.")
        return

    x, y = zip(*sorted(zip(x, y)))
    
    plt.plot(x, y, 'bo-', label='Pontos de Dados')

    plt.title('Integração Numérica')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
  
    plt.legend()
   
    plt.show()

def main():
    all_points = [(gd.xvel, gd.yvel),(gd.xpos, gd.ypos),(gd.xace, gd.yace)]
    for i in range(3):
        plot(all_points[i][0], all_points[i][1])

if __name__ == "__main__":
    main()

 