import customtkinter as ctk
import old_plot_graphic as plotgr
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure

def selec():
    ax = plotgr.selec(1)
    canvas.draw()
def selectwo():
    ax = plotgr.selec(2)
    canvas.draw()
def selecttree():
    ax = plotgr.selec(3)
    canvas.draw()
    
text_description = """  Nesse trabalho foi instruído para que aplicasse a parte conceitual da
    cinemática sobre as grandezas de velocidade, aceleração e posição do objeto. Segue um breve
    resumo do que foi levado em consideração para traçar posteriormente o raciocínio do código:
    
	    Na física, baseando-se em um referencial específico, é possível determinar a posição de uma
    partícula no espaço e, a partir da variação dessa posição, calcular seu deslocamento. A função
    horária do espaço proporciona a capacidade de encontrar a posição de uma partícula em um
    determinado intervalo de tempo quando esta se move de maneira uniforme, com aceleração constante.
    
	    A velocidade é compreendida como a taxa de variação da posição em relação ao tempo.
    Sua própria função horária pode ser derivada da função horária do espaço, funcionando de
    maneira análoga a ela, determinando a taxa de variação da posição de uma partícula em um
    período específico. Caso seja sabido a função da s(t), ao derivar ela, tem-se a função de v(t).
    
	Ao realizar a segunda derivada da função posição, obtemos a taxa de variação da velocidade 
    em relação ao tempo, conhecida como aceleração. O processo para obter as funções horárias pode
    ser invertudo e, por meio da integração, é possível se obter a função tanto da velocidade quanto
    da posição por meio da aceleração da particula."""
students = """João Vitor Ramos Mitidiero\nMaria Eduarda Nascimento Andrade\nGabriel Henrique Silva Cardoso"""
 
window = ctk.CTk()
window.title("Gráficos P.V.A. de um elevador - Física Básica: Mecânica")
window.geometry("1050x600")
window._set_appearance_mode("dark")
window.resizable(width = True, height = True)

title_one = ctk.CTkLabel(window,
                            text = "GRANDEZAS FÍSICAS EM UM ELEVADOR",
                            font = ("arial bold", 20),
                            text_color="white",
                            fg_color="#242424",
                            bg_color="#242424"
                            )
title_one.pack(pady=15,padx=5)

tabview = ctk.CTkTabview(window,
                         width=1920,
                         height= 1080,
                         fg_color="grey",
                         bg_color="#242424")
tabview.pack(padx = 10, pady = 10)
tabview.add("Gráficos")
tabview.add("Descrição")

frame_descr = ctk.CTkFrame(tabview.tab("Descrição"),
                            width = 700,
                            height = 700,
                            fg_color="#242424")
frame_descr.pack(side=ctk.LEFT, pady = 20, padx = 20)

frame_inter = ctk.CTkFrame(tabview.tab("Descrição"),
                           width=700,
                           height= 700,
                            fg_color="#242424")
frame_inter.pack(side=ctk.RIGHT, pady = 20, padx = 20)

description = ctk.CTkLabel(frame_descr,
                            text = text_description,
                            font = ("arial", 12),
                            width = 700,
                            height = 700,
                            text_color="white")
description.pack(pady=15,padx=5)

integra = ctk.CTkLabel(frame_inter,
                            text = students,
                            font = ("arial", 12),
                            width = 700,
                            height = 700,
                            text_color="white")
integra.pack(pady=15,padx=5)

frame_btn = ctk.CTkFrame(tabview.tab("Gráficos"),
                            width = 1920,
                            height = 1080,
                            fg_color="grey")
frame_btn.pack(side=ctk.LEFT, pady = 20, padx = 20)
    
frame_graph = ctk.CTkFrame(tabview.tab("Gráficos"),
                            fg_color="white")
frame_graph.pack(padx=10,pady=5)

instruction = ctk.CTkLabel(tabview.tab("Gráficos"),
                               text = "Selecione uma opção de gráfico abaixo:")
instruction.pack(padx=10,pady=0)

btn_1 = ctk.CTkButton(frame_btn,
                        width=150,
                        text = "Gráfico 1 - Posição",
                        command=selec)
btn_1.pack(pady=30, padx=25)

btn_2 = ctk.CTkButton(frame_btn,
                        width=150,
                        text = "Gráfico 2 - Velocidade",
                        command=selectwo)
btn_2.pack(pady=30, padx=25)

btn_3 = ctk.CTkButton(frame_btn,
                        width=150,
                        text = "Gráfico 3 - Aceleração",
                        command=selecttree)
btn_3.pack(pady=30, padx=25)

fig = plotgr.fig

canvas = FigureCanvasTkAgg(fig, master=frame_graph)
toolbar = NavigationToolbar2Tk(canvas,
                                frame_graph,
                                pack_toolbar=False)
toolbar.update()  
toolbar.pack(side=ctk.BOTTOM,pady= 10, padx = 10)
canvas.get_tk_widget().pack(pady=10,padx=10)

window.mainloop()




