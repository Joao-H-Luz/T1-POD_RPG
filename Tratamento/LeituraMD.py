# Importat Bibiotecas
from RPG import Personagem, Classe, Habilidade

# Converter o Arquivo "Ficha.md" em Personagens
# - Abre | faz a Leitura | Salva o conteudo em conteudo | Fecha o arquivo
with open("Ficha.md", 'r') as fold:
    conteudo = fold.readlines()

# Funções de Tratamento
# - Trata a entrada da lista pro Looping
def tratamento(string: str):
    return string.strip()

# - Trata a saida da lista e transforma em Objeto
def tratamento_de_personagens(lista: list):
    personagem = Personagem(lista[0], lista[1], lista[3:],)
    personagens_criados.append(personagem)

# Listas de Manipulação
conteudo_tratado = list(map(tratamento, conteudo))
dados = []
personagens = []
personagens_criados = []

# Looping para percorrer o arquivo e retirar os dados
for linhas in conteudo_tratado[2:]:
    if "###" in linhas:
        tipo_nome = linhas[4:]
        dados.append(tipo_nome)

    elif "**Classe**" in linhas:
        tipo_class = linhas[14:]
        dados.append(tipo_class)

    elif "-" in linhas:
        tipo_habilidade = linhas[2:]
        dados.append(tipo_habilidade)

    elif linhas == "":
        personagens.append(dados[:])
        dados.clear()

personagens.append(dados[:])
