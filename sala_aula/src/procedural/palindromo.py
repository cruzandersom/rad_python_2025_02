# função para verificar se um texto é um palindromo
def eh_palindromo(texto):
    texto = texto.replace(" ", "").lower()
    # Verifica se o texto é igual ao seu reverso
    return texto == texto[::-1]


# Teste da função

#  Ignorando espaços e maiúsculas: Teste frases como “Ame a ema” ou “Socorram-me, subi no ônibus em Marrocos” (dica: limpe espaços e letras maiúsculas).
def eh_palindromo_ignorando_espacos_e_maiusculas(texto):
    # Remove espaços e converte para minúsculas
    texto = ''.join(filter(str.isalnum, texto)).lower()
    # Verifica se o texto é igual ao seu reverso
    return texto == texto[::-1]


# Exemplos de uso
print(eh_palindromo("arara"))  # True
print(eh_palindromo("hello"))  # False
print(eh_palindromo_ignorando_espacos_e_maiusculas("Ame a ema"))  # True
print(eh_palindromo_ignorando_espacos_e_maiusculas("Socorram-me, subi no ônibus em Marrocos"))  # True


# Conjunto de testes: Dada uma lista de 5 palavras/frases, mostre um relatório: para cada item, “é palíndromo” ou “não é”.
def relatorio_palindromos(lista_textos):
    relatorio = {}
    for texto in lista_textos:
        if eh_palindromo_ignorando_espacos_e_maiusculas(texto):
            relatorio[texto] = "é palíndromo"
        else:
            relatorio[texto] = "não é"
    return relatorio


# Exemplo de uso do relatório
lista_de_testes = [
    "arara",
    "hello",
    "Ame a ema",
    "Socorram-me, subi no ônibus em Marrocos",
    "Python"
]
relatorio = relatorio_palindromos(lista_de_testes)
for texto, resultado in relatorio.items():
    print(f'"{texto}": {resultado}')


# Contador de palíndromos: Leia N palavras e conte quantas são palíndromos; exiba a porcentagem.
def contador_de_palindromos(lista_textos):
    total = len(lista_textos)
    if total == 0:
        return 0, 0.0
    contador = sum(1 for texto in lista_textos if eh_palindromo_ignorando_espacos_e_maiusculas(texto))
    porcentagem = (contador / total) * 100
    return contador, porcentagem


# Exemplo de uso do contador
contador, porcentagem = contador_de_palindromos(lista_de_testes)
print(f'Número de palíndromos: {contador}, Porcentagem: {porcentagem:.2f}%')
