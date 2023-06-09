import socket
import os
import platform
from FilaEncadeada import Fila, FilaException
import threading
from cardapio import *


HOST = '0.0.0.0'
PORTA = 41800
cmd_server = ['SENT_MENU', 'SEND_OK', 'QUIT_OK']

pedidos = Fila()
total = 0
lock = threading.Lock()


def menuPizzaria():
    limpaTerminal()
    escolha = ''
    print("===Área da Pizzaria===")
    print('1 - Abrir pizzaria')
    print("2 - Exibir pedidos")
    print("3 - Sair")
    escolha = input('Selecione uma opção: ')
    return escolha

def processarCliente(con, cliente):
    global total
    while True:
        mensagem = con.recv(1024)
        if not mensagem:
            break
        msgDecodificada = mensagem.decode()
        msgDecodificada = msgDecodificada.split('/')

        if msgDecodificada[0] == 'GET_MENU':
            cardapio_view = f'{cmd_server[0]}\n'
            for item in cardapio:
                cardapio_view += f'{item},{cardapio[item]:.2f}*'
            cardapio_view = cardapio_view[:-1]
            con.send(str.encode(cardapio_view))

        elif msgDecodificada[0] == "SEND":
            lock.acquire()
            try:
                pedidos.enfileira(msgDecodificada[1])
            finally:
                # Libera o bloqueio após a inserção na fila
                lock.release()
            msg = f'{cmd_server[1]}/\n'
            msg += f'Recebemos seu pedido com sucesso!\n{msgDecodificada[1]}'
            con.send(str.encode(msg))

        elif msgDecodificada[0] == 'QUIT':
            msg = f'{cmd_server[2]}/\n'
            msg += 'Xau xau! Volte sempre que estiver com fome!'
            con.send(str.encode(msg))

    print("Desconectando do cliente", cliente)
    con.close()

def limpaTerminal():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')



   
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor = (HOST, PORTA)
sock.bind(servidor)
sock.listen(50)

escolha = menuPizzaria()

if escolha == '1':
    con, cliente = sock.accept()
    t = threading.Thread(target=processarCliente, args=(con, cliente,))
    t.start()
    escolha = 0
    while escolha != '3':
        if escolha == '1':
            print('\nA pizzaria já está aberta!')
            input()
            pass
        elif escolha == '2':
            if(pedidos.estaVazia()):
                print("A fila de pedidos está vazia!")
                input()
            else:
                lock.acquire()
                try:
                    print(pedidos)
                    view = ''
                    tam = pedidos.__len__()
                    i = 0
                    while i < tam:
                        view += f'{1} - {pedidos}'
                        print(view)
                finally:       
                        input()
                    

        escolha = menuPizzaria()

print("Encerrando servidor...")
sock.close()
