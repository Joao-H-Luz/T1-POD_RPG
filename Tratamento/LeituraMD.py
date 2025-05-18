# Bibliotecas Utilizadas
from RPG import Personagem, Guerreiro, Mago, Ladino, BolaDeFogo, Cura, TiroDeArco
from RPG import SubClass 

# Converter o Arquivo "Ficha.md" em Personagens
#  -================================================================================================================================================-  #

# - Abre | faz a Leitura | Salva o "Conteudo do Arquivo" em conteudo | Fecha o arquivo

def leitura_de_arquivo():
    try:
        with open("Ficha.md", 'r') as fold:
            conteudo = fold.readlines()
        return conteudo
    except FileNotFoundError:
        print("Erro: O arquivo 'Ficha.md' não foi encontrado.")
        return []

#  -================================================================================================================================================-  #

# Looping para percorrer o arquivo e retirar os dados

def linha_de_tratamento(conteudo_tratado):
    dados = []                              # Lista de Dados Auxiliar
    personagens = []                        # Lista de Dados Tratados

    # Faz um looping em todas as Linhas do Arquivo, pulando as duas primeiras (Titulo e linha vazia)
    for linhas in conteudo_tratado[2:]:
        try:
            if "###" in linhas:                 # Se tiver "###" significa que é um Nome
                # Trata a linha para retirar o exesso
                tipo_nome = linhas[4:]
                dados.append(tipo_nome)         # Adiciona o Nome na Lista dados

            elif "**Classe**" in linhas:        # Se tiver "**Classe**" significa que é uma Classe
                # Trata a linha para retirar o exesso
                tipo_class = linhas[14:]
                dados.append(tipo_class)        # Adiciona a Classe na Lista dados

            elif "-" in linhas:                 # Se tiver "-" significa que é uma Habilidade
                # Trata a linha para retirar o exesso
                tipo_habilidade = linhas[2:]
                # Adiciona a Habilidade na Lista dados
                dados.append(tipo_habilidade)

            elif linhas == "":                  # Se tiver "" significa que é uma linha vazia | Significa o Sinal de parada para o primeiro grupo de Dados
                # Adiciona uma copia de dados em personagem
                personagens.append(dados[:])
                dados.clear()                   # Limpa a Lista de Dados

        except Exception as e:
            print(f"Erro ao processar a linha: {linhas}\n{e}")

    # Adiciona o ultimo grupo de dados na lista personagens
    personagens.append(dados[:])
    dados.clear()                           # Limpa a Lista de Dados

    return personagens

#  -================================================================================================================================================-  #

# - Trata a saida da lista e transforma em Objeto

def tratamento_de_personagens(lista: list):
    try:
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
            pass                      # Tratamento de erro | Classe desconhecida

# Tratamento do inventario (Instanciar as Habilidades)
        inventario = []               # Inventario

        for hab in habilidade:
            if "BolaDeFogo" in hab:
                inventario.append(BolaDeFogo())
            if "Cura" in hab:
                inventario.append(Cura())
            if "Tiro de Arco" in hab:
                inventario.append(TiroDeArco())
            # com mais elif colocar mais habilidades

# Criar Personagem
        return Personagem(nome, classe, inventario)
    
    except IndexError:
        print(f"Erro: Lista incompleta para personagem: {lista}")
    except Exception as e:
        print(f"Erro ao criar personagem com dados {lista}: {e}")

#  -================================================================================================================================================-  #


def chamada_de_ordem():
    # Ler o Arquivo "Ficha.md"
    conteudo = leitura_de_arquivo()
    if not conteudo:
        print("Nenhum conteúdo lido do arquivo. Encerrando.")
        return []
    try:
        # Tratar as String da lista
        linhas = list(map(lambda x: x.strip(), conteudo))
        # Fazer o looping em todas as Linhas
        dados_personagens = linha_de_tratamento(linhas)
        # Tratar os Personagens
        personagens = list(map(tratamento_de_personagens, dados_personagens))

        return personagens
    
    except Exception as e:
        print(f"Erro inesperado ao processar personagens: {e}")
        return []

#  -================================================================================================================================================-  #