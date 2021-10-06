from src.dao.programacao_dao import ProgramacaoDAO

class FilmeDAO(ProgramacaoDAO):
    def __init__(self, instancia_filme):
        super().__init__(instancia_filme)
        self._programacao_json['duracao'] = instancia.duracao 