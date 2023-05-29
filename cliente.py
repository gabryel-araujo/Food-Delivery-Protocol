import socket, sys
from FilaEncadeada import Fila, FilaException

HOST = '127.0.0.1'
PORTA = 41800

pedido = Fila()
confirmacao = 1

if len(sys.argv) > 1:
    HOST = sys.argv[1]

servidor = (HOST, PORTA)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Exceção será lançada informando que a pizzaria está fechada caso o cliente tente se conectar com o servidor fechado
try:
    sock.connect(servidor)
except ConnectionRefusedError as cre:
    print("A pizzaria se encontra fechada")
    sys.exit()

while confirmacao != 0:
    try:
        print("===Menu===")
        print("1 - Pepperoni")
        print("2 - Frango com catupiry")
        print("3 - Calabresa")
        print("4 - Quatro queijos")
        print("5 - À moda da casa")
        temp = input("Escolha uma opção: ")
            
        if temp == "1":
            pedido.enfileira("Pepperonni")
        elif temp == "2":
            pedido.enfileira("Frango com catupiry")
        elif temp == "3":
            pedido.enfileira("Calabresa")
        elif temp == "4":
            pedido.enfileira("Quatro queijos")
        elif temp == "5":
            pedido.enfileira("À moda da casa")

        print("\nPara continuar comprando digite: 1")
        print("Para fechar o pedido digite: 0")
        confirmacao = int(input('Opção: '))
    except:
        print("\n"+"Você saiu!")
        break
    if confirmacao == 0:
        mensagem = pedido.__str__()
        sock.send(str.encode(mensagem))
        mensagem = sock.recv(1024)
        mensagem = mensagem.decode()
        print("Carrinho: ", mensagem)
    #if not mensagem:
        #break

sock.close()