import customtkinter as ctk

class App(ctk.CTk):
  def __init__(self):
    super().__init__()
    self.geometry('800x600')
    self.title('')
    self.iconbitmap('./images/empty.ico')
    ctk.set_appearance_mode('dark')
    
    self.mainloop()

if __name__ == '__main__':
  App()