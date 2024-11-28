from tkinter import *
from tkinter import messagebox

janela = Tk()
janela.title("Somador")
janela.geometry("220x100+100+100")

#Rótulo e campo Valor 1
rotulo1 = Label(janela, text="Valor 1")
rotulo1.grid(row=0, column=0)
campo1 = Entry(janela)
campo1.grid(row=0, column=1)

#Rótulo e campo Valor 2
rotulo2 = Label(janela, text="Valor 2")
rotulo2.grid(row=1, column=0)
campo2 = Entry(janela)
campo2.grid(row=1, column=1)

#Rótulo e campo (TOTAL)
rotulo3 = Label(janela, text="Soma =")
rotulo3.grid(row=3, column=0)
campo3 = Entry(janela, state="disabled") #Campo desabilitado
campo3.grid(row=3, column=1)

# Função para somar os valores
def somar():
    try:
        v1 = int(campo1.get())
        v2 = int(campo2.get())
        resultado = v1 + v2
        campo3["state"] = "normal"  #Habilitar o campo para inserir o resultado
        campo3.delete(0, END)       #Limpar o campo antes de inserir o resultado
        campo3.insert(0, str(resultado))
        campo3["state"] = "disabled"  #Desabilitar novamente o campo
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")

#Botão soma
botao = Button(janela, text="Somar", command=somar, width=15)
botao.grid(row=2, column=1)

janela.mainloop()
