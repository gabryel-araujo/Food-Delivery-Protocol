import socket, sys
from listaEncadeada import Lista, ListaException
from menu import *


HOST = '127.0.0.1'
PORTA = 41800
mensagem = 0



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
            # while confirmacao != 'n':
                mensagem = Escolha_Cardapio(carrinho)
                # print("\nCarrinho: ", mensagem)
                # print(f'Total: {total:.2f}')
                # print("\nDeseja continuar comprando? (S/N)")
                # confirmacao = input('Opção: ').lower()
            
                    
        elif menu == "2":
            carrinho_pedidos(carrinho)
            

        elif menu == "3":
            if mensagem != 0:
                mensagem = contato(carrinho)
                sock.send(str.encode(mensagem))
                mensagem = sock.recv(1024)
                mensagem = mensagem.decode()
                print('\nSeu pedido foi enviado com sucesso!')
                input('\nPressione ENTER para voltar ao MENU...')
                mensagem = 0
                total = 0
            else:
                limpaTerminal()
                print("\nSeu carrinho está vazio! Adicione algo para fazer seu pedido!")   
                input("\nPressione ENTER para ir ao cardápio...")
                Escolha_Cardapio(carrinho) 

        elif menu == 'x':
            print("\nAgradecemos por sua preferência. Volte sempre!")
            break

    # except:
            print("\n"+"Você saiu!")
            break  
    
    #if not mensagem:
        #break

sock.close()