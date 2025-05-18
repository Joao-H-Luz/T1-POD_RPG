# Bibliotecas Utilizadas
from RPG import Personagem
from SubClass import D20, D2, BolaDeFogo, Cura, TiroDeArco
import random
import datetime

#  -================================================================================================================================================-  #

class Arena:
    def __init__(self, lista_de_Personagens:list):
        self.lista_de_personagens = lista_de_Personagens

    def personagens(self):
        print("\n--- Personagens na Arena ---")
        for personagens in self.lista_de_personagens:           # Faz um looping para mostrar os personagens que estão na arena
            print(f"{personagens.nome_personagem} | Vida: {personagens.pontos_vida} | Ataque: {personagens.pontos_ataque} | Defesa: {personagens.pontos_defesa}")
        print("----------------------------\n")

    def adicionar_personagens(self, novo_personagem):           # Adiciona um Personagem a Arena
        self.lista_de_personagens.append(novo_personagem)
        return (f"{novo_personagem.nome} entrou na Arena")
    
    def remover_personagens(self, personagem):                  # Remove um Personagem da Arena
        if personagem in self.lista_de_personagens:             # Verifica se esse personagem esta na arena
            self.lista_de_personagens.remove(personagem)
            return (f"{personagem.nome} saiu da Arena")
        else:
            return f"{personagem.nome_personagem} não está na Arena"
        
# Funçoes de Batalha
#  -===============================================-  #

# Combate 1X1
    def combate_1x1(self, Personagem_1:Personagem, Personagem_2:Personagem):  # Realiza um combate 1x1 entre dois personagens.

#  --------------------------------------------------------------------  #
        # Cria o arquivo de log com timestamp
        time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") # Ajusta o nome do arquivo para a hora expecifica
        nome_arquivo = f"log_de_batalha_1x1_{time}.txt"
        log = open(nome_arquivo, "w") # Abre o arquivo para escrita

#  --------------------------------------------------------------------  #
        # Começo da Batalha

        log.write(f"--- Combate: {Personagem_1.nome_personagem} vs {Personagem_2.nome_personagem} ---\n\n")
        print(f"--- Combate: {Personagem_1.nome_personagem} vs {Personagem_2.nome_personagem} ---")
        rodada = 1

        while(Personagem_1.pontos_vida > 0 and Personagem_2.pontos_vida > 0):
            log.write(f"Rodada {rodada}\n")
            print(f"--- Rodada {rodada} ---")

#  --------------------------------------------------------------------  #

            # Turno do Personagem_1
            chance_de_ataque_p1 = D20().jogar() + Personagem_1.pontos_ataque
            
            if chance_de_ataque_p1 > Personagem_2.pontos_defesa:
                dano = Personagem_1.atacar(Personagem_2)
                log.write(
                    f"{Personagem_1.nome_personagem} atacou com {dano} de Dano. Vida restante de {Personagem_2.nome_personagem}: {Personagem_2.pontos_vida}\n")
            else:
                log.write(f"{Personagem_1.nome_personagem} errou o ataque!\n")

            if Personagem_2.pontos_vida <= 0:
                vencedor = Personagem_1.nome_personagem
                log.write(f"\n🏆 {vencedor} venceu o combate!\n")
                print(f"\n🏆 {vencedor} venceu o combate!\n")
                break

#  --------------------------------------------------------------------  #

            # Turno do Personagem 2
            chance_de_ataque_p2 = D20().jogar() + Personagem_2.pontos_ataque
            log.write(
                f"{Personagem_2.nome_personagem} atacou com {chance_de_ataque_p2} contra defesa {Personagem_1.pontos_defesa}\n")

            if chance_de_ataque_p2 > Personagem_1.pontos_defesa:
                dano = Personagem_2.atacar(Personagem_1)
                log.write(
                    f"{Personagem_2.nome_personagem} atacou com {dano} de Dano. Vida restante de {Personagem_1.nome_personagem}: {Personagem_1.pontos_vida}\n")
            else:
                log.write(f"{Personagem_2.nome_personagem} errou o ataque!\n")

            if Personagem_2.pontos_vida <= 0:
                vencedor = Personagem_1.nome_personagem
                log.write(f"\n🏆 {vencedor} venceu o combate!\n")
                print(f"\n🏆 {vencedor} venceu o combate!\n")
                break

#  --------------------------------------------------------------------  #
            # Fim da Round e Escrita do Arquivo
            log.write("\n")
            rodada += 1

#  --------------------------------------------------------------------  #
        # Fim da Batalha | Fecha o Arquivo "log_de_batalha_1x1_{time}.txt" | Declara o Arquivo de Log Salvo
        log.close()
        print(f"📄 Log salvo em: {nome_arquivo}")

#  -================================================================================================================================================-  #
# Combate Free For All (FFA)
    def combate_free_for_all(self):

#  --------------------------------------------------------------------  #
        # Cria o arquivo de log com timestamp
        time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        nome_arquivo = f"log_de_batalha_(FFA)_{time}.txt"
        
        with open(nome_arquivo, "w") as log:
            log.write("--- Combate Free For All ---\n\n")
            print("--- Combate Free For All ---")

#  --------------------------------------------------------------------  #

            # Lista de Modificação Interna
            vivos = self.lista_de_personagens.copy()
            rodada = 1

# Começo da Batalha
            while len(vivos) > 1:                       # Verificação de parada, compara se ainda tem combatentes ativos (minimo 2)
                log.write(f"--- Rodada {rodada} ---\n")
                print(f"--- Rodada {rodada} ---")

                for atacante in vivos.copy():
                    if atacante.pontos_vida <= 0:       # Pula o personagem morto
                        continue  

                    alvos_possiveis = [p for p in vivos if p != atacante and p.pontos_vida > 0] # Lista de Alvos disponives
                    if not alvos_possiveis:
                        break                           # Ninguém mais pra atacar

                    alvo = random.choice(alvos_possiveis) # O alvo é escolhido aleatóriamente
                    chance_de_ataque = D20().jogar() + atacante.pontos_ataque

                    if chance_de_ataque > alvo.pontos_defesa:
                        dano = atacante.atacar(alvo)
                        log.write(f"{atacante.nome_personagem} atacou com {dano} de Dano. Vida restante de {alvo.nome_personagem}: {alvo.pontos_vida}\n")

                    else:
                        log.write(f"{atacante.nome_personagem} errou o ataque!\n")

                    # Remove da lista de vivos se morreu
                    if alvo.pontos_vida <= 0:
                        log.write(f"💀 {alvo.nome_personagem} foi eliminado!\n")
                        print(f"💀 {alvo.nome_personagem} foi eliminado!")
                        vivos.remove(alvo)

                    log.write("\n")
                rodada += 1

            vencedor = vivos[0]
            log.write(f"\n🏆 {vencedor.nome_personagem} venceu o Free For All!\n")
            print(f"\n🏆 {vencedor.nome_personagem} venceu o Free For All!\n")

        print(f"📄 Log salvo em: {nome_arquivo}")

#  -================================================================================================================================================-  #