import tkinter as tk
from src.widgets.widgets_to_tk_abc import Widget

class TabletPanelDraw(Widget):
    def __init__(self,root : tk.Tk, width : int = 400,height : int = 400):
        self.root = root
        
        self.canva = tk.Canvas(self.root,width = width,height = height, bd=5,relief="ridge")
        self.coor_x_device,self.coor_y_device =  None, None

        # Vincular eventos del mouse a las funciones
        self.canva.bind("<Button-1>", self.press)
        self.canva.bind("<B1-Motion>", self.logic)

    def press(self, event):
        self.coor_x_device,self.coor_y_device =  event.x, event.y

    def show(self):
        self.canva.pack(pady=10)

    def logic(self,event): #evento del device
        if self.coor_x_device and self.coor_y_device:
            self.canva.create_line(
                (
                    self.coor_x_device,
                    self.coor_y_device,
                    event.x,
                    event.y
                ),
                fill="Blue",
                width=2
            )
        self.coor_x_device, self.coor_y_device = event.x, event.y

    def unshow(self):
        self.canva.pack_forget()

    

