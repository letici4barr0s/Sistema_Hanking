def exibir_ranking(jogadores):
    print("\n===== RANKING =====")
    for i, (nome, nivel, pontuacao) in enumerate(jogadores, start=1):
        if i == 1:
            destaque = "🥇"
        elif i == 2:
            destaque = "🥈"
        elif i == 3:
            destaque = "🥉"
        else:
            destaque = "-"
        print(f"{destaque} {i}º | {nome} | Nível {nivel} | Pontuação {pontuacao}")
