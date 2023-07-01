import socket
import sys
import os
import platform
from Lista_Encadeada import *
from menu import *
from Cliente_Class import Cliente

carrinho = Lista()
HOST = '127.0.0.1'
PORTA = 41800
cmd_client = ['GET_MENU', 'SEND', 'QUIT']  # MÉTODOS DO PROTOCOLO.
req = ''
resp = ''
v_total = 0
cardapio =''


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


def fazPedido(lista):
    global v_total
    global cardapio
    while True:
        limpaTerminal()
        if cardapio == '': #Caso o cliente ainda não tenha recebido o cardápio, realiza a requisição.
            req = f'{cmd_client[0]}/\n' 
            sock.send(str.encode(req)) #Envia o método na requisição.
            resp = sock.recv(1024)
            resp = resp.decode()
            resp = resp.split('/') #Separando a mensagem do protocolo do conteúdo.
            if resp[0] == 'SENT_MENU':
                cardapio = resp[1] #Adiciona em uma variável apenas a parte contendo o cardápio.
                cardapio = cardapio.split('*') #Separa o cardápio pelas linhas.
        cardapio = cardapio.split(',') #Dessa vez, separa o cardápio por elemento.
        tam = len(cardapio)
        i = 0
        cardapio_view = '=============== CARDÁPIO ===================\n'
        while i <= tam:
            cardapio_view += f'{i+1} - {cardapio[i][0]}: R$ {cardapio[i][1]}'
            i += 1
        print(cardapio_view)
        escolha = input("\nEscolha uma opção: ").lower()
        pedido = f'{cardapio[escolha-1][0]}'
        v_total += float(cardapio[escolha-1][0])
        lista.inserir(1, pedido)
        print("\nCarrinho: ", lista)
        print(f'Total: {v_total:.2f}')
        print("\nDeseja continuar comprando? (S,N)")
        confirmacao = input('Opção: ').lower()
        if confirmacao == 'n':
            return lista.__str__()
        else:
            carrinho_pedidos()

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
        item = input('Insira o nome do item ou sua posição no carrinho: ').capitalize()
        try:
            if lista.busca(item):
                lista.remover(lista.busca(item))
            else:
                lista.remover(int(item))
            print(lista)
            carrinho_pedidos(lista)
        except ListaException as le:
            print(le)
            carrinho_pedidos(lista)
    elif escolha == '2':
        fazPedido(lista)
    else:
        return


def dadosPagamento():
    limpaTerminal()
    global v_total
    cliente = Cliente()
    print("Para finalizar, preencha os campos abaixo:")
    cliente.setNome(input("Nome: "))
    cliente.setTelefone(input("Telefone: "))
    cliente.setCep(input("Cep: "))
    print("\nVALOR TOTAL:", v_total)
    print("Forma de pagamento:")
    print("1 - Cartão (pagamento na entrega)\n2 - Dinheiro")
    cliente.setPagamento(input("Opção: "))
    if cliente.getPagamento() == 'Dinheiro':
        print("Vai ser necessário troco?(S/N)")
        troco = input().lower()
        if troco == 's':
            valor = float(input("Informar o valor do troco: "))
            cliente.setTroco(valor)
    return cliente

def esvaziaCarrinho(lista):
    while not (lista.estaVazia()):
        lista.remover(lista.tamanho())


def limpaTerminal():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

# -------------- Início programa principal ------------

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
        fazPedido(carrinho)

    elif menu == "2":
        carrinho_pedidos(carrinho)

    elif menu == "3":
        if len(carrinho) != 0:
            dados = dadosPagamento()
            req = f'{cmd_client[1]}/{carrinho}/{dados}\n'
            sock.send(str.encode(req))
            input('\nPressione ENTER para voltar ao MENU...')
            esvaziaCarrinho(carrinho)
            v_total = 0
        else:
            limpaTerminal()
            print("\nSeu carrinho está vazio! Adicione algo para fazer seu pedido!")
            input("\nPressione ENTER para ir ao cardápio...")
            fazPedido(carrinho)

    elif menu == 'x':
        req = cmd_client[2]
        sock.send(str.encode(req))
        req = sock.recv(1024)
        req = req.decode()
        req = req.split('/')
        if req[0] == 'QUIT_OK':
            print(req.decode())
            break

sock.close()