# Bibliotecas Utilizadas
import traceback        # Biblioteca que auxilia a identificar onde e o que é o erro
import datetime

# Tratamento de erro
def log_erro(erro):
    time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    nome_arquivo = "log_de_erros.txt"
    with open(nome_arquivo, "a") as log:
        log.write(f"--- Erro em {time} ---\n")
        log.write(f"{str(erro)}\n")
        log.write(traceback.format_exc())
        log.write("\n\n")