import random
import time


class JogarDados:
    def __init__(self):
        self.dado1 = random.randint(2,6)
        self.dado2 = random.randint(2,6)
    
    def jogar(self):
        return self.dado1, self.dado2



class JogadorUm:
    def __init__(self,nome):
        self.nome = nome
    
    def jogar(self):
        dados = JogarDados()
        dado1J1, dado2J1 = dados.jogar()
        pontoJogadorUm = dado1J1 + dado2J1
        return pontoJogadorUm

class JogadorDois:
    def __init__(self,nome):
        self.nome = nome
    
    def jogar(self):
        dados = JogarDados()
        dado1J2, dado2J2 = dados.jogar()
        pontoJogadorDois = dado1J2 + dado2J2
        return pontoJogadorDois

class Rodada:
    def rodar(self, j1, j2):
        pontoRodadaJogador1 = 0
        pontoRodadaJogador2 = 0
        while True:
            print("Jogando dados do jogador 1...")
            time.sleep(1.5)
            pontoJogadorUm = j1.jogar()
            print("Ponto J1: ", pontoJogadorUm)
            time.sleep(0.7)
            print("Jogando dados do jogador 2...")
            time.sleep(1.5)
            pontoJogadorDois = j2.jogar()
            print("Ponto J2: ",pontoJogadorDois)

            if pontoJogadorUm > pontoJogadorDois:
                pontoRodadaJogador1 +=1
                print("==========================================")
                print("==========================================")
                print("→ Jogador 1 ganhou essa rodada")
                
            elif pontoJogadorUm < pontoJogadorDois:
                pontoRodadaJogador2 += 1
                print("==========================================")
                print("==========================================")
                print("→ Jogador 2 ganhou essa rodada")

            else:
                print("Empatou!")
            
            print("==========================================")
            print("==========================================")

            print(f"Total de pontos até agora: J1: {pontoRodadaJogador1} e J2: {pontoRodadaJogador2}")

            print("==========================================")
            print("==========================================")
            
            jogarNovamente = input("Deseja jogar novamente (S/N)? ")

            if jogarNovamente == "N":
                print("==========================================")
                print("==========================================")
                print(f"♦ Total de pontos final: J1: {pontoRodadaJogador1} e J2: {pontoRodadaJogador2} ♦")
                print("==========================================")
                print("==========================================")
                print("Até mais!")
                break

def main():

    nomeJogador1 = input("Seu nome: ")
    nomeJogador2 = input("Seu nome: ")
    j1 = JogadorUm(nomeJogador1)
    j2 = JogadorDois(nomeJogador2)
    j1.jogar()
    j2.jogar()

    rodada = Rodada()
    rodada.rodar(j1, j2)

main()

