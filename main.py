from RPG import *
from Tratamento import *


def main():
    lista_personagens = chamada_de_ordem()
    arena = Arena(lista_personagens)
    while True:
        print("\n--- MENU RPG ---")
        print("1. Combate entre dois personagens")
        print("2. Combate entre múltiplos personagens (Free For All)")
        print("3. Combate em ondas")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            while True:
                print("Escolha o primeiro personagem:")
                for i, p in enumerate(arena.lista_de_personagens):
                    print(f"{i+1}. {p.nome_personagem}")
                escolha1 = int(input("Digite o número: ")) - 1

                print("Escolha o segundo personagem:")
                for i, p in enumerate(arena.lista_de_personagens):
                    print(f"{i+1}. {p.nome_personagem}")
                escolha2 = int(input("Digite o número: ")) - 1

                if escolha1 == escolha2:
                    print(
                        "Você não pode escolher o mesmo personagem para os dois lados! Tente novamente.")
                elif not (0 <= escolha1 < len(arena.lista_de_personagens)) or not (0 <= escolha2 < len(arena.lista_de_personagens)):
                    print("Escolha inválida. Tente novamente.")
                else:
                    break

            arena.combate_1x1(arena.lista_de_personagens[escolha1], arena.lista_de_personagens[escolha2])

        elif opcao == "2":
            arena.combate_free_for_all()
            break
        
        elif opcao == "3":
            lista_selecionados = []
            print("Escolha 5 heróis para o combate em ondas:")

            while len(lista_selecionados) < 5:
                print("\nPersonagens disponíveis:")
                for i, p in enumerate(arena.lista_de_personagens):
                    if p not in lista_selecionados:
                        print(f"{i+1}. {p.nome_personagem}")

                try:
                    escolha = int(
                        input(f"Escolha o herói {len(lista_selecionados)+1}: ")) - 1
                except ValueError:
                    print("Digite um número válido.")
                    continue

                if not (0 <= escolha < len(arena.lista_de_personagens)):
                    print("Escolha inválida. Tente novamente.")
                elif arena.lista_de_personagens[escolha] in lista_selecionados:
                    print("Herói já selecionado, escolha outro.")
                else:
                    lista_selecionados.append(arena.lista_de_personagens[escolha])

            combate_onda(lista_selecionados)
            break

        elif opcao == "4":
            print("Saindo do sistema.")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
