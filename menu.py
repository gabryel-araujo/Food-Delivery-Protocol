import os
from listaEncadeada import Lista, ValorInexistenteException
from cardapio import cardapio

carrinho = Lista()
total = 0


def showMenu():
    limpaTerminal()
    escolha = ''
    print("===Menu===")
    print("1 - Mostrar cardápio")
    print("2 - Abrir carrinho")
    print("3 - Finalizar Pedido")
    print("X - Sair")
    escolha = input("Escolha uma opção: ").lower()
    return escolha


def Escolha_Cardapio(lista):
    confirmacao = ''
    while True:
        limpaTerminal()
        escolha = ''
        global total
        print("===CARDÁPIO===\n")
        for item in cardapio:
            print(f'{item} - {cardapio[item][0]}: R$ {cardapio[item][1]:.2f}')
        escolha = input("\nEscolha uma opção: ").lower()
        if escolha in cardapio.keys():
            lista.inserir(1, cardapio[escolha][0])
            total += cardapio[escolha][1]
        print("\nCarrinho: ", lista)
        print(f'Total: {total:.2f}')
        print("\nDeseja continuar comprando? (S/N)")
        confirmacao = input('Opção: ').lower()    
        if confirmacao == 'n':
            return lista.__str__()
    

def pagamento(lista):
    global total
    limpaTerminal()
    print("Para finalizar, preencha os campos abaixo:")
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    print("\nForma de pagamento:")
    pagamento = input("1 - Cartão (pagamento na entrega) 2 - Dinheiro")
    lista.inserir(1, nome)
    lista.inserir(2, telefone)
    if pagamento == '2':
        print("Informe o valor em cédulas a ser pago para providenciarmos o troco: ")
        valor = input("")
        print(f'Seu troco será de R$ {valor-total:.2f}')
    return lista.__str__()

def carrinho_pedidos(lista):
    limpaTerminal()
    global total
    print("===Carrinho===\n")
    print(lista)
    print(f'Total: {total:.2f}')
    print("\n1 - Remover item")
    print("2 - Adicionar item")
    print("3 - Voltar")
    
    escolha = input ("\nEscolha uma opção: ").lower()
    if escolha == '1':
        item = input('Insira o sabor: ')
        if lista.busca(item) :
            lista.remover(lista.busca(item))
            #total -= cardapio (SUBTRAIR DO VALOR TOTAL QUANDO REMOVER UM ITEM!)
            print (lista)
            carrinho_pedidos(lista)
    elif escolha == '2':
        Escolha_Cardapio(lista)
        return
    else:
        return
        # except:
        #     raise ValorInexistenteException (f'0 sabor {item} não está no seu carrinho')
# TEMP MENU, TEMP CARDAPIO, TEMP CARRINHO

def limpaTerminal():
    os.system('cls')
    os.system('clear')