# Bibliotecas Utilizadas
from RPG import *

# Converter o Arquivo "Ficha.md" em Personagens
#  -================================================================================================================================================-  #

# - Abre | faz a Leitura | Salva o "Conteudo do Arquivo" em conteudo | Fecha o arquivo

def leitura_de_arquivo():
    with open("Ficha.md", 'r') as fold:
        conteudo = fold.readlines()
    return conteudo

#  -================================================================================================================================================-  #

# Looping para percorrer o arquivo e retirar os dados

def linha_de_tratamento(conteudo_tratado):
    dados = []                              # Lista de Dados Auxiliar
    personagens = []                        # Lista de Dados Tratados

    # Faz um looping em todas as Linhas do Arquivo, pulando as duas primeiras (Titulo e linha vazia)
    for linhas in conteudo_tratado[2:]:
        if "###" in linhas:                 # Se tiver "###" significa que é um Nome
            # Trata a linha para retirar o exesso
            tipo_nome = linhas[4:]
            dados.append(tipo_nome)         # Adiciona o Nome na Lista dados

        elif "**Classe**" in linhas:        # Se tiver "**Classe**" significa que é uma Classe
            # Trata a linha para retirar o exesso
            tipo_class = linhas[14:]
            dados.append(tipo_class)        # Adiciona a Classe na Lista dados

        elif "**Habilidades**" in linhas:
            pass

        elif "-" in linhas:                 # Se tiver "-" significa que é uma Habilidade
            # Trata a linha para retirar o exesso
            tipo_habilidade = linhas[2:]
            # Adiciona a Habilidade na Lista dados
            dados.append(tipo_habilidade)

        elif linhas == "":                  # Se tiver "" significa que é uma linha vazia | Significa o Sinal de parada para o primeiro grupo de Dados
            # Adiciona uma copia de dados em personagem
            personagens.append(dados[:])
            dados.clear()                   # Limpa a Lista de Dados

    # Adiciona o ultimo grupo de dados na lista personagens
    personagens.append(dados[:])
    dados.clear()                           # Limpa a Lista de Dados

    print("Dados processados do arquivo:")
    for i, p in enumerate(personagens):
        print(f"{i+1}. {p}")

    return personagens

#  -================================================================================================================================================-  #

# - Trata a saida da lista e transforma em Objeto

def tratamento_de_personagens(lista: list):
    # Nome do Personagem
    nome = lista[0]               # Nome do Personagem

# Cria Instancias de Classe
    if "Guerreiro" == lista[1]:   # Classe do Personagem
        classe = Guerreiro()
        # Se for "Guerreiro" tamanho de 2 Habilidades no máximo
        habilidade = lista[2:5]
    elif "Mago" == lista[1]:
        classe = Mago()           # Se for "Mago" tamanho de 5 Habilidades no máximo
        habilidade = lista[2:8]
    elif "Ladino" == lista[1]:
        classe = Ladino()
        # Se for "Ladino" tamanho de 5 Habilidades no máximo
        habilidade = lista[2:6]
    else:
        raise ValueError(f"Classe inválida: {lista[1]}")

# Tratamento do inventario (Instanciar as Habilidades)
    inventario = []               # Inventario

    for hab in habilidade:
        if hab == "BolaDeFogo":
            inventario.append(BolaDeFogo())
        elif hab == "Cura":
            inventario.append(Cura())
        elif hab == "Tiro de Arco":
            inventario.append(TiroDeArco())
        else:
            print(f"Habilidade desconhecida: {hab}")
        # com mais elif colocar mais habilidades

# Criar Personagem
    return Personagem(nome, classe, inventario)

#  -================================================================================================================================================-  #


def chamada_de_ordem():
    # Ler o Arquivo "Ficha.md"
    conteudo = leitura_de_arquivo()
    if not conteudo:
        print("Nenhum conteúdo lido do arquivo. Encerrando.")
        return []
    # Tratar as String da lista
    linhas = list(map(lambda x: x.strip(), conteudo))
    # Fazer o looping em todas as Linhas
    dados_personagens = linha_de_tratamento(linhas)
    # Tratar os Personagens
    personagens = list(map(tratamento_de_personagens, dados_personagens))

    return personagens
#  -================================================================================================================================================-  #