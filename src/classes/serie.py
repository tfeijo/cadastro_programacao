from src.classes.programacao import Programacao

class Serie(Programacao):
    def __init__(self, id, nome, genero, idioma, legenda, ano, duracao):
        super().__init__(id, nome, genero, idioma, legenda, ano)
        self.__duracao = str(duracao).title()
    
    @property
    def duracao(self):
        return self.__duracao

    def __str__(self):
        return f'''
        Detalhes da série {self.nome}:
            Gênero: {self.genero}
            Idioma: {self.idioma}
            Legenda: {self.legenda}
            Ano: {self.ano}
            Duração: {self.__duracao} episódio(s)
        '''