import tkinter as tk
from src.widgets.widgets_to_tk_abc import Widget

class TabletConnectionStatus(Widget):
    def __init__(self,root : tk.Tk):
        self.root = root
        self.text = tk.StringVar() #Transform elemnto in Stringvar 
        self.label = tk.Label(root, textvariable=self.text)

    def show(self):
        self.label.pack(pady=10)

    def logic(self, status : bool = False):
        
        self.text.set("Tablet Connected" if status else "Tablet Unconnected")

    def unshow(self):
        self.label.pack_forget()

    

