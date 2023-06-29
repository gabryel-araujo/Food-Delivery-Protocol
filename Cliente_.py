#Criação da classe cliente para cadastro de dados

class Cliente:
    def __init__(self):
        self.__nome = None
        self.__telefone = None
        self.__cep = None
        self.__pagamento = None
        self.__troco = None

    def getNome(self):
        return self.__nome
    
    def getTelefone(self):
        return self.__telefone

    def getCep(self):
        return self.__pagamento

    def getPagamento(self):
        return self.__pagamento
    
    def getTroco(self):
        return self.__troco    
    
    def setNome(self, novoNome):
        self.__nome = novoNome

    def setTelefone(self, novoTelefone):
        self.__telefone = novoTelefone

    def setCep(self, novoCep):
        self.__cep = novoCep

    def setPagamento(self, formaPagamento):
        if formaPagamento == '1':
            self.__pagamento = 'Cartão'
        elif formaPagamento == '2':
            self.__pagamento = 'Dinheiro'

    def setTroco(self, troco):
        self.__troco = troco

    def __str__(self):
        return f'Nome: {self.__nome} | Telefone: {self.__telefone} | CEP: {self.__cep} | {self.__pagamento} | Troco: {self.__troco}'