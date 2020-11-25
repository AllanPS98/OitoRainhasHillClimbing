import random as rnd
import Rainha
import Hill

gabarito_Y = [6, 4, 2, 0, 5, 7, 1, 3]
a = list(range(0, 8))
b = list(range(0, 8))
print(a)
rnd.shuffle(b)
print(b)

lista_rainhas = []
for i in range(8):
    rainha = Rainha.Rainha(a[i], b[i])
    lista_rainhas.append(rainha)

for rainha in lista_rainhas:
    print(rainha.__getPosicao__(), end=' ')
print('\n')

hill = Hill.Hill()
ant = lista_rainhas.copy()
pontuacao = hill.avaliacao(lista_rainhas, gabarito_Y)
pontuacao_antiga = pontuacao
while pontuacao != 8:
    lista_rainhas = hill.mutacao(lista_rainhas)
    pontuacao = hill.avaliacao(lista_rainhas, gabarito_Y)
    while pontuacao_antiga >= pontuacao:
        lista_rainhas = hill.mutacao(lista_rainhas)
        pontuacao_antiga = pontuacao
        pontuacao = hill.avaliacao(lista_rainhas, gabarito_Y)

print("Resultado")
for rainha in lista_rainhas:
    print(rainha.__getPosicao__(), end=' ')
print('\n')
print("Gabarito")
print(gabarito_Y)






