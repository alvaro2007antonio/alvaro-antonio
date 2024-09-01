class Autor:
    def __init__(self, nome, nacionalidade, datanascimento):
        self.__nome = nome
        self.__nacionalidade = nacionalidade
        self.__datanascimento = datanascimento

    def getNome(self):
        return self.__nome
    
    def getNacionalidade(self):
        return self.__nacionalidade
    
    def getDatanascimento(self):
        return self.__datanascimento
    
    def setNome(self, nome):
        self.__nome = nome

    def setNacionalidade(self, nacionalidade):
        self.__nacionalidade = nacionalidade

    def setDatanascimento(self, datanascimento):
        self.__datanascimento = datanascimento

    def exibir_autor(self):
        return (f"Nome:{self.__nome},Nacionalidade:{self.__nacionalidade}, Data de Nascimento:{self.__datanascimento}")