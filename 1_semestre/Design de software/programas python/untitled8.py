import tkinter as tk

class MainWindow:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("910x700+0+0")
       
        for i in range (0,7):       
            self.window.rowconfigure(i, weight = 1 )
        
        self.window.columnconfigure(0, weight = 1, minsize = 70)
        self.window.columnconfigure(1, weight = 1, minsize = 840)
            
        self.titulo = tk.Label(text = "Bem Vindo ao Integrator", font=("MS Shell Dlg 2", 16))
        self.titulo.grid(row = 0, column = 0, columnspan = 2, sticky = "nsw")
       
        self.descricao = tk.Label(text = "Aqui você pode acessar diversos serviços para que sua vida na sala seja muito mais prática e rápida.", font=("MS Shell Dlg 2", 12))
        self.descricao.grid(row = 1, column = 0, columnspan = 2, sticky = "nwe")
        
        self.pergunta = tk.Label(text = "O que você deseja acessar ?", font=("MS Shell Dlg 2", 12))
        self.pergunta.grid(row = 2, column = 0, columnspan = 2, sticky = "nw")
        
                
        #Botões
        self.Integrabotao = tk.Button(self.window)
        self.Integrabotao.config(text = "Integrantes da sala")
        self.Integrabotao.grid(row = 3, column = 0,columnspan = 1, sticky = "nwe")
        
        self.calenbotao = tk.Button(self.window)
        self.calenbotao.config(text = "Calendário de tarefas")
        self.calenbotao.grid(row = 4, column = 0,columnspan = 1, sticky = "nwe")
        
        self.aulasbotao = tk.Button(self.window)
        self.aulasbotao.config(text = "Aulas da semana")
        self.aulasbotao.grid(row = 5, column = 0,columnspan = 1, sticky = "nwe")
        
        self.servicosbotao = tk.Button(self.window)
        self.servicosbotao.config(text = "Serviços próximos ao Insper")
        self.servicosbotao.grid(row = 6, column = 0,columnspan = 1, sticky = "nwe")
        
        
    def iniciar (self):
        self.window.mainloop()        
app = MainWindow()
app.iniciar()