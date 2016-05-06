# -*- coding: utf-8 -*-

import tkinter as tk

def diz_oi():
    print("Oi gente!")

window = tk.Tk()

botão = tk.Button(window)
botão.configure(text="Diga oi!")
botão.configure(command=diz_oi)
botão.grid()

window.mainloop()

