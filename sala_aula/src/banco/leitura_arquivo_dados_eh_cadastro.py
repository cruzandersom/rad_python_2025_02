from leitura_arquivos import *

arquivo_csv = ler_arquivo_csv('cadastro.csv')

for linha in arquivo_csv:
    print(linha)


arquivo_txt = ler_arquivo_csv('dados.csv')
for linha in arquivo_txt:
    print(linha)