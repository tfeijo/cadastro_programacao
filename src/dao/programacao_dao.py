
class ProgramacaoDAO():
    def __init__(self, instancia_programacao):
        self._programacao_json = {}
        self.preenche_valores_json(instancia_programacao)
    
    def preenche_valores_json(self, instancia):
        self._programacao_json['id'] = instancia.id
        self._programacao_json['nome'] = instancia.nome
        self._programacao_json['genero'] = instancia.genero
        self._programacao_json['idioma'] = instancia.idioma
        self._programacao_json['legenda'] = instancia.legenda
        self._programacao_json['ano'] = instancia.ano
        self._programacao_json['avaliacao'] = instancia.avaliacao
        self._programacao_json['favorito'] = instancia.favorito
    
    def __str__(self):
        return str(self._programacao_json)
        

