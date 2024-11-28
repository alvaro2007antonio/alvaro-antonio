from tkinter import *
from tkinter import messagebox

janela = Tk()
janela.title("Tela de Login")
janela.geometry("300x150+100+100")

# Usuário e senha válidos (dados fixos para demonstração)
usuario_valido = "admin"
senha_valida = "1234"

#Rótulo e campo do usuário
rotulo_usuario = Label(janela, text="Usuário:")
rotulo_usuario.grid(row=0, column=0, padx=10, pady=10)
campo_usuario = Entry(janela)
campo_usuario.grid(row=0, column=1)

#Rótulo e campo da senha
rotulo_senha = Label(janela, text="Senha:")
rotulo_senha.grid(row=1, column=0, padx=10, pady=10)
campo_senha = Entry(janela, show="*")  # O caractere "*" oculta a senha
campo_senha.grid(row=1, column=1)

#Função para verificar o login
def verificar_login():
    usuario = campo_usuario.get()
    senha = campo_senha.get()

    if usuario == usuario_valido and senha == senha_valida:
        messagebox.showinfo("Login", "Acesso permitido")
    else:
        messagebox.showerror("Login", "Acesso negado")

# Botão login
botao_entrar = Button(janela, text="Entrar", command=verificar_login, width=15)
botao_entrar.grid(row=2, column=1, pady=10)

#Inicialização da janela principal
janela.mainloop()
