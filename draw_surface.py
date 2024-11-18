from tkinter import Canvas
from setting import *

class DrawSurface(Canvas):
  def __init__(self, parent, colour_string, brush_float):
    super().__init__(master = parent,background = CANVAS_BG, bd = 0, highlightthickness = 0, relief='ridge')
    self.pack(expand = True, fill = 'both')

    self.colour_string = colour_string
    self.brush_float = brush_float

    self.bind('<Motion>', self.draw)
    self.bind('<Button>', self.activate_draw)
    self.bind('<ButtonRelease>', self.deactivate_draw)

  def draw(self, event):
    pass
  def activate_draw(self, event):
    pass
  def deactivate_draw(self, event):
    pass