# Bibliotecas Utilizadas
from RPG.Class import Classe, Habilidade, Dado
from random import randint

# SubClasses Obrigatórias:
#  -================================================================================================================================================-  #

# SubClass || Classe
class Guerreiro(Classe):
    def __init__(self):
        super().__init__(classe="Guerreiro",
                         pontos_vida=50,
                         dado_de_ataque=D12(),
                         pontos_ataque=6,
                         pontos_defesa=8,
                         limite_habilidades=2)
        
    def __repr__(self):
        return (f"Classe: {self.classe} | Ataque: {self.pontos_ataque} | Defesa: {self.pontos_defesa} | Tipo de Dado: {self.dado_de_ataque}")
    
#  -================================================================================================================================================-  #

class Mago(Classe):
    def __init__(self):
        super().__init__(classe="Mago",
                         pontos_vida=14,
                         dado_de_ataque=D6(),
                         pontos_ataque=10,
                         pontos_defesa=3,
                         limite_habilidades=5)
        
    def __repr__(self):
        return (f"Classe: {self.classe} | Ataque: {self.pontos_ataque} | Defesa: {self.pontos_defesa} | Tipo de Dado: {self.dado_de_ataque}")
    
#  -================================================================================================================================================-  #

class Ladino(Classe):
    def __init__(self):
        super().__init__(classe="Ladino",
                         pontos_vida=21,
                         dado_de_ataque=D8(),
                         pontos_ataque=8,
                         pontos_defesa=5,
                         limite_habilidades=3)
        
    def __repr__(self):
        return (f"Classe: {self.classe} | Ataque: {self.pontos_ataque} | Defesa: {self.pontos_defesa} | Tipo de Dado: {self.dado_de_ataque}")

#  -================================================================================================================================================-  #

class Bardo(Classe):
    def __init__(self):
        super().__init__(classe="Bardo",
                         pontos_vida=5 + (self.pontos_defesa * 2),
                         dado_de_ataque=D10(),
                         pontos_ataque=5,
                         pontos_defesa=5,
                         limite_habilidades=5)

    def __repr__(self):
        return (f"Classe: {self.classe} | Ataque: {self.pontos_ataque} | Defesa: {self.pontos_defesa} | Tipo de Dado: {self.dado_de_ataque}")

    def labia(self):
        pass

    def moral(self):
        pass

#  -================================================================================================================================================-  #

# SubClass || Habilidade

class BolaDeFogo(Habilidade):
    def __init__(self):
        super().__init__(nome="Bola de Fogo",
                         descricao="Uma bola de fogo que causa dano em área.",
                         pontos_ataque=10)
                         
    def usar(self, alvo):       # Fazer um Metodo que simula uzar a Habilidade
        alvo.pontos_vida -= self.pontos_ataque
        return self.pontos_ataque
    
    def __str__(self):
        return (f"{self.nome}")
    
    def __repr__(self):
        return (f"{self.nome} | {self.descricao} | Causa {self.pontos_ataque} de Dano")
    
#  -===============================================-  #

class Cura(Habilidade):
    def __init__(self):
        super().__init__(nome="Cura",
                         descricao="Uma cura que recupera vida.",
                         pontos_ataque=10)

    def usar(self, alvo):       # Fazer um Metodo que simula uzar a Habilidade
        alvo.pontos_vida += self.pontos_ataque  # Cura O personagem
        return self.pontos_ataque
        
    def __str__(self):
        return (f"{self.nome}")

    def __repr__(self):
        return (f"{self.nome} | {self.descricao} | Causa {self.pontos_ataque} de Dano")
    
#  -===============================================-  #

class TiroDeArco(Habilidade):
    def __init__(self):
        super().__init__(nome="Disparo com Arco",
                         descricao="Um tiro de precisão com Arco!",
                         pontos_ataque=6)

    def usar(self, alvo):       # Fazer um Metodo que simula uzar a Habilidade
        alvo.pontos_vida -= self.pontos_ataque
        return self.pontos_ataque

    def __str__(self):
        return (f"{self.nome}")

    def __repr__(self):
        return (f"{self.nome} | {self.descricao} | Causa {self.pontos_ataque} de Dano")
    
#  -===============================================-  #

class AumentoMoral(Habilidade):
    def __init__(self):
        super().__init__(nome="Musica de Batalha",
                         descricao="O bardo começa a tocar 'Black Sabbath' no meio da batalha.",
                         pontos_ataque=10)

    def usar(self, alvo):          # Fazer um Metodo que simula uzar a Habilidade
        alvo.pontos_vida += self.pontos_ataque
        return self.pontos_ataque

    def __str__(self):
        return (f"{self.nome} | {self.descricao} | Causa {self.pontos_ataque} de Dano")

#  -================================================================================================================================================-  #

# SubClass || Dado

# -- DADO de 4 Lados --

class D4(Dado):
    def __init__(self):
        super().__init__(lados=4)

    def jogar(self):                # Metodo que Simula jogar o Dado
        numero_do_dado = randint(1, self.lados)
        return numero_do_dado
    
    def __repr__(self):             # Metodo de Representação da Classe
        return (f"{self.lados} Lados")

#  -===============================================-  #

# -- DADO de 6 Lados --

class D6(Dado):
    def __init__(self):
        super().__init__(lados=6)

    def jogar(self):                # Metodo que Simula jogar o Dado
        numero_do_dado = randint(1, self.lados)
        return numero_do_dado
    
    def __repr__(self):             # Metodo de Representação da Classe
        return (f"{self.lados} Lados")

#  -===============================================-  #

# -- DADO de 8 Lados --

class D8(Dado):
    def __init__(self):
        super().__init__(lados=8)

    def jogar(self):                # Metodo que Simula jogar o Dado
        numero_do_dado = randint(1, self.lados)
        return numero_do_dado
    
    def __repr__(self):             # Metodo de Representação da Classe
        return (f"{self.lados} Lados")

#  -===============================================-  #

# -- DADO de 10 Lados --

class D10(Dado):
    def __init__(self):
        super().__init__(lados=10)

    def jogar(self):                # Metodo que Simula jogar o Dado
        numero_do_dado = randint(1, self.lados)
        return numero_do_dado
    
    def __repr__(self):             # Metodo de Representação da Classe
        return (f"{self.lados} Lados")
    
#  -===============================================-  #

# -- DADO de 12 Lados --

class D12(Dado):
    def __init__(self):
        super().__init__(lados=12)

    def jogar(self):                # Metodo que Simula jogar o Dado
        numero_do_dado = randint(1, self.lados)
        return numero_do_dado
    
    def __repr__(self):             # Metodo de Representação da Classe
        return (f"{self.lados} Lados")
    
#  -===============================================-  #

# -- DADO de 20 Lados --
# Dado Padrão de Ataque

class D20(Dado):
    def __init__(self):
        super().__init__(lados=20)

    def jogar(self):                # Metodo que Simula jogar o Dado
        numero_do_dado = randint(1, self.lados)
        return numero_do_dado
    
    def __repr__(self):             # Metodo de Representação da Classe
        return (f"{self.lados} Lados")

#  -===============================================-  #

# -- DADO de 2 Lados (Habilidade) --

class D2(Dado):
    def __init__(self):
        super().__init__(lados=2)

    def jogar(self):                # Metodo que Simula jogar o Dado
        numero_do_dado = randint(1, self.lados)
        return numero_do_dado

#  -================================================================================================================================================-  #