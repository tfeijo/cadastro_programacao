from src.classes.filme import Filme
from src.classes.serie import Serie
from src.dao.serie_dao import SerieDAO
from src.bd.bd_connection import bd

nova_serie = Serie(1, "Breaking Bad", "Ação", "Inglês", "Espanhol", 2011, 53)
nova_serie_dao = SerieDAO(nova_serie)
bd.insert_in_BD(nova_serie_dao._programacao_json)