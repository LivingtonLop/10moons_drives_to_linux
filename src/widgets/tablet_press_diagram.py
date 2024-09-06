import tkinter as tk
from src.widgets.widgets_to_tk_abc import Widget

class TabletPressDiagram(Widget):
    def __init__(self,root : tk.Tk, width : int = 500,height : int = 300):
        self.root = root
        self.coord = tk.IntVar() #Transform elemnto in IntVar 
        self.canva = tk.Canvas(self.root,width = width,height = height, bd=5,relief="ridge")

    @staticmethod
    def create_cuadricule(canvas : tk.Canvas,size_cell : int,width : int = 500,height : int = 300):
        for x in range(0, width,size_cell):
            canvas.create_line(x, 0, x, height, fill="lightgray")

        for y in range(0, height,size_cell):
            canvas.create_line(0, y, width, y, fill="lightgray")
        
        #canvas.create_rectangle(1,1, width-1, height-1, outline="lightgray", width=2)

    def show(self):
        self.canva.pack(side='left', expand=False)

    def logic(self, coor_line : int = 0):
        pass

    def unshow(self):
        self.canva.pack_forget()

    

