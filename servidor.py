import socket, os, sys

HOST = '127.0.0.1'
PORTA = 41800

def processarCliente(con, cliente):
    print("Conectado com: ", cliente)
    while True:
        mensagem = con.recv(1024)
        msgDecodificada = mensagem.decode()
        if not mensagem: break
        if msgDecodificada == "1":
            print(cliente, "Pedido selecionado: Pepperoni")
        if msgDecodificada == "2":
            print(cliente, "Pedido selecionado: Frango com catupiry")
        if msgDecodificada == "3":
            print(cliente, "Pedido selecionado: Calabresa")
        if msgDecodificada == "4":
            print(cliente, "Pedido selecionado: Quatro queijos")
        if msgDecodificada == "5":
            print(cliente, "Pedido selecionado: À moda da casa")

        con.send(mensagem)
    print("Desconectando do cliente", cliente)
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
