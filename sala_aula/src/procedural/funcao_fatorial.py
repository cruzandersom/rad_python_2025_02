# Função fatorial(n)
def fatorial(n):
    if n < 0:
        raise ValueError("Fatorial não é definido para números negativos")
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

# Teste da função
print(fatorial(5))  # 120


# fatorial usando recursão
def fatorial_recursivo(n):
    if n < 0:
        raise ValueError("Fatorial não é definido para números negativos")
    if n == 0 or n == 1:
        return 1
    return n * fatorial_recursivo(n - 1)


# Tabela de fatoriais: Mostre os fatoriais de 0 a 10, um por linha.
def tabela_de_fatoriais(inicio, fim):
    for i in range(inicio, fim + 1):
        print(f"{i}! = {fatorial(i)}")


# Exemplo de uso da tabela
tabela_de_fatoriais(0, 10)


# Verificação de entrada: Se o usuário digitar número negativo, exiba mensagem e peça novamente.
def solicitar_numero_positivo():
    while True:
        try:
            numero = int(input("Digite um número inteiro não negativo para calcular o fatorial: "))
            if numero < 0:
                print("Número inválido. Por favor, digite um número não negativo.")
            else:
                return numero
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")


# Exemplo de uso da solicitação
numero = solicitar_numero_positivo()
print(f"O fatorial de {numero} é {fatorial(numero)}")


# Combinatória simples: Calcule a quantidade de anagramas de uma palavra sem letras repetidas usando fatorial do tamanho (ex.: “casa” tem letras repetidas; use uma sem repetição como “amor”).
def anagramas(palavra):
    tamanho = len(palavra)
    return fatorial(tamanho)


# Exemplo de uso da função de anagramas
print(anagramas("amor"))  # 24 (4! = 24)
print(anagramas("python"))  # 720 (6! = 720)
print(anagramas("casa"))  # 24 (4! = 24, mas com letras repetidas o cálculo seria diferente)
print(anagramas("abcde"))  # 120 (5! = 120)
