from tkinter import Canvas
from setting import *

class DrawSurface(Canvas):
  def __init__(self, parent, colour_string, brush_float):
    super().__init__(master = parent,background = CANVAS_BG, bd = 0, highlightthickness = 0, relief='ridge')
    self.pack(expand = True, fill = 'both')

    self.colour_string = colour_string
    self.brush_float = brush_float
    self.allow_draw = False

    self.old_x = None
    self.old_y = None

    self.bind('<Motion>', self.draw)
    self.bind('<Button>', self.activate_draw)
    self.bind('<ButtonRelease>', self.deactivate_draw)

  def draw(self, event):
    if self.allow_draw:
      if self.old_x and self.old_y:
        self.create_brush_line((self.old_x, self.old_y), (event.x, event.y))
      self.old_x = event.x
      self.old_y = event.y

  def create_brush_line(self, start, end):
    brush_size = self.brush_float.get() * 10
    self.create_line(start, end, fill = 'black', width = brush_size)

  def activate_draw(self, event):
    self.allow_draw = True

  def deactivate_draw(self, event):
    self.allow_draw = False
    self.old_x = None
    self.old_y = None