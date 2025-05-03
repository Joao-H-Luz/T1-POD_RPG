# Bibliotecas Utilizadas
from Class import Classe, Habilidade, Dado

# SubClasses Obrigatórias:
# SubClass = Classe
class Guerreiro(Classe):
    def __init__(self, nome):
        super().__init__(nome,
                         pontos_vida=10 + (self.pontos_defesa * 5),
                         dado_de_ataque=D12,
                         pontos_ataque=6,
                         pontos_defesa=8,
                         limite_habilidades=2)
        
    def __str__(self):
        return "Classe: Guerreiro | " + super().__str__()
        

class Mago(Classe):
    def __init__(self, nome):
        super().__init__(nome,
                         pontos_vida=8 + (self.pontos_defesa * 2),
                         dado_de_ataque=D6,
                         pontos_ataque=10,
                         pontos_defesa=3,
                         limite_habilidades=5)
        
    def __str__(self):
        return "Classe: Mago | " + super().__str__()
    

class Ladino(Classe):
    def __init__(self, nome):
        super().__init__(nome,
                         pontos_vida=6 + (self.pontos_defesa * 3),
                         dado_de_ataque=D8,
                         pontos_ataque=8,
                         pontos_defesa=5,
                         limite_habilidades=3)
        
    def __str__(self):
        return "Classe: Ladino | " + super().__str__()


# SubClass = Habilidade
class BolaDeFogo(Habilidade):
    def __init__(self, nome=..., descricao=..., pontos_ataque=...):
        super().__init__(nome="Bola de Fogo",
                         descricao="Uma bola de fogo que causa dano em área.",
                         pontos_ataque=10)
                         
    def usar(self):
        return super().usar()
    

class Cura(Habilidade):
    def __init__(self, nome=..., descricao=..., pontos_ataque=...):
        super().__init__(nome="Cura de Vida",
                         descricao="Uma cura que recupera 10 pontos de vida.",
                         pontos_ataque=10)

    def usar(self):
        return super().usar()
        

class TiroDeArco(Habilidade):
    def __init__(self, nome=..., descricao=..., pontos_ataque=...):
        super().__init__(nome="Disparo com Arco",
                         descricao="Um tiro de arco que causa dano em área.",
                         pontos_ataque=6)

    def usar(self):
        return super().usar()


# SubClass = Dado
class D4(Dado):
    def __init__(self, lados=...):
        super().__init__(lados=4)

    def jogar(self):
        return super().jogar()
    

class D6(Dado):
    def __init__(self, lados=...):
        super().__init__(lados=6)

    def jogar(self):
        return super().jogar()
    

class D8(Dado):
    def __init__(self, lados=...):
        super().__init__(lados=8)

    def jogar(self):
        return super().jogar()
    

class D10(Dado):
    def __init__(self, lados=...):
        super().__init__(lados=10)

    def jogar(self):
        return super().jogar()
    

class D12(Dado):
    def __init__(self, lados=...):
        super().__init__(lados=12)

    def jogar(self):
        return super().jogar()
    

class D20(Dado):
    def __init__(self, lados=...):
        super().__init__(lados=20)

    def jogar(self):
        return super().jogar()