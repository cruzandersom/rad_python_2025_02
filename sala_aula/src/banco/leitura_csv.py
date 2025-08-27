# Leitura de arquivo CSV
import csv

with open('dados.csv', 'r') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)

    for linha in leitor_csv:
        print(linha)
        print(type(linha))