from tkinter import *
from tkinter import messagebox

janela = Tk()
janela.title("Calculadora")
janela.geometry("260x150+100+100")

#ROTULOS E CAMPOS DOS VALORES 1 E 2
rotulo1 = Label(janela, text="Valor 1")
rotulo1.grid(row=0, column=0)
campo1 = Entry(janela)
campo1.grid(row=0, column=1)

rotulo2 = Label(janela, text="Valor 2")
rotulo2.grid(row=1, column=0)
campo2 = Entry(janela)
campo2.grid(row=1, column=1)


#ROTULOS E CAMPOS EXIBIÇÃO DE RESULTADOS
rotulo3 = Label(janela, text="Resultado =")
rotulo3.grid(row=3, column=0)
campo3 = Entry(janela, state="disabled")  #Campo desabilitado
campo3.grid(row=3, column=1)

# Funções para as operações
def calcular(operacao):
    try:
        v1 = float(campo1.get())
        v2 = float(campo2.get())
        
        # Escolhe a operação com base no botão clicado
        if operacao == "+":
            resultado = v1 + v2
        elif operacao == "-":
            resultado = v1 - v2
        elif operacao == "*":
            resultado = v1 * v2
        elif operacao == "/":
            if v2 == 0:  # Tratamento de divisão por zero
                raise ZeroDivisionError
            resultado = v1 / v2

        # Exibe o resultado no campo desabilitado
        campo3["state"] = "normal"
        campo3.delete(0, END)
        campo3.insert(0, str(round(resultado, 2)))
        campo3["state"] = "disabled"
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")
    except ZeroDivisionError:
        messagebox.showerror("Erro", "Divisão por zero não é permitida.")

# Botões para as operações
botao_somar = Button(janela, text="Somar", command=lambda: calcular("+"), width=10)
botao_somar.grid(row=2, column=0)

botao_subtrair = Button(janela, text="Subtrair", command=lambda: calcular("-"), width=10)
botao_subtrair.grid(row=2, column=1)

botao_multiplicar = Button(janela, text="Multiplicar", command=lambda: calcular("*"), width=10)
botao_multiplicar.grid(row=2, column=2)

botao_dividir = Button(janela, text="Dividir", command=lambda: calcular("/"), width=10)
botao_dividir.grid(row=2, column=3)

# Inicialização da janela
janela.mainloop()
