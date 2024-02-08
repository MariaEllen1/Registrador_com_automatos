import tkinter as tk
from tkinter import PhotoImage, StringVar
import tkinter.messagebox as messagebox
import customtkinter
from random import choice

def automato_telefone(numero):
    print(f"================= Verificando número de telefone: {numero} =================")
    estado_atual = 'Primeiro Digito'

    for caractere in numero:
        print(f"Analisando o caractere: {caractere}, estado atual: {estado_atual}")
        if estado_atual == 'Primeiro Digito':
            if caractere.isdigit():
                estado_atual = 'Segundo Digito'
            else:
                return False
        elif estado_atual == 'Segundo Digito':
            if caractere.isdigit():
                estado_atual = 'Terceiro Digito'
            else:
                return False
        elif estado_atual == 'Terceiro Digito':
            if caractere.isdigit():
                estado_atual = 'Quarto Digito'
            else:
                return False
        elif estado_atual == 'Quarto Digito':
            if caractere.isdigit():
                estado_atual = 'Quinto Digito'
            else:
                return False
        elif estado_atual == 'Quinto Digito':
            if caractere.isdigit():
                estado_atual = 'Sexto Digito'
            else:
                return False
        elif estado_atual == 'Sexto Digito':
            if caractere.isdigit():
                estado_atual = 'Setimo Digito'
            else:
                return False
        elif estado_atual == 'Setimo Digito':
            if caractere.isdigit():
                estado_atual = 'Oitavo Digito'
            else:
                return False
        elif estado_atual == 'Oitavo Digito':
            if caractere.isdigit():
                estado_atual = 'Nono Digito'
            else:
                return False
        elif estado_atual == 'Nono Digito':
            if caractere.isdigit():
                estado_atual = 'Decimo Digito'
            else:
                return False
        elif estado_atual == 'Decimo Digito':
            if caractere.isdigit():
                estado_atual = 'Decimo_Primeiro Digito'
            else:
                return False
        elif estado_atual == 'Decimo_Primeiro Digito':
            if caractere.isdigit():
                estado_atual = 'Estado de Aceitação'
            else:
                return False

    if len(numero) != 11:
        return False

    if estado_atual == 'Estado de Aceitação':
        print(f"{estado_atual}")
        return True
    else:
        return False

def exibir_erro(mensagem):
    messagebox.showerror("Erro", mensagem)

def encerrar_programa():
    janela.destroy()

def janela_cadastro_concluido():
    nome = nome_var.get().strip()
    senha = senha_var.get().strip()
    numero = numero_var.get().strip()

    if not nome or not senha or not numero:
        exibir_erro("Preencha todos os campos (nome, senha e telefone) para concluir o cadastro.")
    elif not automato_nome(nome):
        exibir_erro("Nome inválido.")
    elif not automato_senha(senha):
        exibir_erro("A senha não atende aos critérios.")
    elif not automato_telefone(numero):
        exibir_erro("Telefone inválido.")
    else:
        janela_concluido = tk.Toplevel()
        janela_concluido.geometry("400x100")
        janela_concluido.title("Cadastro Concluído")

        label_concluido = tk.Label(janela_concluido, text="Cadastro concluído com sucesso!", font=("Roboto", 16))
        label_concluido.pack(pady=20)

        janela.after(3000, encerrar_programa)

def automato_gerador_senha():
    estado_atual = 'Primeiro Caractere'
    senha = ''
    maiusculo = 0
    numero = 0

    while estado_atual != 'Estado de Aceitacao':
        if estado_atual == 'Primeiro Caractere':
            caractere = choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789")
            senha += caractere
            print(f"Analisando o caractere: {caractere}, estado atual: {estado_atual}")
            if caractere.isupper():
                estado_atual = 'Segundo Caractere'
                maiusculo += 1
            elif caractere.isnumeric():
                estado_atual = 'Segundo Caractere'
                numero += 1
            elif caractere.islower():
                estado_atual = 'Segundo Caractere'
            else:
                return False
        elif estado_atual == 'Segundo Caractere':
            caractere = choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789")
            senha += caractere
            print(f"Analisando o caractere: {caractere}, estado atual: {estado_atual}")
            if caractere.isupper():
                estado_atual = 'Terceiro Caractere'
                maiusculo += 1
            elif caractere.isnumeric():
                estado_atual = 'Terceiro Caractere'
                numero += 1
            elif caractere.islower():
                estado_atual = 'Terceiro Caractere'
            else:
                return False
        elif estado_atual == 'Terceiro Caractere':
            caractere = choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789")
            senha += caractere
            print(f"Analisando o caractere: {caractere}, estado atual: {estado_atual}")
            if caractere.isupper():
                estado_atual = 'Quarto Caractere'
                maiusculo += 1
            elif caractere.isnumeric():
                estado_atual = 'Quarto Caractere'
                numero += 1
            elif caractere.islower():
                estado_atual = 'Quarto Caractere'
            else:
                return False
        elif estado_atual == 'Quarto Caractere':
            caractere = choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789")
            senha += caractere
            print(f"Analisando o caractere: {caractere}, estado atual: {estado_atual}")
            if caractere.isupper():
                estado_atual = 'Quinto Caractere'
                maiusculo += 1
            elif caractere.isnumeric():
                estado_atual = 'Quinto Caractere'
                numero += 1
            elif caractere.islower():
                estado_atual = 'Quinto Caractere'
            else:
                return False
        elif estado_atual == 'Quinto Caractere':
            caractere = choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789")
            senha += caractere
            print(f"Analisando o caractere: {caractere}, estado atual: {estado_atual}")
            if caractere.isupper():
                estado_atual = 'Sexto Caractere'
                maiusculo += 1
            elif caractere.isnumeric():
                estado_atual = 'Sexto Caractere'
                numero += 1
            elif caractere.islower():
                estado_atual = 'Sexto Caractere'
            else:
                return False
        elif estado_atual == 'Sexto Caractere':
            caractere = choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789")
            senha += caractere
            print(f"Analisando o caractere: {caractere}, estado atual: {estado_atual}")
            if caractere.isupper():
                estado_atual = 'Setimo Caractere'
                maiusculo += 1
            elif caractere.isnumeric():
                estado_atual = 'Setimo Caractere'
                numero += 1
            elif caractere.islower():
                estado_atual = 'Setimo Caractere'
            else:
                return False
        elif estado_atual == 'Setimo Caractere':
            caractere = choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789")
            senha += caractere
            print(f"Analisando o caractere: {caractere}, estado atual: {estado_atual}")
            if caractere.isupper():
                estado_atual = 'Oitavo Caractere'
                maiusculo += 1
            elif caractere.isnumeric():
                estado_atual = 'Oitavo Caractere'
                numero += 1
            elif caractere.islower():
                estado_atual = 'Oitavo Caractere'
            else:
                return False
        elif estado_atual == 'Oitavo Caractere':
            caractere = choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789")
            senha += caractere
            print(f"Analisando o caractere: {caractere}, estado atual: {estado_atual}")
            if caractere.isupper():
                estado_atual = 'Estado de Aceitação'
                maiusculo += 1
            elif caractere.isnumeric():
                estado_atual = 'Estado de Aceitação'
                numero += 1
            elif caractere.islower():
                estado_atual = 'Estado de Aceitação'
            else:
                return False

        if estado_atual == 'Estado de Aceitação':
            if maiusculo >= 1:
                if numero >= 1:
                    senha_var.set(senha)
                    print("Estado de Aceitação")
                    return True
                else:
                    senha = ''
                    estado_atual = 'Primeiro Caractere'
            else:
                senha = ''
                estado_atual = 'Primeiro Caractere'

def automato_nome(nome):
    print(f"================= Verificando nome: {nome} =================")
    estado_atual_nome = 'Primeiro Caractere'

    for caractere in nome:
        print(f"Analisando o caractere: {caractere}, estado atual: {estado_atual_nome}")

        if estado_atual_nome == 'Primeiro Caractere':
            if caractere.isupper():
                estado_atual_nome = 'Segundo Caractere'
            elif caractere.islower:
                estado_atual_nome = 'Segundo Caractere'
        elif estado_atual_nome == 'Segundo Caractere':
            if caractere.isupper():
                estado_atual_nome = 'Terceiro Caractere'
            elif caractere.islower:
                estado_atual_nome = 'Terceiro Caractere'
        elif estado_atual_nome == 'Terceiro Caractere':
            if caractere.isupper():
                estado_atual_nome = 'Quarto Caractere'
            elif caractere.islower:
                estado_atual_nome = 'Quarto Caractere'
        elif estado_atual_nome == 'Quarto Caractere':
            if caractere.isupper():
                estado_atual_nome = 'Quinto Caractere'
            elif caractere.islower:
                estado_atual_nome = 'Quinto Caractere'
        elif estado_atual_nome == 'Quinto Caractere':
            if caractere.isupper():
                estado_atual_nome = 'Sexto Caractere'
            elif caractere.islower:
                estado_atual_nome = 'Sexto Caractere'
        elif estado_atual_nome == 'Sexto Caractere':
            if caractere.isupper():
                estado_atual_nome = 'Setimo Caractere'
            elif caractere.islower:
                estado_atual_nome = 'Setimo Caractere'
        elif estado_atual_nome == 'Setimo Caractere':
            if caractere.isupper():
                estado_atual_nome = 'Oitavo Caractere'
            elif caractere.islower:
                estado_atual_nome = 'Oitavo Caractere'
        elif estado_atual_nome == 'Oitavo Caractere':
            if caractere.isupper():
                estado_atual_nome = 'Nono Caractere'
            elif caractere.islower:
                estado_atual_nome = 'Nono Caractere'
        elif estado_atual_nome == 'Nono Caractere':
            if caractere.isupper():
                estado_atual_nome = 'Decimo Caractere'
            elif caractere.islower:
                estado_atual_nome = 'Decimo Caractere'
        elif estado_atual_nome == 'Decimo Caractere':
            if caractere.isupper():
                estado_atual_nome = 'Decimo_Primeiro Caractere'
            elif caractere.islower:
                estado_atual_nome = 'Decimo_Primeiro Caractere'
        elif estado_atual_nome == 'Decimo_Primeiro Caractere':
            if caractere.isupper():
                estado_atual_nome = 'Decimo_Segundo Caractere'
            elif caractere.islower:
                estado_atual_nome = 'Decimo_Segundo Caractere'
        elif estado_atual_nome == 'Decimo_Segundo Caractere':
            if caractere.isupper():
                estado_atual_nome = 'Decimo_Terceiro Caractere'
            elif caractere.islower:
                estado_atual_nome = 'Decimo_Terceiro Caractere'
        elif estado_atual_nome == 'Decimo_Terceiro Caractere':
            if caractere.isupper():
                estado_atual_nome = 'Decimo_Quarto Caractere'
            elif caractere.islower:
                estado_atual_nome = 'Decimo_Quarto Caractere'
        elif estado_atual_nome == 'Decimo_Quarto Caractere':
            if caractere.isupper():
                estado_atual_nome = 'Decimo_Quinto Caractere'
            elif caractere.islower:
                estado_atual_nome = 'Decimo_Quinto Caractere'
        elif estado_atual_nome == 'Decimo_Quinto Caractere':
            if caractere.isupper():
                estado_atual_nome = 'Decimo_Sexto Caractere'
            elif caractere.islower:
                estado_atual_nome = 'Decimo_Sexto Caractere'
        elif estado_atual_nome == 'Decimo_Sexto Caractere':
            if caractere.isupper():
                estado_atual_nome = 'Decimo_Setimo Caractere'
            elif caractere.islower:
                estado_atual_nome = 'Decimo_Setimo Caractere'
        elif estado_atual_nome == 'Decimo_Setimo Caractere':
            if caractere.isupper():
                estado_atual_nome = 'Decimo_Oitavo Caractere'
            elif caractere.islower:
                estado_atual_nome = 'Decimo_Oitavo Caractere'
        elif estado_atual_nome == 'Decimo_Oitavo Caractere':
            if caractere.isupper():
                estado_atual_nome = 'Decimo_Nono Caractere'
            elif caractere.islower:
                estado_atual_nome = 'Decimo_Nono Caractere'
        elif estado_atual_nome == 'Decimo_Nono Caractere':
            if caractere.isupper():
                estado_atual_nome = 'Vigessimo Caractere'
            elif caractere.islower:
                estado_atual_nome = 'Vigessimo Caractere'

    if len(nome) < 3 or len(nome) > 21:
        return False

    if estado_atual_nome == 'Quarto Caractere':
        print(f'Estado de Aceitação')
        return True
    elif estado_atual_nome == 'Quinto Caractere':
        print(f'Estado de Aceitação')
        return True
    elif estado_atual_nome == 'Sexto Caractere':
        print(f'Estado de Aceitação')
        return True
    elif estado_atual_nome == 'Setimo Caractere':
        print(f'Estado de Aceitação')
        return True
    elif estado_atual_nome == 'Oitavo Caractere':
        print(f'Estado de Aceitação')
        return True
    elif estado_atual_nome == 'Nono Caractere':
        print(f'Estado de Aceitação')
        return True
    elif estado_atual_nome == 'Decimo Caractere':
        print(f'Estado de Aceitação')
        return True
    elif estado_atual_nome == 'Decimo_Primeiro Caractere':
        print(f'Estado de Aceitação')
        return True
    elif estado_atual_nome == 'Decimo_Segundo Caractere':
        print(f'Estado de Aceitação')
        return True
    elif estado_atual_nome == 'Decimo_Terceiro Caractere':
        print(f'Estado de Aceitação')
        return True
    elif estado_atual_nome == 'Decimo_Quarto Caractere':
        print(f'Estado de Aceitação')
        return True
    elif estado_atual_nome == 'Decimo_Quinto Caractere':
        print(f'Estado de Aceitação')
        return True
    elif estado_atual_nome == 'Decimo_Sexto Caractere':
        print(f'Estado de Aceitação')
        return True
    elif estado_atual_nome == 'Decimo_Setimo Caractere':
        print(f'Estado de Aceitação')
        return True
    elif estado_atual_nome == 'Decimo_Oitavo Caractere':
        print(f'Estado de Aceitação')
        return True
    elif estado_atual_nome == 'Decimo_Nono Caractere':
        print(f'Estado de Aceitação')
        return True
    elif estado_atual_nome == 'Vigessimo Caractere':
        print(f'Estado de Aceitação')
        return True
    else:
        return False

def automato_senha(senha):
    print(f"================= Verificando senha: {senha} =================")
    estado_atual = 'Primeiro Caractere'
    maiusculo = 0
    numero = 0

    for caractere in senha:
        print(f"Analisando o caractere: {caractere}, estado atual: {estado_atual}")

        if estado_atual == 'Primeiro Caractere':
            if caractere.isupper():
                estado_atual = 'Segundo Caractere'
                maiusculo += 1
            elif caractere.isnumeric():
                estado_atual = 'Segundo Caractere'
                numero += 1
            elif caractere.islower():
                estado_atual = 'Segundo Caractere'
        elif estado_atual == 'Segundo Caractere':
            if caractere.isupper():
                estado_atual = 'Terceiro Caractere'
                maiusculo += 1
            elif caractere.isnumeric():
                estado_atual = 'Terceiro Caractere'
                numero += 1
            elif caractere.islower():
                estado_atual = 'Terceiro Caractere'
        elif estado_atual == 'Terceiro Caractere':
            if caractere.isupper():
                estado_atual = 'Quarto Caractere'
                maiusculo += 1
            elif caractere.isnumeric():
                estado_atual = 'Quarto Caractere'
                numero += 1
            elif caractere.islower():
                estado_atual = 'Quarto Caractere'
        elif estado_atual == 'Quarto Caractere':
            if caractere.isupper():
                estado_atual = 'Quinto Caractere'
                maiusculo += 1
            elif caractere.isnumeric():
                estado_atual = 'Quinto Caractere'
                numero += 1
            elif caractere.islower():
                estado_atual = 'Quinto Caractere'
        elif estado_atual == 'Quinto Caractere':
            if caractere.isupper():
                estado_atual = 'Sexto Caractere'
                maiusculo += 1
            elif caractere.isnumeric():
                estado_atual = 'Sexto Caractere'
                numero += 1
            elif caractere.islower():
                estado_atual = 'Sexto Caractere'
        elif estado_atual == 'Sexto Caractere':
            if caractere.isupper():
                estado_atual = 'Sétimo Caractere'
                maiusculo += 1
            elif caractere.isnumeric():
                estado_atual = 'Sétimo Caractere'
                numero += 1
            elif caractere.islower():
                estado_atual = 'Sétimo Caractere'
        elif estado_atual == 'Sétimo Caractere':
            if caractere.isupper():
                estado_atual = 'Oitavo Caractere'
                maiusculo += 1
            elif caractere.isnumeric():
                estado_atual = 'Oitavo Caractere'
                numero += 1
            elif caractere.islower():
                estado_atual = 'Oitavo Caractere'

    if estado_atual == 'Oitavo Caractere':
        if maiusculo >= 1:
            if numero >= 1:
                print("Estado de Aceitação")
                return True
            else:
                return False
        else:
            return False
    else:
        return False

janela = customtkinter.CTk()
janela.geometry("600x500")
janela.title("Registro")
janela.resizable(False, False)

img = PhotoImage(file="login100x100.png")
label_img = customtkinter.CTkLabel(master=janela, image=img, text="")
label_img.place(x=20, y=120)

frame = customtkinter.CTkFrame(master=janela, width=350, height=396)
frame.place(x=150, y=30)

label = customtkinter.CTkLabel(master=frame, text="Registro", font=('Roboto', 20, 'bold'), text_color=('white'))
label.place(x=25, y=5)

nome_var = StringVar()
nome_entry = customtkinter.CTkEntry(master=frame, textvariable=nome_var, placeholder_text="Nome de usuário",
                                    width=300, font=('Roboto', 20, 'bold'), text_color=('white'))
nome_entry.place(x=25, y=105)

label1 = customtkinter.CTkLabel(master=frame, text="*O campo nome é de caráter obrigatório.", text_color="green",
                                font=("Roboto", 8))
label1.place(x=25, y=135)

senha_var = StringVar()
senha_entry = customtkinter.CTkEntry(master=frame, textvariable=senha_var, placeholder_text="Senha", width=300,
                                     font=('Roboto', 20, 'bold'), text_color=('white'))
senha_entry.place(x=25, y=175)

label2 = customtkinter.CTkLabel(master=frame, text="*O campo senha é de caráter obrigatório.", text_color="green",
                                font=("Roboto", 8))
label2.place(x=25, y=205)

numero_var = StringVar()
telefone_entry = customtkinter.CTkEntry(master=frame, textvariable=numero_var, placeholder_text="Telefone", width=300,
                                        font=('Roboto', 20, 'bold'), text_color=('white'))
telefone_entry.place(x=25, y=235)

label3 = customtkinter.CTkLabel(master=frame, text="*O campo Telefone é de caráter obrigatório.", text_color="green",
                                font=("Roboto", 8))
label3.place(x=25, y=265)

button1 = customtkinter.CTkButton(master=frame, text="Gerar senha", width=300, command=automato_gerador_senha)
button1.place(x=25, y=295)

button2 = customtkinter.CTkButton(master=frame, text="Registrar-se", width=300, command=janela_cadastro_concluido)
button2.place(x=25, y=355)

janela.mainloop()
