# 🧙‍♂️ RPG de Batalha em Python

Este projeto é um jogo de RPG baseado em turnos, feito em Python, que permite combates entre personagens personalizados em diferentes modos: **1x1**, **Free For All** e **Combate em Ondas**.

---

## 🛠️ Tecnologias utilizadas

- Python 3
- Módulos próprios:
  - `RPG.py`
  - `Tratamento.py`

---

## 🎮 Modos de Jogo

Ao executar o programa `main.py`, um **menu interativo** será exibido no terminal com as seguintes opções:

### 1. Combate entre dois personagens
Permite que o jogador escolha **dois personagens** da lista para lutarem entre si. O combate ocorre em turnos e termina quando um dos personagens perde todos os pontos de vida.

### 2. Combate múltiplo (Free For All)
Todos os personagens da lista se enfrentam em um confronto sem alianças. O último sobrevivente é declarado o vencedor.

### 3. Combate em ondas
Você escolhe **5 heróis** para enfrentar **inimigos em várias rodadas** (10 no total). A dificuldade aumenta a cada onda. Nas ondas 5 e 10, você enfrentará **chefes especiais** (bosses).

> ⚠️ Nas rodadas com bosses (5 e 10), **não aparecem inimigos comuns**, apenas o chefe da rodada.

### 4. Sair
Encerra o programa.

---

## 📦 Estrutura dos Arquivos

- `main.py` — Exibe o menu e gerencia as escolhas do jogador.
- `RPG.py` — Contém as classes dos personagens, arena de combate e lógica principal do jogo.
- `Tratamento.py` — Lida com entrada e validação de dados do usuário.
- `Dado.py`, `Habilidade.py`, `Classe.py` — arquivos auxiliares que simulam rolagem de dados e habilidades especiais.
- `logs/` — pasta (opcional) onde o jogo pode registrar eventos de combate.

---

## 🚀 Como rodar o jogo

1. Certifique-se de ter o **Python 3** instalado.
2. Baixe ou clone este repositório.
3. Certifique-se de que os arquivos `RPG.py`, `Tratamento.py` e `main.py` estejam na mesma pasta.
4. Execute o seguinte comando no terminal:

```bash
python main.py
```

5. Escolha uma das opções do menu para jogar.

---

## 🧑‍💻 Criadores

- João Henrique da Luz  
- Frederico

---

🎲 **Boa sorte nos combates! Que os dados rolem a seu favor!**
