import os

def showMenu():
    print("===Menu===")
    print("1 - Mostrar cardápio")
    print("2 - Abrir carrinho")
    print("3 - Sair")

def cardapio(temp, pedido):
    os.system('clear')
    print("===Cardápio===")
    print("1 - Pepperoni")
    print("2 - Frango com catupiry")
    print("3 - Calabresa")
    print("4 - Quatro queijos")
    print("5 - À moda da casa")

    if temp == "1":
        pedido.inserir(1, "Pepperonni")
    elif temp == "2":
        pedido.inserir(1, "Frango com catupiry")
    elif temp == "3":
        pedido.inserir(1, "Calabresa")
    elif temp == "4":
        pedido.inserir(1, "Quatro queijos")
    elif temp == "5":
        pedido.inserir(1, "À moda da casa")

    mensagem = pedido.__str__()
    print("Carrinho: ", mensagem)
    print("\nPara continuar comprando digite: 1")
    print("Para fechar o pedido digite: 0")
    

# TEMP MENU, TEMP CARDAPIO, TEMP CARRINHO