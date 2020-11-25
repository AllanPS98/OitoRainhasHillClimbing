import Rainha
import random as rnd


class Hill:
    def __init__(self):
        pass

    def avaliacao(self, lista_rainhas, gabarito):
        pontuacao = 8
        for i in range(8):
            if lista_rainhas[i].__getY__() != gabarito[i]:
                pontuacao -= 1
        return pontuacao

    def mutacao(self, lista_rainhas):
        posicao1 = rnd.randint(0,7)
        posicao2 = rnd.randint(0,7)
        while posicao2 == posicao1:
            posicao2 = rnd.randint(0, 7)
        aux = lista_rainhas[posicao1].__getY__()
        lista_rainhas[posicao1].__setY__(lista_rainhas[posicao2].__getY__())
        lista_rainhas[posicao2].__setY__(aux)
        return lista_rainhas
