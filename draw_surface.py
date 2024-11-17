from tkinter import Canvas
from setting import *

class DrawSurface(Canvas):
  def __init__(self, parent):
    super().__init__(master = parent)
    self.pack(expand = True, fill = 'both')