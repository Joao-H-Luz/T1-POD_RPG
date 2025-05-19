# Bibliotecas Utilizadas
from .Dado import *
from .Classe import *
from .Habilidade import *

# -- Personagem --

class Personagem:
    instancias = 0

    def __init__(self, nome_personagem: str, classe: Classe, inventario: list):
        self.nome_personagem = nome_personagem
        self.pontos_vida = classe.pontos_vida
        self.dado_de_ataque = classe.dado_de_ataque
        self.pontos_ataque = classe.pontos_ataque
        self.pontos_defesa = classe.pontos_defesa
        self.limite_habilidade = classe.limite_habilidades
        self.inventario = inventario
        self.classe = classe.classe
        Personagem.instancias += 1

    @classmethod
    def qntd_instancias(cls):
        return cls.instancias

    def atacar(self, alvo):
        # Se tem habilidades no inventário e D2 sorteou 2, usa habilidade
        if len(self.inventario) > 0 and D2().jogar() == 2:
            # Usa a primeira habilidade no inventário
            efeito = self.usar_habilidade(alvo)
            # Retorna o valor do efeito (positivo cura, negativo dano)
            return efeito

        # Ataque normal:
        ataque_total = self.dado_de_ataque.jogar() + self.pontos_ataque
        dano_final = ataque_total - alvo.pontos_defesa
        dano_final = max(0, dano_final)  # dano mínimo zero, não cura o inimigo
        alvo.pontos_vida -= dano_final
        return dano_final

    def usar_habilidade(self, alvo):
        # Usa a habilidade no alvo e remove do inventário
        habilidade = self.inventario.pop(0)
        efeito = habilidade.usar(alvo)
        return efeito

    def __eq__(self, personagem_2):
        return self.nome_personagem == personagem_2.nome_personagem and self.classe == personagem_2.classe

    def __str__(self):
        return (f"Nome: {self.nome_personagem} | Classe: {self.classe} | Inventario: {self.ver_inventario()}")

    def __repr__(self):
        return (f"Nome: {self.nome_personagem} | Classe: {self.classe} | Inventario: {self.ver_inventario()}")

    def ver_inventario(self):
        return ', '.join(str(habilidade) for habilidade in self.inventario)

#  -================================================================================================================================================-  #