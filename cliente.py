import socket, sys
from listaEncadeada import Lista, ListaException
from menu import showMenu, cardapio

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
        showMenu()
        temp = input("Escolha uma opção: ")
            
        if temp == "1":
            cardapio()
            
        elif temp == "2":
            print("Carrinho: ", mensagem)
        elif temp == "3":
            pass
        
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