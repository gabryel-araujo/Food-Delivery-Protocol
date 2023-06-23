import socket, sys
from Lista_Encadeada import*
from menu import*


HOST = '127.0.0.1'
PORTA = 41800
mensagem = 0
options = ['menu', 'send', 'quit']

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
    # try:
        menu = showMenu()
        if menu == "1":
                req = options[0]
                sock.send(str.encode(req))
                req = sock.recv(1024)
                print(req)

            # while confirmacao != 'n':
                # req = options[0]
                # sock.send(str.encode(req))
                # req = sock.recv(1024)
                # req = req.decode()
                mensagem = Escolha_Cardapio(carrinho)
                # print("\nCarrinho: ", mensagem)
                # print(f'Total: {total:.2f}')
                # print("\nDeseja continuar comprando? (S/N)")
                # confirmacao = input('Opção: ').lower()
            
                    
        elif menu == "2":
            carrinho_pedidos(carrinho)
            

        elif menu == "3":
            if len(mensagem) != 0:
                req = options[1]
                mensagem = pagamento(carrinho)
                sock.send(str.encode(mensagem))
                mensagem = sock.recv(1024)
                mensagem = mensagem.decode()
                print 

                # print('\nSeu pedido foi enviado com sucesso!')
                # input('\nPressione ENTER para voltar ao MENU...')
                mensagem = 0
                total = 0
                carrinho.esvaziar()
            else:
                limpaTerminal()
                print("\nSeu carrinho está vazio! Adicione algo para fazer seu pedido!")   
                input("\nPressione ENTER para ir ao cardápio...")
                Escolha_Cardapio(carrinho) 

        elif menu == 'x':
            req = options[2]
            sock.send(str.encode(req))
            req = sock.recv(1024)
            print(req)
            
            
            
            # print("\nAgradecemos por sua preferência. Volte sempre!")
            break

    # except:
            print("\n"+"Você saiu!")
            break  
    
    #if not mensagem:
        #break

sock.close()