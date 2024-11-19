from tkinter import *
from turtle import width #Importa a Biblioteca tkinter
janela = Tk() #Cria o objeto janela e recebe o frame Tk com todos os componentes

#ROTULO
info = "Esse texto será\nexibido no rótulo\nem várias linhas"
rotulo = Label(janela, text = info)
rotulo.grid(row=0, column=2)
rotulo["font"] = ("Bokor", "18", "bold")
rotulo["fg"] = "white"
rotulo["bg"] = "purple"
rotulo["width"] = 20
rotulo["height"] = 10


#ROTULO2
info2 = """Assim tanbém
é possível
ter várias linhas."""

rotulo2 = Label(janela, text = info2)
rotulo2.grid(row=0, column=3)
rotulo2["width"] = 20
rotulo2["height"] = 10
rotulo2["fg"] = "orange"
rotulo2["bg"] = "navyblue"
rotulo2["font"] = ("Bokor", "18", "bold")


#BOTAO_SAIR
botao_sair = Button(janela) #Criado o botão
botao_sair.grid(row=3, column=3) #row (linha) e column (coluna) servem como alinhamento
botao_sair["text"] = "Sair" #Propriedade texto
botao_sair["width"] = 10 #Largura

botao_sair["command"] = quit #Comando para sair
botao_sair["font"] = ("Bokor", "18", "bold")
botao_sair["fg"] = "yellow"
botao_sair["bg"] = "red"

janela.mainloop() #Executa a janela

#Propriedades: width (largura), height (tamanho), text (texto)
#font (Família da fonte do texto), fg (Cor do texto), bg (Cor de fundo), side(Lado do widget --> left, right, Top, Bottom)
#PhotoImage (Imagem)