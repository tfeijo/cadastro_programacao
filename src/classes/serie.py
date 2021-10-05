from src.classes.programacao import Programacao

class Serie(Programacao):
    def __init__(self, id, nome, genero, idioma, legenda, ano, duracao):
        super().__init__(id, nome, genero, idioma, legenda, ano)
        self.__duracao = str(duracao).title()
    
    def __str__(self):
        return f'''
        Detalhes da série {self.__nome}:
            Gênero: {self.__genero}
            Idioma: {self.__idioma}
            Legenda: {self.__legenda}
            Ano: {self.__ano}
            Duração: {self.__duracao} episódio(s)
        '''