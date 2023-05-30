import socket, sys
from listaEncadeada import Lista, ListaException
from menu import showMenu, Escolha_Cardapio, carrinho_pedidos

HOST = '127.0.0.1'
PORTA = 41800

carrinho = Lista()
confirmacao = ''
mensagem = ''

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
        menu = showMenu()
        confirmacao = ""

        if menu == "1":
            while confirmacao != 'n':
                mensagem = Escolha_Cardapio(carrinho)
                print("\nCarrinho: ", mensagem)
                print("\nDeseja continuar comprando? (S/N)")
                confirmacao = input('Opção: ').lower()


        elif menu == "2":
            escolha = carrinho_pedidos(carrinho)


        elif menu == "3":
            sock.send(str.encode(mensagem))
            mensagem = sock.recv(1024)
            mensagem = mensagem.decode()
            print('\nSeu pedido foi enviado com sucesso!')
            input('\nAperte ENTER para voltar ao MENU...')

        elif menu == 'x':
            print("\nAgradecemos por sua preferência. Volte sempre!")
            break

        # confirmacao = int(input('Opção: '))
    except:
        print("\n"+"Você saiu!")
        break

    #if not mensagem:
        #break

sock.close()