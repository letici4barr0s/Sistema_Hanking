Sistema de Ranking de Jogadores

Descrição:

Pequeno sistema em Python que importa arquivos CSV com dados de jogadores, armazena-os em um banco SQLite e exibe um ranking via interface gráfica (Tkinter). O projeto destaca os 3 primeiros colocados.

Estrutura do projeto deve ser essa:
SISTEMAHANKING/
│-- jogadores1.csv
│-- jogadores2.csv
│-- jogadores3.csv
│-- main.py # interface gráfica (ponto de entrada)
│-- database.py
│-- utils.py
│-- ranking.py
│-- jogadores.db # criado automaticamente após a primeira importação
│-- erros.log # criado automaticamente se houver linhas inválidas
│-- README.md
