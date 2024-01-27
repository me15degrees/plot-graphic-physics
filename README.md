# Introdução à Cinemática

Na Física, a posição de um objeto pode ser descrita em função do tempo, podendo ser representada por uma função s(t). Vale ressaltar que o tempo é uma grandeza independente, visto que pode variar independentemente das outras variáveis.

A velocidade é entendida como a taxa de variação da posição, também em relação ao tempo, sendo representada por uma função como v(t). Matematicamente, a velocidade v(t) é a derivada da posição s(t) em relação ao tempo (t). Isto é, a velocidade instantânea em um determinado momento é dada pela inclinação da tangente à curva da posição em relação ao tempo.

A aceleração é a taxa de variação da velocidade em relação ao tempo. Matematicamente, a aceleração a(t) é a derivada da velocidade v(t) em relação ao tempo (t). Da mesma forma, a aceleração em um determinado momento é dada pela inclinação da tangente à curva da velocidade em relação ao tempo.

Também é possível realizar o processo inverso, usando a integral para reconstituir as transformações, sendo a constante uma grandeza inicial.

##

### Sobre o código
O trabalho está dividido em 3 arquivos .py: 

O `plot-graphic.py` usa as bibliotecas do *numpy*, *matplotlib* e *rich menu* para plotar os gráficos de s(t), v(t)e a(t), por meio dos dados existentes e criar um menu iterativo. O gráfico é criado a partir da integração em relação ao tempo da função de aceleração, passando os pontos fornecidos por ela, para achar a função de velocidade para o mesmo intervalo de tempo, e assim por diante.


```
Para encontrar a integral da função de velocidade v = a⋅(t−t0)+v0, você deve integrar em relação ao tempo t.

Lembre-se de que a constante de integração é necessária ao realizar a integração.

Vamos calcular a integral:

∫v dt=∫(a⋅(t−t0)+v0) dt

Ao realizar a integração, obtemos:

s(t)=a/2(t−t0)²+v0⋅(t−t0)+s0

Onde s(t) é a função de posição, s0​ é a constante de integração que dependerá das condições iniciais.

Portanto, a integral da função de velocidade v = a⋅(t−t0)+v0 em relação ao tempo t é a função de posição s(t) dada pela fórmula acima.
```

O `all_differentiate.py` é responsável por impirimir com formatação as funções derivadas de s(t) para v(t), e de v(t) para a(t).

Já o `all_integrate.py` é responsável por impirimir com formatação as funções integradas de a(t) para v(t), e de v(t) para s(t).

