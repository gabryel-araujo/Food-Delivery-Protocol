import socket, sys

HOST = '127.0.0.1'
PORTA = 41800

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
while True:
    try:
        print("===Menu===")
        print("1 - Pepperoni")
        print("2 - Frango com catupiry")
        print("3 - Calabresa")
        print("4 - Quatro queijos")
        print("5 - À moda da casa")
        mensagem = input("Escolha uma opção: ")
    except:
        print("\n"+"Você saiu!")
        break
    sock.send(str.encode(mensagem))
    mensagem = sock.recv(1024)
    if not mensagem:
        break
    mensagem = mensagem.decode()
    print("Pedido enviado: ", mensagem)
sock.close()