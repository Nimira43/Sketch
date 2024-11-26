import customtkinter as ctk
from draw_surface import DrawSurface

class App(ctk.CTk):
  def __init__(self):
    super().__init__()
    self.geometry('800x600')
    self.title('')
    self.iconbitmap('./images/empty.ico')
    ctk.set_appearance_mode('light')
    
    self.colour_string = ctk.StringVar(value = '000')
    self.brush_float = ctk.DoubleVar(value = 1)

    DrawSurface(self, self.colour_string, self.brush_float)

    self.mainloop()

if __name__ == '__main__':
  App()