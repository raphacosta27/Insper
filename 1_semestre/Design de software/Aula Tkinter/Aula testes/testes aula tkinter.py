import tkinter as tk

def diz_oi():
    print("Olá")
    
window = tk.Tk()

botão = tk.Button(window)
botão.configure(text = "Diga oi!")
botão.configure(command = diz_oi)  #Callback
botão.grid()    #plt.show()

window.mainloop()