import socket, sys
from listaEncadeada import Lista, ListaException

HOST = '127.0.0.1'
PORTA = 41800

pedido = Lista()
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
        print(pedido.estaVazia())
        print("===Menu===")
        print("1 - Pepperoni")
        print("2 - Frango com catupiry")
        print("3 - Calabresa")
        print("4 - Quatro queijos")
        print("5 - À moda da casa")
        temp = input("Escolha uma opção: ")
            
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
        print(pedido.estaVazia())
        mensagem = pedido.__str__()
        print("Carrinho: ", mensagem)
        print("\nPara continuar comprando digite: 1")
        print("Para fechar o pedido digite: 0")
        confirmacao = int(input('Opção: '))
        
    except:
        print("\n"+"Você saiu!")
        break
    if confirmacao == 0:
        sock.send(str.encode(mensagem))
        mensagem = sock.recv(1024)
        mensagem = mensagem.decode()
    #if not mensagem:
        #break

sock.close()