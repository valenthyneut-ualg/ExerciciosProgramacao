# Algoritmo do jogo da Forca:
#
#    início
#      escrever "Insira uma palavra para usar no jogo da forca: "
#      ler palavra
#
#      palavraTraço = "_" * tamanho(palavra)
#      letrasAdivinhadas = []
#
#      tentativas = 10
#
#      repetir
#        escrever "{palavaTraço}"
#        escrever "Jogador, escreva uma letra da palavra: "
#
#        ler letra
#        se letrasAdivinhadas.contem(letra)
#          escrever "Já adivinhou essa letra!"
#        senão
#          letrasAdivinhadas.adicionar(letra)
#
#          se palavra.contem(letra)
#            indicesLetra = palavra.indicesDe(letra)
#            por indice em indicesLetra
#              palavraTraço[indice] = letra
#
#            se palavraTraço == palavra
#              escrever "Ganhou! A palavra era '{palavra}'."
#              quebrar repetir
#          senão
#            tentativas -= 1
#            se tentativas == 0
#              escrever "Perdeu! A palavra era '{palavra}'."
#              quebrar repetir
#            senão
#              escrever "Ups! Adivinhou incorretamente. Tem {tentativas} tentativas."

from Hangman.Controller import Controller

if __name__ == '__main__':
	Controller().start()