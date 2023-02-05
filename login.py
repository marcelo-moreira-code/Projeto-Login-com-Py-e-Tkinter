import customtkinter
from tkinter import *

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

janela = customtkinter.CTk()
janela.geometry('700x400')
janela.title('Sistema de Login')
janela.iconbitmap("fogue2.ico")
janela.resizable(False, False)

#Trabalhando com a imagem da tela
img = PhotoImage(file='fog3.png')
label_img = customtkinter.CTkLabel(master=janela, image=img)
label_img.place(x=5, y=65)

#frame
frame = customtkinter.CTkFrame(master=janela, width=350, height=396)
frame.pack(side=RIGHT)


janela.mainloop()
