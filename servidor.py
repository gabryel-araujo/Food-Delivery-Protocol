import socket, os, sys
from FilaEncadeada import Fila, FilaException

HOST = '127.0.0.1'
PORTA = 41800

pedidos = Fila()

def processarCliente(con, cliente):
    print("Conectado com: ", cliente)
    while True:
        mensagem = con.recv(1024)
        msgDecodificada = mensagem.decode()
        if not mensagem: break
        pedidos.enfileira(msgDecodificada)
        print("Pedido do cliente",msgDecodificada)
        print("="*50)
        print(f"Pedidos em espera: {pedidos} Total: {len(pedidos)}")
        con.send(mensagem)

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
    pid = os.fork()
    if pid == 0:
        sock.close()
        processarCliente(con,cliente)
        sys.exit(0)
    con.close()
sock.close()


#área para adicionar novas ideias e coisas para fazer
# 1)criação de um chat para falar com a empresa sobre o pedido