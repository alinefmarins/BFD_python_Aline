# 2 - Suponha que estamos desenvolvendo um sistema para um banco. Este sistema deve obedecer as seguintes restrições:

# A - Uma classe pai chamada Cliente,

class Cliente:

# com os atributos: nome, cpf, endereço   

    def __init__(self, nome, cpf, endereco):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco

    # Métodos para consultar informações
    def consultar_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"Endereço: {self.endereco}")

    # Métodos para alterar informações
    def alterar_nome(self, novo_nome):
        self.nome = novo_nome

    def alterar_endereco(self, novo_endereco):
        self.endereco = novo_endereco


# B - Uma classe filha chamada Conta_Corrente 

class Conta_Corrente(Cliente):

# que deve herdar os atributos da classe pai mais o atributo "saldo". Este atributo deve ser privado.

    def __init__(self, nome, cpf, endereco, saldo=0.0):
        super().__init__(nome, cpf, endereco)
        self.__saldo = saldo  # atributo privado

# C - O sistema precisa ser capaz de: depositar, sacar, consultar saldo, consultar informações dos clientes e alterar informações dos clientes. 
    # Método para depositar
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R${valor} realizado com sucesso.")
        else:
            print("Valor de depósito inválido.")

    # Método para sacar
    def sacar(self, valor):
        if valor <= 0:
            print("Valor de saque inválido.")
        elif valor > self.__saldo:
            print("Saldo insuficiente para saque.")
        else:
            self.__saldo -= valor
            print(f"Saque de R${valor} realizado com sucesso.")

    # Método para consultar saldo
    def consultar_saldo(self):
        print(f"Saldo atual: R${self.__saldo}")

    # Método para exibir todas as informações da conta
    def exibir_dados_completos(self):
        self.consultar_informacoes()
        self.consultar_saldo()


# Crie ao menos 1 instância de Conta_Corrente, 

conta1 = Conta_Corrente("Aline Freitas", "123.456.789-00", "Rua Coutinho, 123", saldo=1000.0)

# execute todos os métodos para teste.
# Consultando informações e saldo
conta1.exibir_dados_completos()

# Realizando um depósito
conta1.depositar(500)

# Tentando depositar um valor inválido
conta1.depositar(-100)

# Consultando saldo após depósito
conta1.consultar_saldo()

# Realizando um saque
conta1.sacar(300)

# Tentando sacar mais do que o saldo
conta1.sacar(1500)

# Tentando sacar valor inválido
conta1.sacar(-50)

# Consultando saldo final
conta1.consultar_saldo()

# Alterando informações do cliente
conta1.alterar_nome("Aline Freitas Marins")
conta1.alterar_endereco("Rua Imãos Coutinho, Lt A, qd B")

# Exibindo dados atualizados
conta1.exibir_dados_completos()
