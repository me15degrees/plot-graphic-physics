import customtkinter as ctk
import plot_graphic as plotgr
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

  
window = ctk.CTk()
window.title("Gráficos P.V.A. de um elevador - Física Básica: Mecânica")
window.geometry("1050x600")
window._set_appearance_mode("dark")
window.resizable(width = True, height = True)

title_one = ctk.CTkLabel(window,
                            text = "GRANDEZAS FÍSICAS EM UM ELEVADOR",
                            font = ("arial bold", 20))
title_one.pack(pady=15,padx=5)

tabview = ctk.CTkTabview(window,width=1920, height= 1080)
tabview.pack(padx = 10, pady = 10)
tabview.add("Gráficos")
tabview.add("Equações")
tabview.add("Descrição")

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




