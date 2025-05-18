# Bibliotecas Utilizadas
from abc import ABC, abstractmethod
from SubClass import D2, BolaDeFogo, Cura, TiroDeArco, Guerreiro, Mago, Ladino

# Classes Obrigatórias:
#  -================================================================================================================================================-  #

# -- Dado --

class Dado(ABC):
    def __init__(self, lados: int):
        super().__init__()
        self.lados = lados  # Quantos Lados tem o Dado

    @abstractmethod
    def jogar(self):        # Metodo que Simula jogar o Dado
        pass

    @abstractmethod
    def __repr__(self):     # Metodo de Representação da Classe
        pass

#  -===============================================-  #

    # Metodos de Comparação de Dados

    def __eq__(self, dado):                 # Metodo de Comparação ==
        return self.lados == dado.lados

    def __ne__(self, dado):                 # Metodo de Comparação !=
        return self.lados != dado.lados

    def __lt__(self, dado):                 # Metodo de Comparação <
        return self.lados < dado.lados

    def __le__(self, dado):                 # Metodo de Comparação <=
        return self.lados <= dado.lados

    def __gt__(self, dado):                 # Metodo de Comparação >
        return self.lados > dado.lados

    def __ge__(self, dado):                 # Metodo de Comparação >=
        return self.lados >= dado.lados

#  -================================================================================================================================================-  #

# -- Classe --


class Classe(ABC):
    def __init__(self, classe: str, pontos_vida: float, dado_de_ataque: int,
                 pontos_ataque: float, pontos_defesa: float, limite_habilidades: int):
        super().__init__()
        self.classe = classe  # Nome da Classe
        self.pontos_vida = pontos_vida  # Vida do Objeto
        self.dado_de_ataque = dado_de_ataque
        # Dado de Ataque mais Pontos de Ataque == Ataque Final
        self.pontos_ataque = pontos_ataque
        self.pontos_defesa = pontos_defesa
        # Limite de Habilidades que a Classe pode ter no Inventario
        self.limite_habilidades = limite_habilidades

    @abstractmethod
    def __repr__(self):
        pass

#  -================================================================================================================================================-  #

# -- Habilidade --

class Habilidade(ABC):
    def __init__(self, nome: str, descricao: str, pontos_ataque: int):
        self.nome = nome
        self.descricao = descricao
        self.pontos_ataque = pontos_ataque

    @abstractmethod
    def usar(self):  # Metodo que simula uzar a Habilidade
        pass

    @abstractmethod
    def __str__(self):
        pass

#  -================================================================================================================================================-  #

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
        if len(self.inventario) > 0:
            if D2().jogar() == 2:
                if self.inventario[0] == "Cura":
                    self.usar_habilidade(self)
                    return (f"O Personagem {self.nome} se Curou")
                else:
                    self.usar_habilidade(alvo)
                    return (f"O Personagem {self.nome} se Curou")
        else:
            ataque_total = self.dado_de_ataque.jogar()
            alvo.pontos_vida -= ataque_total
            return ataque_total

    def usar_habilidade(self, alvo):
        ataque = self.inventario[0].usar(alvo)
        self.inventario.pop(0)
        return ataque

    def __eq__(self, personagem_2):
        return self.nome_personagem == personagem_2.nome_personagem and self.classe == personagem_2.classe
    
    def __str__(self):
        return (f"Nome: {self.nome_personagem} | Classe: {self.classe} | Inventario: {self.ver_inventario()}")
    
    def __repr__(self):
        return (f"Nome: {self.nome_personagem} | Classe: {self.classe} | Inventario: {self.ver_inventario()}")
    
    def ver_inventario(self):
        return ', '.join(str(habilidade) for habilidade in self.inventario)

#  -================================================================================================================================================-  #