import csv
from database import inserir_jogador

def importar_csv(arquivo_csv, lista_id):
    with open(arquivo_csv, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)  # pula cabeçalho
        for linha in reader:
            try:
                nome, nivel, pontuacao = linha
                inserir_jogador(nome, int(nivel), float(pontuacao), lista_id)
            except Exception as e:
                with open("erros.log", "a", encoding="utf-8") as log:
                    log.write(f"Erro na linha {linha}: {str(e)}\n")
