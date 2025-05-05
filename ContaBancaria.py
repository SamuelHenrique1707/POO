class ContaBancaria:
    #Método inicializador (construtor)
    def __init__(self, titular, saldo_inicial=0, limite=1000):
        """
        Inicializa a conta bancária com o nome titular e um saldo inicial (0 por padrão)
        """
        self.__titular = titular # Nome do titular da conta
        self.__saldo = saldo_inicial # Saldo inicial da conta
        self.__limite = limite # Definição do atributo limite

    # Método para depositar dinheiro
    def depositar(self, valor):
        """
        Deposita um valor na conta. O valor deve ser positivo
        """
        if valor > 0:
            self.__saldo = self.__saldo + valor # saldo disponível incluindo o limite
            print(f"Depósito de R${valor} realizado com sucesso!")
        else:
            print("O valor do depósito deve ser positivo.")

    # Método para mostrar o saldo da conta
    def mostrar_saldo(self):
        """
        Exibe o saldo atual da conta.
        """
        print(f"Saldo atual da conta de {self.__titular}: R${self.__saldo}")

    def sacar(self, valor):
        """
        Saca o valor da conta. O valor deve ser positivo e não pode ultrapassar do saldo
        """
        if valor > 0:
            if self.__saldo + self.__limite >= valor:
                self.__saldo = self.__saldo - valor # saque disponível incluindo o limite
                print(f"Saque de R${valor} realizado com sucesso!")
            else:
                print(f"Saldo insuficiente!!!!")
        else:
            print("O valor do depósito deve ser positivo.")



conta1 = ContaBancaria("Sam", 500.00)
conta1.depositar(100)
conta1.sacar(1000)
conta1.mostrar_saldo()