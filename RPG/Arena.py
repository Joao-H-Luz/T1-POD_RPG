# Bibliotecas Utilizadas
from .Personagem import *
from .Dado import *
from .Classe import *
from .Habilidade import *
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
        return (f"{novo_personagem.nome_personagem} entrou na Arena")
    
    def remover_personagens(self, personagem):                  # Remove um Personagem da Arena
        if personagem in self.lista_de_personagens:             # Verifica se esse personagem esta na arena
            self.lista_de_personagens.remove(personagem)
            return (f"{personagem.nome_personagem} saiu da Arena")
        else:
            return f"{personagem.nome_personagem} não está na Arena"
        
# Funçoes de Batalha
#  -===============================================-  #

# Combate 1X1
    def combate_1x1(self, Personagem_1:Personagem, Personagem_2:Personagem):  # Realiza um combate 1x1 entre dois personagens.
        # Cria o arquivo de log com timestamp
        time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") # Ajusta o nome do arquivo para a hora expecifica
        nome_arquivo = f"log_de_batalha_1x1_{time}.txt"
        log = open(nome_arquivo, "w") # Abre o arquivo para escrita

        # Começo da Batalha

        log.write(f"--- Combate: {Personagem_1.nome_personagem} vs {Personagem_2.nome_personagem} ---\n\n")
        print(f"--- Combate: {Personagem_1.nome_personagem} vs {Personagem_2.nome_personagem} ---")
        rodada = 1

        while(Personagem_1.pontos_vida > 0 and Personagem_2.pontos_vida > 0):
            log.write(f"Rodada {rodada}\n")
            print(f"--- Rodada {rodada} ---")

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
                log.write(f"\n{vencedor} venceu o combate!\n")
                print(f"\n{vencedor} venceu o combate!\n")
                break

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
                log.write(f"\n{vencedor} venceu o combate!\n")
                print(f"\n{vencedor} venceu o combate!\n")
                break

            # Fim da Round e Escrita do Arquivo
            log.write("\n")
            rodada += 1

        # Fim da Batalha | Fecha o Arquivo "log_de_batalha_1x1_{time}.txt" | Declara o Arquivo de Log Salvo
        log.close()
        print(f"Log salvo em: {nome_arquivo}")

#  -================================================================================================================================================-  #

    def combate_free_for_all(self):

        # Cria o arquivo de log com timestamp
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        nome_arquivo = f"log_de_batalha_(FFA)_{timestamp}.txt"

        with open(nome_arquivo, "w") as log:
            log.write("--- Combate Free For All ---\n\n")
            print("--- Combate Free For All ---")

            # Copia a lista de personagens vivos e inicializa abates
            vivos = self.lista_de_personagens.copy()
            abates = {p.nome_personagem: 0 for p in vivos}
            rodada = 1

            # Loop principal: continua enquanto tiver mais de um vivo
            while len(vivos) > 1:
                log.write(f"--- Rodada {rodada} ---\n")
                print(f"--- Rodada {rodada} ---")

                for atacante in vivos.copy():
                    if atacante.pontos_vida <= 0:
                        continue

                    # Seleciona alvos possíveis (exceto o próprio atacante)
                    alvos_possiveis = [p for p in vivos if p !=
                                    atacante and p.pontos_vida > 0]

                    if not alvos_possiveis:
                        # Não tem mais alvos: termina o combate
                        vivos = [atacante]
                        break

                    alvo = random.choice(alvos_possiveis)
                    chance_de_ataque = D20().jogar() + atacante.pontos_ataque

                    if chance_de_ataque > alvo.pontos_defesa:
                        dano = atacante.atacar(alvo)
                        log.write(
                            f"{atacante.nome_personagem} atacou com {dano} de Dano. Vida restante de {alvo.nome_personagem}: {alvo.pontos_vida}\n")
                    else:
                        log.write(f"{atacante.nome_personagem} errou o ataque!\n")

                    if alvo.pontos_vida <= 0:
                        log.write(
                            f"{alvo.nome_personagem} foi eliminado por {atacante.nome_personagem}!\n")
                        print(
                            f"{alvo.nome_personagem} foi eliminado por {atacante.nome_personagem}!")
                        abates[atacante.nome_personagem] += 1
                        vivos.remove(alvo)

                    log.write("\n")

                rodada += 1

            # Ao sair do loop, só resta um vencedor
            vencedor = vivos[0]
            log.write(f"\n{vencedor.nome_personagem} venceu o Free For All!\n")
            print(f"\n{vencedor.nome_personagem} venceu o Free For All!\n")

            # Ranking de abates
            ranking = sorted(abates.items(), key=lambda x: x[1], reverse=True)
            log.write("\nRanking de Abates:\n")
            print("Ranking de Abates:")
            for nome, kills in ranking:
                log.write(f"- {nome} eliminou {kills}\n")
                print(f"- {nome} eliminou {kills}")

        print(f"Log salvo em: {nome_arquivo}")

#  -================================================================================================================================================-  #

@staticmethod
def combate_onda(lista_herois):
    if len(lista_herois) != 5:
        print("É necessário selecionar exatamente 5 heróis para o combate em ondas.")
        return

    vivos = lista_herois.copy()
    rodada = 1

    time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    nome_arquivo = f"log_de_batalha_onda_{time}.txt"

    with open(nome_arquivo, "w") as log:
        log.write("--- Combate em Onda ---\n\n")
        print("--- Combate em Onda ---")

        while rodada <= 10 and len(vivos) > 0:
            log.write(f"\n--- Rodada {rodada} ---\n")
            print(f"\n--- Rodada {rodada} ---")

            # Criar inimigos da rodada (onda cresce: rodada * 2 inimigos)
            inimigos = []
            qtd_inimigos = rodada * 2

            # Boss na rodada 5: Lorde Abissal
            if rodada == 5:
                boss = Personagem(nome_personagem="Lorde Abissal",classe=Lorde_Abissal(), inventario=[])
                inimigos.append(boss)
                qtd_inimigos -= 1
                log.write(f"Boss chegou: {boss.nome_personagem}!\n")
                print(f"Boss chegou: {boss.nome_personagem}!")

            # Boss na rodada 10: Smaug, o Dourado
            if rodada == 10:
                boss = Personagem(nome_personagem="🐉 Smaug, o Dourado", classe=Smaug_Dourado(), inventario=[])
                inimigos.append(boss)
                qtd_inimigos -= 1
                log.write(f"Boss chegou: {boss.nome_personagem}!\n")
                print(f"Boss chegou: {boss.nome_personagem}!")

            # Criar inimigos comuns restantes
            for i in range(qtd_inimigos):
                inimigo = Personagem(nome_personagem=f"Inimigo {i+1}",
                    classe= Barbaro(),
                    inventario= [])
                inimigos.append(inimigo)

            vivos_inimigos = inimigos.copy()

            # Checar chance do bardo na rodada 5 convencer o Lorde Abissal
            if rodada == 5:
                bardo_vivo = any(p.nome_personagem.lower() ==
                                 "bardo" and p.pontos_vida > 0 for p in vivos)
                if bardo_vivo:
                    chance_bardo = random.random()
                    if chance_bardo <= 0.25:
                        mensagem_bardo = "O bardo mandou aquela cantoria épica de 2 minutos de duração... até o Lorde Abissal pensou 'já perdi, vou deixar passar'."
                        log.write(mensagem_bardo + "\n")
                        print(mensagem_bardo)
                        rodada += 1
                        continue  # Pula direto para a próxima rodada sem lutar

            # Começam os turnos de ataque
            while len(vivos) > 0 and len(vivos_inimigos) > 0:
                # Heróis atacam primeiro
                for heroi in vivos.copy():
                    if heroi.pontos_vida <= 0:
                        vivos.remove(heroi)
                        continue
                    if len(vivos_inimigos) == 0:
                        break
                    alvo = random.choice(vivos_inimigos)
                    chance_ataque = D20().jogar() + heroi.pontos_ataque
                    if chance_ataque > alvo.pontos_defesa:
                        dano = heroi.atacar(alvo)
                        log.write(
                            f"{heroi.nome_personagem} atacou {alvo.nome_personagem} com {dano} de dano. Vida restante: {alvo.pontos_vida}\n")
                    else:
                        log.write(
                            f"{heroi.nome_personagem} errou o ataque em {alvo.nome_personagem}.\n")
                    if alvo.pontos_vida <= 0:
                        log.write(f"{alvo.nome_personagem} foi eliminado!\n")
                        print(f"{alvo.nome_personagem} foi eliminado!")
                        vivos_inimigos.remove(alvo)

                # Inimigos atacam depois
                for inimigo in vivos_inimigos.copy():
                    if inimigo.pontos_vida <= 0:
                        vivos_inimigos.remove(inimigo)
                        continue
                    if len(vivos) == 0:
                        break
                    alvo = random.choice(vivos)
                    chance_ataque = D10().jogar() + inimigo.pontos_ataque
                    if chance_ataque > alvo.pontos_defesa:
                        dano = inimigo.atacar(alvo)
                        log.write(
                            f"{inimigo.nome_personagem} atacou {alvo.nome_personagem} com {dano} de dano. Vida restante: {alvo.pontos_vida}\n")
                    else:
                        log.write(
                            f"{inimigo.nome_personagem} errou o ataque em {alvo.nome_personagem}.\n")
                    if alvo.pontos_vida <= 0:
                        log.write(f"{alvo.nome_personagem} foi eliminado!\n")
                        print(f"{alvo.nome_personagem} foi eliminado!")
                        vivos.remove(alvo)

            if len(vivos) == 0:
                log.write("\nTodos os heróis foram derrotados!\n")
                print("\nTodos os heróis foram derrotados! Fim da batalha.")
                break

            log.write(f"\nFim da rodada {rodada}.\n")
            print(f"Fim da rodada {rodada}.")

            rodada += 1

        if len(vivos) > 0:
            log.write("\nOs heróis sobreviveram até o fim das 10 rodadas!\n")
            print("\nOs heróis sobreviveram até o fim das 10 rodadas!")
        else:
            log.write(
                "\nOs heróis foram derrotados antes de chegar ao fim das 10 rodadas.\n")
            print("\nOs heróis foram derrotados antes de chegar ao fim das 10 rodadas.")

        print(f"Log salvo em: {nome_arquivo}")

#  -================================================================================================================================================-  #