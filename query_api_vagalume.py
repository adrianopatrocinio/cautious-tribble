print('Cliente da Vagalume API Iniciado: \n')

nome_artista = input('Digite o nome de um Artista\n')

import busca

resultado = busca.artista(nome_artista)

newinput = input('Digite:\n-pos: para saber a posição do artista no ranking\n-album: para saber o ultimo álbum do artista\n-frequencia: para saber as palavras mais frequentes nas letras mais acessadas do artista\n-musicas n: para exibir as n musicas mais acessadas do artista (n = 0 para todas)\n')
if newinput == '-pos':
    print ('\nA posição do artista é '+ resultado.rank.pos)

elif newinput == '-frequencia':
    print('\nAs palavras mais frequêntes são:\n' + resultado.toplyrics.freq_palavras_toplyrics)

elif newinput == '-album':
    print('\nO ultimo album do artista é: '+resultado.albuns.ultimo)
else:
    newlist = newinput.split()
    resultado2 = busca.artista(nome_artista,int(newlist(1)))
    if newinput(0)=='-musicas':
        print('\nAs '+newlist(1)+'músicas mais acessadas do artista são: \n'+ resultado2.toplyrics.ntoplyrics)