class Conta:

    def __init__(self,
                 cliente,
                 banco,
                 agencia,
                 conta,
                 saldo=10.00):
        self.cliente = cliente
        self.banco = banco
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    def __str__(self):
        return f"Conta(cliente={self.cliente}, banco={self.banco}, agencia={self.agencia}, conta={self.conta}, saldo={self.saldo})"

    def sacar(self, valor):
        if self.saldo < valor:
            print("Saldo insuficiente")
        else:
            self.saldo -= valor
            print(f"Saque de {valor} realizado com sucesso. Novo saldo: {self.saldo}")

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de {valor} realizado com sucesso. Novo saldo: {self.saldo}")

    def transferir(self, valor, conta_destino):
        if self.saldo < valor:
            print("Saldo insuficiente para transferência")
        else:
            self.saldo -= valor
            conta_destino.depositar(valor)
            print(
                f"Transferência de {valor} para {conta_destino.cliente} realizada com sucesso. Novo saldo: {self.saldo}")


conta_01 = Conta("Anderson Cruz", "Banco do Brasil", "0001", "12345-6", 1000.00)

conta_02 = Conta("Maria Silva", "Caixa Econômica", "0001", "98765-4", 500.00)

print(conta_01)
print(conta_02)

conta_01.transferir(200.00, conta_02)
print(conta_01)
print(conta_02)
