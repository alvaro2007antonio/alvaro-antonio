from autor import Autor
from livro import Livro
def menu():
    print("\nMenu da Biblioteca")
    print("1. Adicionar Livro")
    print("2. Remover Livro")
    print("3. Buscar Livro")
    print("4. Listar Livro")
    print("5. Sair")

def main():
    biblioteca = biblioteca()

    while True:
        menu()
        opçao = int(input("Escolha uma opção: "))

        if opçao == 1:
            titulo = input("Digite o título do livro: ")
            nome_autor = input("Digite o nome do autor: ")
            nacionalidade = input("Digite a nacionalidade do autor: ")
            data_nascimento = input("Digite a data de nascimento do autor (DD/MM/AAAA): ")
            ano_publicacao = int(input("Digite o ano de publicação: "))

            autor = Autor(nome_autor, nacionalidade, data_nascimento)
            livro = Livro(titulo, autor, ano_publicacao)
            biblioteca.adicionar_livro(livro)
            print("Livro adicionado com sucesso!")

        elif opçao == 2:
            titulo = input("Digite o título do livro a ser removido: ")
            
            if biblioteca.remover_livro(titulo):
                print("Livro removido com sucesso!")
            else:
                print("Livro não encontrado!")

        elif opçao == 3:
            titulo = input("Digite o título do livro a ser buscado: ")
            livro = biblioteca.buscar_livro(titulo)

            if livro:
                print(f"Livro encontrado: {livro}")
            else:
                print("Livro não encontrado!")

        elif opçao == 4:
            livros = biblioteca.listar_livros()

            if livros:
                print("\nLista de Livros:")
                for livro in livros:
                    print(livro)
            else:
                print("Nenhum livro na biblioteca.")

        elif opçao == 5:
            print("Saindo...")
            break

        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()