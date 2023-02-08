import customtkinter as ctk
from tkinter import *

janela = ctk.CTk()

class Application():
    def __init__(self):
        self.janela= janela
        self.tema()
        self.tela()
        self.tela_login()
        janela.mainloop()

    
    def tema(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

    def tela(self):
        janela.geometry("700x400")
        janela.title("Sistema de Login")
        janela.iconbitmap("fogue2.ico")
        janela.resizable(False, False)

    def tela_login(self):
        # Trabalhando com a imagem da tela
        img = PhotoImage(file="geo2.png")
        label_img = ctk.CTkLabel(master=janela, image=img).place(x=10, y=75)

        title_label = ctk.CTkLabel(master=janela, text="Entre na sua conta e tenha\n a plataforma", 
        font=("Roboto", 20), text_color="#00B0F0").place(x=15, y=10)
        # Substitui text_font por font , pois , estava crashando !

        # frame
        login_frame = ctk.CTkFrame(master=janela, width=350, height=396)
        login_frame.pack(side=RIGHT)

        #widgets dentro da frame de tela de login
        label = ctk.CTkLabel(master=login_frame, text="Sistema de Login", font=("Roboto", 20)).place(x=25, y=5)

        username_entry = ctk.CTkEntry(master=login_frame, placeholder_text="Nome de Usuário", width=300, 
        font=("Roboto", 14)).place(x=25, y=105)
        username_label = ctk.CTkLabel(master=login_frame, text="* O campo nome de usuário é de caráter obrigatório.", 
        text_color="green", font=("Roboto", 8)).place(x=25, y=135)

        password_entry = ctk.CTkEntry(master=login_frame, placeholder_text="Senha de Usuário", width=300, 
        font=("Roboto", 14),show="*").place(x=25, y=175)
        password_label = ctk.CTkLabel(master=login_frame, text="*O campo Senha é de caráter obrigatório.", 
        text_color="green", font=("Roboto", 8)).place(x=25, y=205)

        #Caixa manter-me conectado
        checkbox = ctk.CTkCheckBox(master=login_frame, text="Manter-me conectado sempre.").place(x=25, y=235)

        login_button = ctk.CTkButton(master=login_frame, text="Login", width=300).place(x=25, y=285)


        register_span = ctk.CTkLabel(master=login_frame, text="Não possue uma conta?").place(x=25, y=325)


        def tela_register():
            # Remover o frame de login
            login_frame.pack_forget()

            # Criando a tela de cadastro de usuários
            rg_frame = ctk.CTkFrame(master=janela, width=350, height=396)
            rg_frame.pack(side=RIGHT)
            
            label = ctk.CTkLabel(master=rg_frame, text="Faça o seu cadastro", font=("Roboto", 20)).place(x=25, y=5)

            span = ctk.CTkLabel(master=rg_frame, text="*Todos os campos são de caráter obrigatório", font=("Roboto",10), text_color="gray").place(x=25, y=65)

            username_entry = ctk.CTkEntry(master=rg_frame, placeholder_text="Nome de Usuário", width=300, 
            font=("Roboto", 14)).place(x=25, y=105)

            email_entry = ctk.CTkEntry(master=rg_frame, placeholder_text="E-mail de Usuário", width=300, 
            font=("Roboto", 14)).place(x=25, y=145)

            password_entry = ctk.CTkEntry(master=rg_frame, placeholder_text="Senha de Usuário", width=300, 
            font=("Roboto", 14), show="*").place(x=25, y=185)

            confirm_password_entry = ctk.CTkEntry(master=rg_frame, placeholder_text="Confirmar senha", width=300, 
            font=("Roboto", 14), show="*").place(x=25, y=225)
            
            
            checkbox = ctk.CTkCheckBox(master=rg_frame, text="Aceito todos os Termos e Políticas.").place(x=25, y=265)

            
            back_button = ctk.CTkButton(master=rg_frame, text="VOLTAR", width=145, fg_color="green", hover_color="#202020").place(x=25, y=315)
            save_button = ctk.CTkButton(master=rg_frame, text="CADASTRAR", width=145, fg_color="green", hover_color="014B05").place(x=180, y=315)

            pass
        
        register_button = ctk.CTkButton(master=login_frame, text="Cadastre-se", width=150, 
        fg_color="green", hover_color="#2D9334", command=tela_register).place(x=175, y=325)



Application()
