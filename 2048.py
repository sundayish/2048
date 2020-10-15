import tkinter as tk

class Game(tk.Frame):
    tk.Frame.__init__(self)
    self.grid()
    self.master.title("2048")