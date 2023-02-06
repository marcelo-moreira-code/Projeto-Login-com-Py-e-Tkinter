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
img = PhotoImage(file="geo2.png")
label_img = customtkinter.CTkLabel(master=janela, image=img)
label_img.place(x=5, y=65)

label_title = customtkinter.CTkLabel(master=janela, text="Entre na sua conta e tenha\n a plataforma", 
font=("Roboto", 18), text_color="#00B0F0").place(x=10, y=10)
# Substitui text_font por font , pois , estava crashando !


# frame
frame = customtkinter.CTkFrame(master=janela, width=350, height=396)
frame.pack(side=RIGHT)

# frame widgets
label = customtkinter.CTkLabel(master=frame, text="Sistema de Login", font=("Roboto", 20))
label.place(x=25, y=5)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Nome de Usuário", width=300, 
font=("Roboto", 14)).place(x=25, y=105)
label1 = customtkinter.CTkLabel(master=frame, text="* O campo nome de usuário é de caráter obrigatório.", 
text_color="green", font=("Roboto", 8)).place(x=25, y=135)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Senha de Usuário", width=300, 
font=("Roboto", 14),show="*").place(x=25, y=175)
label2 = customtkinter.CTkLabel(master=frame, text="*O campo Senha é de caráter obrigatório.", 
text_color="green", font=("Roboto", 8)).place(x=25, y=205)

#Caixa manter-me conectado
checkbox = customtkinter.CTkCheckBox(master=frame, text="Manter-me conectado sempre.").place(x=25, y=235)

button = customtkinter.CTkButton(master=frame, text="Login", width=300).place(x=25, y=285)


janela.mainloop()
