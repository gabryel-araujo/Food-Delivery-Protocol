import os
from Lista_Encadeada import*

total = 0
    
#Criei aqui um protótipo de menu para o servidor para se comportar parecido com o do cliente

def menuServidor():
    escolha = ''
    print("===Área da Pizzaria===")
    print('1 - Abrir pizzaria')
    print("2 - Exibir pedidos")
    escolha = input('Selecione uma opção: ')

    if escolha == '1':
        return '1'
    
    if escolha == '2':
        return '2'