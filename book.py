from autor import Autor

class Livro:
    def __init__(self, titulo, autor, anopublicação):
        self.__titulo = titulo
        self.__autor = autor
        self.__anopublicação = anopublicação

    def getTitulo(self):
        return self.__titulo
    
    def getAutor(self):
        return self.__autor
    
    def getAnopublicação(self):
        return self.__anopublicação
    
    def setTitulo(self, titulo):
        self.__titulo = titulo

    def setAutor(self, autor):
        self.__autor = autor

    def setAnopublicação(self, anopublicação):
        self.__anopublicação = anopublicação

    def __str__(self):
        return (f"Titulo:{self.__titulo}, Autor:{self.__autor}, Ano da Publicação{self.__anopublicação}") 