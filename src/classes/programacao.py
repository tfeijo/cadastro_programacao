class Programacao:
    def __init__(self, id, nome, genero, idioma, legenda, ano):
        self.__id = int(id)
        self.__nome = str(nome)
        self.__genero = str(genero)
        self.__idioma = str(idioma)
        self.__legenda = str(legenda)
        self.__ano = int(ano)
        self.__avaliacao = int(0)
        self.__favorito = False

    @property
    def nome(self):
        return self.__nome
    
    @property
    def genero(self):
        return self.__genero
    
    @property
    def idioma(self):
        return self.__idioma
    
    @property
    def legenda(self):
        return self.__legenda
    
    @property
    def ano(self):
        return self.__ano
    
    @property
    def avaliacao(self):
        return self.__avaliacao
    
    @property
    def favorito(self):
        return self.__favorito
    
    def incrementa_avaliacao(self):
        self.__avaliacao += 1
    
    def __str__(self):
        pass

    def favoritar_programacao(self):
        self.__favorito = True

    def desfavoritar_programacao(self):
        self.__favorito = False
    
    def reproduzir(self):
        print("Programação sendo reproduzida")
    
    
    def velocidade_reproducao(self, velocidade_reproducao):
        print(f"Programação sendo reproduzida na velocidade x{velocidade_reproducao}")

    def pausar(self):
        print("Programação sendo pausada")


