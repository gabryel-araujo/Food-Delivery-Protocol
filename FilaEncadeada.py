class FilaException(Exception):
    def __init__(self,msg):
        super().__init__(msg)

class No:
    def __init__(self, carga:any):
        self.__carga = carga
        self.__prox = None

    @property
    def carga(self):
        return self.__carga
    
    @carga.setter
    def carga(self, novaCarga):
        self.__carga = novaCarga

    @property
    def prox(self):
        return self.__prox

    @prox.setter
    def prox(self, novoNo):
        self.__prox = novoNo
    

    def temProximo(self)->bool:
        return self.__prox == None

    def __str__(self):
        return f'{self.__carga}'

class Head:
    def __init__(self):
        self.__frente = None
        self.__final  = None
        self.__tam = 0
    
    @property
    def frente(self):
        return self.__frente
    
    @property
    def final(self):
        return self.__final

    @property
    def tam(self):
        return self.__tam

    @frente.setter
    def frente(self, novoNo):
        self.__frente = novoNo
    
    @final.setter
    def final(self, novoNo):
        self.__final = novoNo

    @tam.setter
    def tam(self, novoNo):
        self.__tam = novoNo


class Fila:

    def __init__(self):
        self.__head = Head()

    
    def estaVazia(self)->bool:
        return self.__head.tam == 0

    def __len__(self)->int:
        return self.__head.tam

    def enfileira(self, carga:any):
        novoNo = No(carga)
        if self.estaVazia():
            self.__head.frente = self.__head.final = novoNo
        else:
            self.__head.final.prox = novoNo
            self.__head.final = novoNo
        self.__head.tam += 1

    
    def desenfileira(self)->any:
        if self.estaVazia():
            raise FilaException("Fila está vazia")

        carga = self.__head.frente.carga
        if self.__head.tam == 1:
            self.__head.final = None
        self.__head.frente = self.__head.frente.prox
        self.__head.tam -= 1
        return carga


    def __str__(self)->str:
        s = 'Pedido: [ '
        cursor = self.__head.frente
        while(cursor != None):
            s += f'{cursor.carga}, ' 
            cursor = cursor.prox
        return s[:-2] + ' ]'

    def elemento(self, posicao:int)->any:
        if posicao <= 0 or posicao > self.__len__():
            raise FilaException(f"Posicao invalida. A fila so tem {self.__len__()} elementos.")
        
        contador = 1
        cursor = self.__head.frente
        while(cursor != None):
            if contador == posicao:
                return cursor.carga
            cursor = cursor.prox
            contador += 1
        
                
    def busca(self, key:any)->int:
        contador = 1
        cursor = self.__head.frente
        while(cursor != None):
            if key == cursor.carga:
                return contador
            cursor = cursor.prox
            contador += 1

        raise FilaException(f"A chave {key} não está na fila.")

