# -*- coding: utf-8 -*-

import tkinter as tk

class Application:
    
    def __init__(self):
        self.lastx = 0
        self.lasty = 0
        
        self.window = tk.Tk()
        self.window.columnconfigure(0, weight=1)
        self.window.rowconfigure(0, weight=1)
        
        self.canvas = tk.Canvas(self.window)
        self.canvas.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.canvas.bind("<Button-1>", self.xy)
        self.canvas.bind("<B1-Motion>", self.addLine)
        
    def xy(self, event):
        self.lastx = event.x
        self.lasty = event.y

    def addLine(self, event):
        self.canvas.create_line((self.lastx, self.lasty, event.x, event.y))
        self.lastx = event.x
        self.lasty = event.y
        
    def start(self):
        self.window.mainloop()

app = Application()
app.start()
