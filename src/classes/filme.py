from src.classes.programacao import Programacao

class Filme(Programacao):
    def __init__(self, id, nome, genero, idioma, legenda, ano, duracao):                            
        super().__init__(id, nome, genero, idioma, legenda, ano)
        self.__duracao = int(duracao)
    

    @property
    def duracao(self):
        return self.__duracao
        
    def __str__(self):
        return f'''
        Detalhes do filme {self.nome}:
            Gênero: {self.genero}
            Idioma: {self.idioma}
            Legenda: {self.legenda}
            Ano: {self.ano}
            Duração: {self.__duracao} min'''

