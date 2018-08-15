 #busca.py
import requests


def artista(nome_artista):
    consulta = requests.get('https://api.vagalume.com.br/search.php', params={'art': nome_artista})
    consulta = consulta.json()
    consulta_index = requests.get(consulta['art']['url']+'index.js')
    consulta_index = consulta_index.json()
    return IndexArtista(consulta_index['artist'])

class Toplyrics(object):
    def __init__(self, toplyrics):
        self.quanttoplyrics = len(toplyrics)
        self.todotoplyrics = range(quanttoplyrics)
        i=0
        while i < len(toplyrics['item']):
            self.todotoplyrics[i] = toplyrics['item'][i]['desc']
            i=i+1

    def n_toplyrics(self,n):
        self.toplyrics = range(n)
        i=0
        while i < n:
            self.toplyrics[i] = self.todotoplyrics[i]
            i=i+1
        return ntoplyrics
    ##def fetch_lyrics(self,n=len(toplyrics)):

class Álbuns(object):
    def __init__(self,albuns):
        self.todosalbuns = range(len(albuns))
        while i < len(albuns['item']):
            self.todosalbuns[i] = albuns['item'][i]['desc']
            i=i+1

class Gênero(object):
    def __init__(self, genre):
        i=0
        while i < len(genre):
            self.genero[i] = genre[i]['name']
            i=i+1


class RankArtista(object):
    def __init__(self,pos):
        self.rank = pos['pos']

class IndexArtista(object):
    def __init__(self, index):
        id = index['id']
        genre = index['genre']
        toplyrics = index['toplyrics']
        pos = index['rank']
        albuns = index['albums']

        self.pos = RankArtista(pos)
        self.genre = Gênero(genre)
        self.toplyrics = Toplyrics(toplyrics)
        self.albuns = Álbuns(albuns)