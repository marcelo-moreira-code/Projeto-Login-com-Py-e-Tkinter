import customtkinter
from tkinter import *

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

janela = customtkinter.CTk()
janela.geometry("700x400")
janela.title("Sistema de Login")
janela.iconbitmap("fogue2.ico")
janela.resizable(False, False)

# Trabalhando com a imagem da tela
img = PhotoImage(file="fog3.png")
label_img = customtkinter.CTkLabel(master=janela, image=img)
label_img.place(x=5, y=65)

# frame
frame = customtkinter.CTkFrame(master=janela, width=350, height=396)
frame.pack(side=RIGHT)

# frame widgets
label = customtkinter.CTkLabel(master=frame, text="Sistema de Login", text_font=("Roboto", 20))
label.place(x=25, y=5)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Nome de Usuário", width=300, 
text_font=("Roboto", 14)).place(x=25, y=105)
label1 = customtkinter.CTkLabel(master=frame, text="* O campo nome de usuário é de caracter obrigatório.", 
text_color="green", text_font=("Roboto", 8)).place(x=25, y=135)


janela.mainloop()
