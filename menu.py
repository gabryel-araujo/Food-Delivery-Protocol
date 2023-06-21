import os
from listaEncadeada import Lista, ValorInexistenteException

def showMenu():
    escolha = ''
    os.system('cls')
    print("===Menu===")
    print("1 - Mostrar cardápio")
    print("2 - Abrir carrinho")
    print("3 - Finalizar Pedido")
    print("X - Sair")
    escolha = input("Escolha uma opção: ").lower()
    return escolha


def Escolha_Cardapio(lista):
    escolha = ''
    os.system('cls')
    print("===Cardápio===")
    print("1 - Pepperoni")
    print("2 - Frango com catupiry")
    print("3 - Calabresa")
    print("4 - Quatro queijos")
    print("5 - À moda da casa")
    escolha = input("Escolha uma opção: ").lower()
    if escolha == "1":
        lista.inserir(1, "Pepperonni")
    elif escolha == "2":
        lista.inserir(1, "Frango com catupiry")
    elif escolha == "3":
        lista.inserir(1, "Calabresa")
    elif escolha == "4":
        lista.inserir(1, "Quatro queijos")
    elif escolha == "5":
        lista.inserir(1, "À moda da casa")
    return lista.__str__()

def carrinho_pedidos(lista):
    os.system('cls')
    print("===Carrinho===\n")
    print(lista)
    print("\n1 - Remover item")
    print("2 - Adicionar item")
    
    escolha = input ("Escolha uma opção: ").lower()
    if escolha == '1':
        item = input('Insira o sabor: ')
        if lista.busca(item) :
            lista.remover(lista.busca(item))
            print (lista)
            carrinho_pedidos(lista)
    elif escolha == '2':
        return
        # except:
        #     raise ValorInexistenteException (f'0 sabor {item} não está no seu carrinho')
# TEMP MENU, TEMP CARDAPIO, TEMP CARRINHO