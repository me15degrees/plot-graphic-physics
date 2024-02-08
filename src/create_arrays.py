import pandas as pd

velocidade = pd.read_csv("csv/velocidade.csv", sep=";")
velocidade.dropna(inplace=True)
xvel = pd.DataFrame(velocidade["x"]).values
yvel = pd.DataFrame(velocidade["velocidade"]).values

posicao = pd.read_csv("csv/posicao.csv", sep=";")
posicao.dropna(inplace=True)
xpos = pd.DataFrame(posicao["x"]).values
ypos = pd.DataFrame(posicao["Posicao"]).values

aceleracao = pd.read_csv("csv/aceleracao.csv", sep=";")
aceleracao.dropna(inplace=True)
xace = pd.DataFrame(aceleracao["x"]).values
yace = pd.DataFrame(aceleracao["Aceleracao"]).values
