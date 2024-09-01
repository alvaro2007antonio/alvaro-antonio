from livro import Livro

class Biblioteca:
    def __init__(self):
        self.__livros = []

    def adicionar_livro(self, livro):
        self.__livros.append(livro)
        
    def remover_livro(self, titulo):
        for livro in self.__livros:
            if livro.get_titulo().lower() == titulo.lower():
                self.__livros.remove(livro)
                return True
        return False
        
    def buscar_livro(self, titulo):
        for livro in self.__livros:
            if livro.get_titulo().lower() == titulo.lower():
              return livro
        return None
    
    def listar_livros(self):
        return self.__livros