import os
from Lista_Encadeada import*
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
        # print("===CARDÁPIO===\n")
        # for item in cardapio:
        #     print(f'{item} - {cardapio[item][0]}: R$ {cardapio[item][1]:.2f}')
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
    print("1 - Cartão (pagamento na entrega)\n2 - Dinheiro")
    pagamento = input("Opção: ")
    lista.inserir(1, nome)
    lista.inserir(2, telefone)
    if pagamento == '2':
        lista.inserir(3,'Dinheiro')
        print("Vai ser necessário troco?(S/N)")
        troco = input().lower()
        if troco == 's':
            valor = float(input("Informar o valor do troco: "))   
            lista.inserir(4, valor)
        else:
            lista.inserir(4,'No')
    else:
        lista.inserir(3,'Cartão')         
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