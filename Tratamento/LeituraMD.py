# Converter o Arquivo "Ficha.md" em Personagens

with open("Ficha.md", 'r') as fold: # Abre | faz a Leitura | Salva o conteudo em conteudo | Fecha o arquivo
    conteudo = fold.readlines()


for i in conteudo:
    if "###" in i:
        pass
