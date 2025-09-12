
# Definindo a classe Cliente com
# atributos Nome, CPF, Idade,
# Profissao e Endereco
# Objeto não foi instanciado ainda não está em memória


class Cliente:
    Nome: str
    CPF: str
    Idade: int
    Profissao: str
    Endereco: str


cpf : str = "4.789-00"



# Instanciando o objeto Cliente
# Colocando o objeto em memória

cliente = Cliente()
cliente.Nome = "Anderson Cruz"
cliente.CPF = "123.456.789-00"
cliente.Idade = 30
cliente.Profissao = "Desenvolvedor"
cliente.Endereco = "Rua A, 123, Cidade B"
print(cliente.Nome)