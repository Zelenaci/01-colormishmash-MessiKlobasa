#!/usr/bin/env python3

from os.path import basename, splitext
import tkinter as tk
from tkinter import Canvas, Scale, HORIZONTAL 

# from tkinter import ttk



class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "ColorMishMash"

    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
       
        self.bind("<Escape>", self.quit) #klávesa ESC spustí funkci Quit
       
        self.lblR = tk.Label(self, text="R") #Nadpis, který se zobrazuje
        self.lblR.pack() #umístění nadpisu (3 typy umístění: pack, grid a place)
        self.scaleR = Scale(self, from_=0, to=255, orient=HORIZONTAL, length=256, command=self.change)
        self.scaleR.pack()

        self.lblG = tk.Label(self, text="G") #Nadpis, který se zobrazuje
        self.lblG.pack() #umístění nadpisu (3 typy umístění: pack, grid a place)
        self.scaleG = Scale(self, from_=0, to=255, orient=HORIZONTAL, length=256)
        self.scaleG.pack()

        self.lblB = tk.Label(self, text="B") #Nadpis, který se zobrazuje
        self.lblB.pack() #umístění nadpisu (3 typy umístění: pack, grid a place)
        self.scaleB = Scale(self, from_=0, to=255, orient=HORIZONTAL, length=256)
        self.scaleB.pack()

        self.canvasMain = Canvas(self, width=200, height=100, background='#000000' )
        self.canvasMain.pack()

       
        self.btnQuit = tk.Button(self, text="Quit", command=self.quit)
        self.btnQuit.pack()
       
        self.btn2 = tk.Button(self, text="Change", command=self.change)
        self.btn2.pack()

    def change(self, event):
        r = self.scaleR.get()
        g = self.scaleR.get()
        b = self.scaleR.get()
        self.canvasMain.confing(background=f"#{r:02x}{g:02x}{b:02x}")
    
    def quit(self, event=None):
        super().quit()


app = Application()
app.mainloop()
