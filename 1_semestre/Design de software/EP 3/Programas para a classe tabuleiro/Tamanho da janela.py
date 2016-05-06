import tkinter as tk


window = tk.Tk()
window.geometry("300x300")
window.rowconfigure(0, minsize=100, weight=1)
window.rowconfigure(3, weight=1)
window.columnconfigure(0, minsize=100, weight=1)
window.columnconfigure(, weight=1)
window.mainloop()