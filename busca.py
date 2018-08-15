 #busca.py
import requests
from nltk.corpus import stopwords

def artista(nome_artista, n=0):
    consulta = requests.get('https://api.vagalume.com.br/search.php', params={'art': nome_artista})
    consulta = consulta.json()
    consulta_index = requests.get(consulta['art']['url']+'index.js')
    consulta_index = consulta_index.json()
    return IndexArtista(consulta_index['artist'], n)

class Toplyrics(object):
    def __init__(self, toplyrics,n):
        for i in range(len(toplyrics['item'])):
            if i ==0:
                self.todotoplyrics = toplyrics['item'][0]['desc'] + '\n'
            else:
                self.todotoplyrics = self.todotoplyrics + toplyrics['item'][i]['desc'] +'\n'

        if n > 0:
            for i in range(n):
                if i ==0:
                   self.ntoplyrics = toplyrics['item'][0]['desc'] + '\n'
                else:
                    self.ntoplyrics = self.ntoplyrics + toplyrics['item'][i]['desc'] +'\n'

        for i in range(len(toplyrics['item'])):
            lyrics = requests.get('https://api.vagalume.com.br/search.php', params={'musid':toplyrics['item'][i]['id']})
            lyrics = lyrics.json()
            if i ==0:
                totallyrics = lyrics['mus'][0]['text']
            else:
                totallyrics = totallyrics + lyrics['mus'][0]['text']
        stopWords = set(stopwords.words('portuguese'))
        listalyrics = totallyrics.split()
        frequencia = []
        for i in listalyrics:
            if i not in stopWords:
                frequencia.append(listalyrics.count(i))
        dictionary = dict((zip(listalyrics, frequencia)))
        for key in dictionary:
            list = [(key,dictionary[key])]
        list.sort()
        list.reverse()
        self.freq_palavras_toplyrics = list

class Álbuns(object):
    def __init__(self,albuns):
        self.ultimo = albuns['item'][0]['desc']
        for i in range(len(albuns['item'])):
            if i ==0:
                self.todosalbuns = albuns['item'][i]['desc'] + '\n'
            else:
                self.todosalbuns = self.todosalbuns + albuns['item'][i]['desc'] + '\n'

class Gênero(object):
   def __init__(self, genre):
       for i in range(len(genre)):
           if i == 0:
               self.gênero = genre[i]['name'] + '\n'
           else:
               self.gênero = self.gênero + genre[i]['name'] + '\n'


class RankArtista(object):
    def __init__(self,rank):
        self.pos = rank['pos']

class IndexArtista(object):
    def __init__(self, index,n):
        id = index['id']
        genre = index['genre']
        toplyrics = index['toplyrics']
        rank = index['rank']
        albuns = index['albums']

        self.rank = RankArtista(rank)
        self.genre = Gênero(genre)
        self.toplyrics = Toplyrics(toplyrics,n)
        self.albuns = Álbuns(albuns)