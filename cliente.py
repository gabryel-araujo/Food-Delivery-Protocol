import socket
import sys
import os
import platform
from Lista_Encadeada import *
from menu import *
from Cliente_Class import Cliente

carrinho = Lista()
HOST = '0.0.0.0'
PORTA = 41800
mensagem = 0
cmd_client = ['MENU', 'SEND', 'REMOVE', 'QUIT']  # MÉTODOS DO PROTOCOLO.
cmd_MENU = ['SHOW', 'CHOOSE']  # Dentro do método MENU temos o SHOW e CHOOSE.
req = ''
resp = ''
v_total = 0
cardapio = ""


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


def Escolhe_pedido(lista, cardapio):
    global v_total
    while True:
        limpaTerminal()
        # Adicionando o SHOW na requisição.
        if cardapio == '':
            req = f'{cmd_client[0]}/{cmd_MENU[0]}'
            sock.send(str.encode(req))
            resp = sock.recv(1024)
            resp = resp.decode()
            # Dividindo o método do protocolo do conteúdo da mensagem.
            resp = resp.split('/')
            print(type(resp))
            cardapio = resp[1]
        print(cardapio)
        cardapio = cardapio.split('\n')
        print(cardapio)
        escolha = input("\nEscolha uma opção: ").lower()

        #if resp[0] == 'SENT_MENU':
            # Armazena a opção do cardápio escolhida pelo cliente.
                # Enviando o método CHOOSE e a opção escolhida do cardápio na requisição.
            # req = f'{cmd_client[0]}/{cmd_MENU[1]}/{escolha}'
            # sock.send(str.encode(req))
            # resp = sock.recv(1024)
            # resp = resp.decode()
            # # Dividindo o método do protocolo do conteúdo da mensagem.
            # resp = resp.split('/')

        if resp[0] == 'ADD_ITEM':
            pedido = resp[1]
            v_total += float(resp[2])
            lista.inserir(1, pedido)
            print("\nCarrinho: ", lista)
            print(f'Total: {v_total:.2f}')
            print("\nDeseja continuar comprando? (S/N)")
            confirmacao = input('Opção: ').lower()

            if confirmacao == 'n':
                return
        else:
            print("\nOpção inválida. Tente novamente.")
            input("\nPressione ENTER para continuar...")


def carrinho_pedidos(lista):
    limpaTerminal()
    global v_total
    print("===Carrinho===\n")
    print(lista)
    print(f'Total: {v_total:.2f}')
    print("\n1 - Remover item")
    print("2 - Adicionar item")
    print("3 - Voltar")

    escolha = input("\nEscolha uma opção: ").lower()
    if escolha == '1':
        item = input(
            'Insira o nome do item ou sua posição no carrinho: ').capitalize()
        try:
            if lista.busca(item):
                lista.remover(lista.busca(item))
                req = f'{cmd_client[2]}/{item}'
            else:
                rmv = lista.elemento(int(item))
                lista.remover(int(item))
                req = f'{cmd_client[2]}/{rmv}'
            sock.send(str.encode(req))
            resp = sock.recv(1024)
            resp = resp.decode()
            # Dividindo o método do protocolo do conteúdo da mensagem.
            resp = resp.split('/')
            if resp[0] == 'VALOR':
                v_total -= float(resp[1])
                print(lista)
                carrinho_pedidos(lista)
        except ListaException as le:
            print(le)
            carrinho_pedidos(lista)
    elif escolha == '2':
        Escolhe_pedido(lista)
    else:
        return


def dados_pagamento():
    limpaTerminal()
    global v_total
    cliente = Cliente()
    print("Para finalizar, preencha os campos abaixo:")
    cliente.setNome(input("Nome: "))
    cliente.setTelefone(input("Telefone: "))
    cliente.setCep(input("Cep: "))
    print("\nForma de pagamento:")
    print("1 - Cartão (pagamento na entrega)\n2 - Dinheiro")
    cliente.setPagamento(input("Opção: "))
    if cliente.getPagamento() == 'Dinheiro':
        print("Vai ser necessário troco?(S/N)")
        troco = input().lower()
        if troco == 's':
            valor = float(input("Informar o valor do troco: "))
            cliente.setTroco(valor)
    return cliente


def limpaTerminal():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


if len(sys.argv) > 1:
    HOST = sys.argv[1]

servidor = (HOST, PORTA)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.connect(servidor)
except ConnectionRefusedError as cre:
    print("A pizzaria se encontra fechada")
    sys.exit()

while True:
    menu = showMenu()
    if menu == "1":
        Escolhe_pedido(carrinho, cardapio)

    elif menu == "2":
        carrinho_pedidos(carrinho)

    elif menu == "3":
        if len(carrinho) != 0:
            dados = dados_pagamento()
            req = f'{cmd_client[1]}/{carrinho}/{dados}'
            sock.send(str.encode(req))
            input('\nPressione ENTER para voltar ao MENU...')
            carrinho.esvaziar()

        else:
            limpaTerminal()
            print("\nSeu carrinho está vazio! Adicione algo para fazer seu pedido!")
            input("\nPressione ENTER para ir ao cardápio...")
            Escolhe_pedido(carrinho)

    elif menu == 'x':
        req = cmd_client[2]
        sock.send(str.encode(req))
        req = sock.recv(1024)
        print(req.decode())
        break

sock.close()
