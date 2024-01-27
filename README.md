# Introdução à Cinemática

Na Física, a posição de um objeto pode ser descrita em função do tempo, podendo ser representada por uma função s(t). Vale ressaltar que o tempo é uma grandeza independente, visto que pode variar independentemente das outras variáveis.

A velocidade é entendida como a taxa de variação da posição, também em relação ao tempo, sendo representada por uma função como v(t). Matematicamente, a velocidade v(t) é a derivada da posição s(t) em relação ao tempo (t). Isto é, a velocidade instantânea em um determinado momento é dada pela inclinação da tangente à curva da posição em relação ao tempo.

A aceleração é a taxa de variação da velocidade em relação ao tempo. Matematicamente, a aceleração a(t) é a derivada da velocidade v(t) em relação ao tempo (t). Da mesma forma, a aceleração em um determinado momento é dada pela inclinação da tangente à curva da velocidade em relação ao tempo.

Também é possível realizar o processo inverso, usando a integral para reconstituir as transformações, sendo a constante uma grandeza inicial.

##

### Sobre o código
O trabalho está dividido em 3 arquivos .py: 
O `plot-graphic.py`é usa as bibliotecas do *sympy* e *matplotlib* para imprimir os gráficos de s(t), v(t)e a(t), por meio dos dados existentes dos pontos do gráfico de velocidade.

O `all_differentiate.py` é responsável por impirimir com formatação as funções derivadas de s(t) para v(t), e de v(t) para a(t).

Já o `all_integrate.py` é responsável por impirimir com formatação as funções integradas de a(t) para v(t), e de v(t) para s(t).

