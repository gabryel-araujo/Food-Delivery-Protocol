import socket, os, sys
from FilaEncadeada import Fila, FilaException
import threading
from cardapio import*
from menu import*

HOST = '127.0.0.1'
PORTA = 41800
cmd_server = ['SENT_MENU', 'ADD_ITEM', 'VALOR']

pedidos = Fila()
dados_cliente = Fila()
clientList = []
total = 0

escolha = menuServidor()

if escolha == '1':
    pass
elif escolha == '2':
    pass
elif escolha == '3':
    pass
elif escolha == '4':
    print("===Cardápio===\n")
    for item in cardapio:
        print(f'{item} - {cardapio[item][0]}: R$ {cardapio[item][1]:.2f}')
    print("\n1 - Remover item do cardápio")
    print("2 - Adicionar item do cardápio")
    print("3 - Voltar")
    opcao = input('Escolha uma opção: ')

def processarCliente(con, cliente):
    clientList.append(cliente)
    global total
    while True:
        mensagem = con.recv(1024)
        msgDecodificada = mensagem.decode()
        msgDecodificada = msgDecodificada.split('/')
        if msgDecodificada[0] == 'MENU':
            if msgDecodificada[1] == 'SHOW':
                cardapio_view = f'{cmd_server[0]}/===CARDÁPIO===\n'
                for item in cardapio:
                    cardapio_view += f'{item} - {cardapio[item][0]}: R$ {cardapio[item][1]:.2f}\n'
                con.send(str.encode(cardapio_view))
            if msgDecodificada[1] == 'CHOOSE':
                if msgDecodificada[2] in cardapio.keys():
                    total = cardapio[msgDecodificada[2]][1] #Total é incrementado com o valor do pedido que consta no cardápio.
                    pedido = f'{cmd_server[1]}/{cardapio[msgDecodificada[2]][0]}/{total}' #Forma uma string com o pedido e valor total atual.
                    con.send(str.encode(pedido)) #Envia a string ao cliente.
        elif msgDecodificada[0] == "SEND":
            pedidos.enfileira(msgDecodificada[1])
            dados_cliente.enfileira(msgDecodificada[2])
            print("Pedido do cliente",msgDecodificada[1])
            print("Dados: ",msgDecodificada[2])
            print("="*50)
            print(f"Pedidos em espera: {pedidos} Total: {len(pedidos)}")
            con.send(str.encode(f'\nRecebemos seu pedido com sucesso!\nPedido:{msgDecodificada[1]}'))
        elif msgDecodificada[0] == "REMOVE":
            for item in cardapio.values():
                if item[0] == msgDecodificada[1]:
                    total = f'{cmd_server[2]}/{item[1]}'
            con.send(str.encode(total))
        elif msgDecodificada == 'quit':
            con.send(str.encode('\nXau xau! Volte sempre que estiver com fome!'))

        if not mensagem: break

    print("Desconectando do cliente", cliente)
    #mensagem do servidor: agradecemos a preferência teste
    con.close()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor = (HOST, PORTA)
sock.bind(servidor)
sock.listen(50)
while True:
    try:
        con, cliente = sock.accept()
    except KeyboardInterrupt as ke:
        print("\n" + "Servidor encerrado!", ke)
        break
    t = threading.Thread(target=processarCliente, args=(con, cliente,))
    t.start()
    # pid = os.fork()
    # if pid == 0:
    #     sock.close()
    #     processarCliente(con,cliente)
    #     sys.exit(0)
con.close()
sock.close()

#área para adicionar novas ideias e coisas para fazer
# 1)criação de um chat para falar com a empresa sobre o pedido