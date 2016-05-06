# -*- coding: utf-8 -*-

import tkinter as tk

class MeuAplicativo:
    
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Meu primeiro aplicativo!")
        
        botão = tk.Button(self.window)
        botão.configure(text="Diga oi!")
        botão.configure(command=self.diz_oi)
        botão.grid()
        
    def iniciar(self):
        self.window.mainloop()
    
    def diz_oi(self):
        print("Oi gente!")

app = MeuAplicativo()
app.iniciar()
