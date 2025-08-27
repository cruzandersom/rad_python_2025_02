# função que lê arquivo de texto e me retorna uma lista de linhas
def ler_arquivo_texto(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
    return [linha.strip() for linha in linhas]


# função que lê arquivo CSV e me retorna uma lista de listas (cada linha é uma lista)
def ler_arquivo_csv(caminho_arquivo):
    import csv
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv)
        return [linha for linha in leitor_csv]

# função que lê arquivo JSON e me retorna um dicionário ou lista (dependendo da estrutura do JSON)
def ler_arquivo_json(caminho_arquivo):
    import json
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo_json:
        return json.load(arquivo_json)


# função que lê arquivo XML e me retorna um elemento raiz (dependendo da estrutura do XML)
def ler_arquivo_xml(caminho_arquivo):
    import xml.etree.ElementTree as ET
    arvore = ET.parse(caminho_arquivo)
    return arvore.getroot()


# exemplo de uso:
if __name__ == "__main__":
    caminho_texto = 'meuarquivo.txt'
    caminho_csv = 'dados.csv'
    caminho_json = 'dados.json'
    caminho_xml = 'dados.xml'

    linhas_texto = ler_arquivo_texto(caminho_texto)
    print("Linhas do arquivo de texto:", linhas_texto)

    linhas_csv = ler_arquivo_csv(caminho_csv)
    print("Linhas do arquivo CSV:", linhas_csv)

    dados_json = ler_arquivo_json(caminho_json)
    print("Dados do arquivo JSON:", dados_json)

    raiz_xml = ler_arquivo_xml(caminho_xml)
    print("Elemento raiz do arquivo XML:", raiz_xml.tag)