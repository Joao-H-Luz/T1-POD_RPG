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

        try:
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
                try:
                    chance_de_ataque_p1 = D20().jogar() + Personagem_1.pontos_ataque
                    
                    if chance_de_ataque_p1 > Personagem_2.pontos_defesa:
                        dano = Personagem_1.atacar(Personagem_2)
                        log.write(
                            f"{Personagem_1.nome_personagem} atacou com {dano} de Dano. Vida restante de {Personagem_2.nome_personagem}: {Personagem_2.pontos_vida}\n")
                    else:
                        log.write(f"{Personagem_1.nome_personagem} errou o ataque!\n")

                except Exception as e:
                    log.write(f"Erro durante o turno do {Personagem_1.nome_personagem}: {e}\n")
                    continue

                if Personagem_2.pontos_vida <= 0:
                    vencedor = Personagem_1.nome_personagem
                    log.write(f"\n{vencedor} venceu o combate!\n")
                    print(f"\n{vencedor} venceu o combate!\n")
                    break

                # Turno do Personagem 2
                try:
                    chance_de_ataque_p2 = D20().jogar() + Personagem_2.pontos_ataque
                    log.write(
                        f"{Personagem_2.nome_personagem} atacou com {chance_de_ataque_p2} contra defesa {Personagem_1.pontos_defesa}\n")

                    if chance_de_ataque_p2 > Personagem_1.pontos_defesa:
                        dano = Personagem_2.atacar(Personagem_1)
                        log.write(
                            f"{Personagem_2.nome_personagem} atacou com {dano} de Dano. Vida restante de {Personagem_1.nome_personagem}: {Personagem_1.pontos_vida}\n")
                    else:
                        log.write(f"{Personagem_2.nome_personagem} errou o ataque!\n")

                except Exception as e:
                    log.write(f"Erro durante o turno do {Personagem_2.nome_personagem}: {e}\n")
                    continue

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
            
        except Exception as erro_geral:
            print(f"Ocorreu um erro durante o combate: {erro_geral}")

#  -================================================================================================================================================-  #
# Combate Free For All (FFA)
    def combate_free_for_all(self):
        try:
            # Cria o arquivo de log com timestamp
            time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            nome_arquivo = f"log_de_batalha_(FFA)_{time}.txt"
            
            try:
                with open(nome_arquivo, "w") as log:
                    log.write("--- Combate Free For All ---\n\n")
                    print("--- Combate Free For All ---")

                    # Dicionário de abates
                    vivos = self.lista_de_personagens.copy()
                    abates = {p.nome_personagem: 0 for p in vivos}
                    rodada = 1

                # Começo da Batalha
                while len(vivos) > 1:
                    log.write(f"--- Rodada {rodada} ---\n")
                    print(f"--- Rodada {rodada} ---")

                    for atacante in vivos.copy():
                        try:
                            if atacante.pontos_vida <= 0:
                                continue

                            alvos_possiveis = [p for p in vivos if p != atacante and p.pontos_vida > 0]
                            if not alvos_possiveis:
                                break

                            alvo = random.choice(alvos_possiveis)
                            chance_de_ataque = D20().jogar() + atacante.pontos_ataque

                            if chance_de_ataque > alvo.pontos_defesa:
                                dano = atacante.atacar(alvo)
                                log.write(f"{atacante.nome_personagem} atacou com {dano} de Dano. Vida restante de {alvo.nome_personagem}: {alvo.pontos_vida}\n")
                            else:
                                log.write(f"{atacante.nome_personagem} errou o ataque!\n")

                            if alvo.pontos_vida <= 0:
                                log.write(f"{alvo.nome_personagem} foi eliminado por {atacante.nome_personagem}!\n")
                                print(f"{alvo.nome_personagem} foi eliminado por {atacante.nome_personagem}!")
                                abates[atacante.nome_personagem] += 1
                                vivos.remove(alvo)

                            log.write("\n")

                        except Exception as e:
                            print(
                                f"Erro na ação do personagem {atacante.nome_personagem}: {e}")
                            log.write(
                                f"Erro na ação do personagem {atacante.nome_personagem}: {e}\n")
                            
                    rodada += 1

                vencedor = vivos[0]
                log.write(f"\n{vencedor.nome_personagem} venceu o Free For All!\n")
                print(f"\n{vencedor.nome_personagem} venceu o Free For All!\n")

                # Exibir o ranking de abates
                ranking = sorted(abates.items(), key=lambda x: x[1], reverse=True)
                log.write("\nRanking de Abates:\n")
                print("Ranking de Abates:")
                for nome, kills in ranking:
                    log.write(f"- {nome} eliminou {kills}\n")
                    print(f"- {nome} eliminou {kills}")

            except IOError as e:
                print(f"Erro ao abrir ou escrever o arquivo de log: {e}")

        except Exception as e:
            print(f"Erro inesperado no combate_free_for_all: {e}")

        print(f"Log salvo em: {nome_arquivo}")

#  -================================================================================================================================================-  #

# Feature Combate em ondas
def combate_onda(self):
    try:
        if len(self.lista_de_personagens) > 5:                  # Somente 5 Herois por combate
            print("Limite de 5 personagens na equipe para este modo de combate.")
            return

        time_herois = self.lista_de_personagens.copy()
        vivos = time_herois.copy()
        rodada = 1

        time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        nome_arquivo = f"log_de_batalha_onda_{time}.txt"

        try:
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
                        boss = Personagem(nome_personagem="Lorde Abissal",
                                        pontos_vida=200, pontos_ataque=30, pontos_defesa=25)
                        inimigos.append(boss)
                        qtd_inimigos -= 1
                        log.write(f"Boss chegou: {boss.nome_personagem}!\n")
                        print(f"Boss chegou: {boss.nome_personagem}!")

                    # Boss na rodada 10: Smaug, o Dourado
                    if rodada == 10:
                        boss = Personagem(nome_personagem="🐉 Smaug, o Dourado",
                                        pontos_vida=250, pontos_ataque=35, pontos_defesa=30)
                        inimigos.append(boss)
                        qtd_inimigos -= 1
                        log.write(f"Boss chegou: {boss.nome_personagem}!\n")
                        print(f"Boss chegou: {boss.nome_personagem}!")

                    # Criar inimigos comuns restantes
                    for i in range(qtd_inimigos):
                        try:
                            inimigo = Personagem(
                                nome_personagem=f"Inimigo {i+1}",
                                pontos_vida=50 + rodada*5,
                                pontos_ataque=10 + rodada*2,
                                pontos_defesa=5 + rodada)
                            inimigos.append(inimigo)

                        except Exception as e:
                            print(f"Erro ao criar inimigo {i+1}: {e}")
                            log.write(f"Erro ao criar inimigo {i+1}: {e}\n")

                    vivos_inimigos = inimigos.copy()

                    # Checar chance do bardo na rodada 5 convencer o Lorde Abissal
                    if rodada == 5:
                        try:
                            bardo_vivo = any(p.nome_personagem.lower() ==
                                            "bardo" and p.pontos_vida > 0 for p in vivos)
                            if bardo_vivo:
                                chance_bardo = random.random()
                                if chance_bardo <= 0.25:
                                    mensagem_bardo = "O bardo mandou aquela cantoria épica de 2 minutos de duração... até o Lorde Abissal pensou 'já perdi, vou deixar passar'."
                                    log.write(mensagem_bardo + "\n")
                                    print(mensagem_bardo)
                                    rodada += 1
                                    continue  # Passa direto para próxima rodada sem lutar

                        except Exception as e:
                            log.write(f"Erro na verificação do bardo: {e}\n")
                            print(f"Erro na verificação do bardo: {e}")

                    # Começa os turnos de ataque
                    # Ordem: heróis atacam primeiro, depois inimigos
                    while len(vivos) > 0 and len(vivos_inimigos) > 0:
                        # Heróis atacam
                        for heroi in vivos.copy():
                            try:
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

                            except Exception as e:
                                log.write(
                                    f"Erro no ataque do herói {heroi.nome_personagem}: {e}\n")
                                print(
                                    f"Erro no ataque do herói {heroi.nome_personagem}: {e}")

                        if len(vivos_inimigos) == 0:
                            break

                        # Inimigos atacam
                        for inimigo in vivos_inimigos.copy():
                            try:
                                if inimigo.pontos_vida <= 0:
                                    vivos_inimigos.remove(inimigo)
                                    continue

                                if len(vivos) == 0:
                                    break

                                alvo = random.choice(vivos)
                                chance_ataque = D20().jogar() + inimigo.pontos_ataque
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
                            
                            except Exception as e:
                                log.write(
                                    f"Erro no ataque do inimigo {inimigo.nome_personagem}: {e}\n")
                                print(
                                    f"Erro no ataque do inimigo {inimigo.nome_personagem}: {e}")

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

        except IOError as e:
            print(f"Erro ao abrir ou escrever o arquivo de log: {e}")

        print(f"Log salvo em: {nome_arquivo}")

    except Exception as e:
        print(f"Erro inesperado no combate em onda: {e}")

#  -================================================================================================================================================-  #
