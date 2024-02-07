import numpy as np
from scipy.stats import linregress
import matplotlib.pyplot as plt

arquivo_dados = 'dados_combustivel.csv'

dados = np.genfromtxt(arquivo_dados, delimiter=',', names=True)



for name in dados.dtype.names[1:]:
    regressao = linregress(dados['x'], dados[name])
    print(f"Regressão para {name}: R^2={regressao.rvalue**2:.4f} e stderr={regressao.stderr:.4f}")



print(dados.dtype.names)