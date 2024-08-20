class Aluno:
    def __init__(self):
        self.nome= ""
        self.curso = ""
        self.serie = ""


aluno1 = Aluno()
aluno1.nome = "Dudu"
aluno1.curso = "Informática"
aluno1.serie = "3o ano"


aluno2 = Aluno()
aluno2.nome = "Rabicó"
aluno2.curso = "Eletrônica"
aluno2.serie = "4o ano"


aluno3 = Aluno()
aluno3.nome = "Alisson"
aluno3.curso = "Comércio"
aluno3.serie = "3o ano"

print(f'{aluno1.nome}    {aluno2.nome}  {aluno3.nome}')
print(f'{aluno1.serie}  {aluno2.serie}  {aluno3.serie}')