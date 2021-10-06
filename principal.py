from src.classes.filme import Filme
from src.classes.serie import Serie
from src.dao.serie_dao import SerieDAO

novo_filme = Filme(1, "John Wick", "Ação", "Inglês", "Português", 2020, 93)
#print(novo_filme)

nova_serie = Serie(1, "Breaking Bad", "Ação", "Inglês", "Espanhol", 2011, 53)

nova_serie_dao = SerieDAO(nova_serie)

print(nova_serie_dao)

