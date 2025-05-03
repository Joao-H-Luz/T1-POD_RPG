# Bibliotecas Utilizadas
from abc import ABC, abstractmethod
from random import randint

# Classes Obrigatórias:

class Dado(ABC):
    def __init__(self, lados=int):
        super().__init__()
        self.lados = lados

    def jogar(self):
        numero_do_dado = randint(1, self.lados + 1)
        return numero_do_dado
    
class Classe(ABC):
    def __init__(self, nome=str, pontos_vida=float, dado_de_ataque=int,
                 pontos_ataque=float, pontos_defesa=float, limite_habilidades=int):
        super().__init__()
        self.nome = nome
        self.pontos_vida = pontos_vida
        self.dado_de_ataque = dado_de_ataque
        self.pontos_ataque = pontos_ataque
        self.pontos_defesa = pontos_defesa
        self.limite_habilidades = limite_habilidades

class Habilidade:
    def __init__(self, nome=str, descricao=str, pontos_ataque=str):
        self.nome = nome
        self.descricao = descricao
        self. pontos_ataque = pontos_ataque

    def usar():
        # Método que simula o uso da habilidade
        pass

class Personagem(Classe):
    instancias = 0

    def __init__(self, nome_personagem=str, nome=str, pontos_vida=float, dado_de_ataque=int, pontos_ataque=float, pontos_defesa=float, limite_habilidades=int, inventario=list):
        super().__init__(nome, pontos_vida, dado_de_ataque, pontos_ataque, pontos_defesa, limite_habilidades)
        self.nome_personagem = nome_personagem
        self.inventario = inventario
        Personagem.qntd_instancias()
                         
    @classmethod
    def qntd_instancias(cls):
        cls.instancias += 1

    def atacar(self, Alvo):
        pass

class Arena:
    lista_de_personagens = list

    @classmethod
    def adicionar_personagens(cls, personagem):
        pass

    @classmethod
    def personagens(cls):
        return Arena.lista_de_personagens