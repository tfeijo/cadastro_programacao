from src.classes.programacao import Programacao

class Filme(Programacao):
    def __init__(self, id, nome, genero, idioma, legenda, ano, duracao):
        super().__init__(id, nome, genero, idioma, legenda, ano)
        self.__duracao = int(duracao)
    
    def __str__(self):
        return f'''
        Detalhes do filme {self.__nome}:
            Gênero: {self.__genero}
            Idioma: {self.__idioma}
            Legenda: {self.__legenda}
            Ano: {self.__ano}
            Duração: {self.__duracao} min
        '''

