# teste.py

import requests


def artista(nome_artista):
    consulta = requests.get('https://api.vagalume.com.br/search.php', params={'art': nome_artista})
    consulta = consulta.json()
    consulta_index = request.get(consulta['art']['url'])
    return IndexArtista(consulta_index.json())

class Toplyrics(object):
    def __init__(self, toplyrics):
        while i < len(toplyrics['item'])
            self.todotoplyrics[i] = toplyrics['item'][i]['desc']

    def n_toplyrics(self,n)
        while i < n
            ntoplyrics[i]=todotoplyrics[i]
        return ntoplyrics[]

class Álbuns(object):
    def __init__(self,albuns):
        while i < len(albuns['item'])
            self.todosalbuns[i] = albuns['item'][i]['desc']



class IndexArtista(object):
    def __init__(self, index):
        id = index['id']
        genre = index['genre']
        toplyrics = index['toplyrics']
        pos = index['rank']['pos']
        albuns = index['albums']

        self.genre = Gênero(genero)
        self.toplyrics = Toplyrics(toplyrics)
        self.albuns = Álbuns(albuns)

