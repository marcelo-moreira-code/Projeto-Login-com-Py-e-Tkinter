import customtkinter
from tkinter import *

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

janela = customtkinter.CTk()
janela.geometry('700x400')
janela.title('Sistema de Login')
janela.iconbitmap("ico.ico")
janela.resizable(False, False)


img = PhotoImage(file='fog.png')
label_img = customtkinter.CTkLabel(master=janela, image=img)
label_img.place(x=5, y=65)


janela.mainloop()
