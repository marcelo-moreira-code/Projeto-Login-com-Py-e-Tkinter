import customtkinter
from tkinter import *

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

janela = customtkinter.CTk()
janela.geometry('700x400')
janela.title('Sistema de Login')
janela.iconbitmap("ico.ico")
janela.resizable(False, False)


img = PhotoImage(file='geometric.png')
label_img = customtkinter.CTkLabel(master=janela)


janela.mainloop()
