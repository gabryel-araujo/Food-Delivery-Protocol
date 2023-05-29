import socket, sys

HOST = '127.0.0.1'
PORTA = 41800

if len(sys.argv) > 1:
    HOST = sys.argv[1]

servidor = (HOST, PORTA)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(servidor)

while True:
    try:
        mensagem = input("Digite CTRL + D para encerrar: ")
    except:
        print("\n"+"Você Saiu!")
        break
    sock.send(str.encode(mensagem))
    mensagem = sock.recv(1024)
    if not mensagem:
        break
    mensagem = mensagem.decode()
    print("Pedido enviado: ", mensagem)
sock.close()