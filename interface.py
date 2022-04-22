import sys
import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb


root = tk.Tk()


class Front():
    def __init__(self):
        super().__init__()
        

        self.title('Youtube Downloader')
        self.geometry('512x480')
        self.configure(background = "light green")

    def LabelE(self):
        self.label1 = Label(root, text='Link'.grid(row = 0))
        self.e1 = Entry(tk)
        self.e1.grid(row=0, column=1)

    






root.mainloop()

#if __name__ == "__main__":
#    gui = Front()
#    gui.mainloop
