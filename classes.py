import time

class posicaoinvalidaException(Exception):
  
    def __init__(self,msg):
        
        super().__init__(msg)

class PilhaException(Exception):
  def __init__(self,mensagem):
    super().__init__(mensagem)

class listaException(Exception):
  def __init__(self, mensagem):
    super().__init__(mensagem)

class valorinvalidoException(Exception):
  def __init__(self,mensagem):
    super().__init__(mensagem)


class ListaEncadeada:

    def __init__(self):
        self.__cabeca = None
        self.__tamanho = 0

    def listavazia(self):
        return True if self.__tamanho ==0 else False
    @property
    def tamanho(self):
        return self.__tamanho
    @property
    def cabeca(self):
        return self.__cabeca
    @cabeca.setter
    def cabeca(self,new_cabeça):
        self.__cabeca = new_cabeça
   

    
    def busca(self, id,posicao):
        if (self.listavazia()):
            raise posicaoinvalidaException('Lista vazia')
        
        apontador = self.__cabeca
        contador = 1

        while( apontador != None ) and (contador <= posicao):
            if( apontador.ide == id) and (contador == posicao):
                return apontador
            apontador = apontador.prox
            contador += 1
            
     
    def adicionar(self,id,cpf,saldo,posicao ):

        try:
            assert posicao > 0

           
            if (self.listavazia()):             
                if ( posicao != 1):                    
                    raise posicaoinvalidaException('A lista esta vazia. A posicao correta para insercao é 1.')

                self.__cabeca = conta(id,cpf,saldo)
                self.__tamanho += 1
                return
            
           
            if ( posicao == 1):
                novo = conta(id,cpf,saldo)
                novo.prox = self.__cabeca
                self.__cabeca = novo
                self.__tamanho += 1
                return

            
            apontador = self.__cabeca
            contador = 1
            while ( (contador < posicao-1) and  (apontador != None)):
                apontador = apontador.prox
                contador += 1

            if ( apontador == None ):
                raise posicaoinvalidaException(f'A posicao {posicao} é invalida para essa lista.')
            
            novo = conta(id,cpf,saldo)
            novo.prox = apontador.prox
            apontador.prox = novo
            self.__tamanho += 1

        except AssertionError:
            raise posicaoinvalidaException('A posicao não pode ser um número negativo ou 0 (zero)')
        except:
            raise


    def remover(self, posicao):
 
        try:
            assert posicao > 0

            if(self.listavazia() ):
                raise posicaoinvalidaException('Não é possível remover de uma lista vazia!!!')

            apontador = self.__cabeca
            contador = 1

            while( (contador <= posicao - 1) and (apontador != None) ) :
                anterior = apontador
                apontador = apontador.prox
                contador+=1

            if ( apontador == None ):
                raise posicaoinvalidaException(f'Posicao {posicao} invalida para remoção')

            dado = apontador

            if( posicao == 1):
                self.__cabeca = apontador.prox
            else:
                anterior.prox = apontador.prox

            self.__tamanho -= 1
            return dado
        
        except AssertionError:
            raise posicaoinvalidaException('A posicao não pode ser um número negativo')
        except:
            raise
    def imprimir_contas(self):
      print('Lista:\n ',end='')

      apontador = self.__cabeca

      print('[ \n',end='')
      while( apontador != None ):
        print(f'{apontador} ', end='')
        apontador = apontador.prox
        time.sleep(2)
      print(']')
     #print(']')

    def ordernar(self):
      ordenado = False
      pointer = self.__cabeca 
      while not ordenado:
          ordenado = True
          for x in range(self.__tamanho + 1):
            if pointer.prox != None:
              if pointer.ide > pointer.prox.ide:
               pointer.ide,pointer.cpf,pointer.saldo,pointer.prox.ide,pointer.prox.cpf,pointer.prox.saldo = pointer.prox.ide,pointer.prox.cpf,pointer.prox.saldo,pointer.ide,pointer.cpf,pointer.saldo
               
               pointer = pointer.prox
               ordenado = False
               
          confirm = False
      pointer = self.__cabeca   
      while not confirm:
          confirm = True
          for x in range(self.__tamanho + 1):
            if pointer.prox != None:
              if pointer.ide > pointer.prox.ide:                
               pointer.ide,pointer.cpf,pointer.saldo,pointer.prox.ide,pointer.prox.cpf,pointer.prox.saldo = pointer.prox.ide,pointer.prox.cpf,pointer.prox.saldo,pointer.ide,pointer.cpf,pointer.saldo
               pointer = pointer.prox
               
               confirm = False
               print(pointer)        
          
      return True
    def __repr__(self):
      return f"{self.__cabeca}"


    
        



# ***************************** PILHA *****************************




class PilhaEncadeada:
  def __init__(self):
    self.__topo = None
    self.__tamanho = 0

  @property
  def topo(self):
      if self.vazia():
        raise PilhaException('A pilha está vazia')
      return self.__topo.cpf

  def vazia(self):
    return self.__tamanho == 0
  
  def tamanho(self):
    return self.__tamanho
  
  def adicionar(self,id,cpf,saldo):
    no = conta(id,cpf,saldo)
    no.prox = self.__topo
    self.__topo = no
    self.__tamanho += 1  

  def remover(self):
      if self.vazia():
        raise PilhaException('A pilha está vazia')
      self.__topo = self.__topo.prox
      self.__tamanho -= 1  

  def __str__(self):
    saida = 'Pilha: ['
    p = self.__topo

    while p != None:
      saida += f'{p}'
      p = p.prox

      if p != None:
        saida += ', '
    
    saida += ']'
    return saida

  def mostrar_elemento(self):
    p = self.__topo
    return f"{p}"
      
      

  def modificar(self, novoValor):
      if self.vazia():
        raise PilhaException('A pilha está vazia')
      
      self.__topo.dado = novoValor





# ****************************** BANCO + CONTA *************************************




class Banco:
    def __init__(self, nome_do_banco):
        self.__nome_do_banco = nome_do_banco
        self.__contasL = ListaEncadeada()
        self.__contasP = PilhaEncadeada()
        self.__contasF = FilaEncadeada()
    
#Gets
    @property
    def nome_do_banco(self):
        return self._nome_do_banco
    
    @property
    def contasL(self):
        return self.__contasL
    
    @property
    def contasP(self):
        return self.__contasP
    @property
    def contasF(self):
        return self.__contasF
    

    
#Setts
    @nome_do_banco.setter
    def nome_do_banco(self, novo_banco):
        self.__nome_do_banco = novo_banco
    @contasL.setter
    def contasL(self,nova_conta):
      self.__contasL = nova_conta
    @contasP.setter
    def contasP(self,novo_contasP):
      self.__contasP = novo_contasP
    def total_valor_contas(self):
      sm = 0
      pointer = self.__contasL.cabeca
      
      while (pointer != None):
        sm += pointer.saldo
        pointer = pointer.prox
      return f'{sm}'
    def adicionar_conta_P(self,conta):
      self.__contasP.adicionar(conta.ide,conta.cpf,conta.saldo)
    def adicionar_conta_F(self,conta):
      self.__contasF.adicionar(conta.ide,conta.cpf,conta.saldo)
    def adicionar_conta_L(self,conta,posicao):
      self.__contasL.adicionar(conta.ide,conta.cpf,conta.saldo,posicao)
    def remover_conta_L(self,posicao):
      self.__contasL.remover(posicao)
    def remover_conta_P(self):
      self.__contasP.remover()
    def remover_conta_F(self):
      self.__contasF.remover()
    def mostrar_tamanho_L(self):
      return self.__contasL.tamanho
    def mostrar_tamanho_P(self):
      return self.__contasP.tamanho()
    def mostrar_tamanho_F(self):
      return self.__contasF.tamanho()
    def ordenar_contas(self):
      self.__contasL.ordernar()
    def imprimir_contas(self):
      self.__contasL.imprimir_contas()
    def busca_conta(self,id):
      if (self.__contasL.listavazia()):
            raise posicaoinvalidaException('Lista vazia')
        
      apontador = self.__contasL.cabeca
      
        
      while( apontador != None ):
            if( apontador.ide == id):
                return apontador
            apontador = apontador.prox
            
            
    def adiciona_valor_conta(self,id,valor):
      a =  self.busca_conta(id)
      if valor > 0:
        a.creditar(valor)
        return True
      else:
        raise valorinvalidoException('Valor inválido!!')
    def __str__(self):
        return f'{self._nome_do_banco}'
              

class conta:
    def __init__(self, ide, cpf, saldo = 0):
      self.__cpf = cpf
      self.__ide = ide 
      self.__saldo = saldo
      self.__prox = None

    @property
    def ide(self):
        return self.__ide
    
    @property
    def cpf(self):
        return self.__cpf
    
    @property
    def saldo(self):
        return self.__saldo
    @property
    def prox(self):
        return self.__prox
    @prox.setter
    def prox(self,new_prox):
        self.__prox = new_prox
    @ide.setter
    def ide(self, nova_ide):
        self.__ide = nova_ide
    
    @cpf.setter
    def cpf(self, new_cpf):
        self.__cpf = new_cpf
    @saldo.setter
    def saldo(self,new_saldo):
        self.__saldo = new_saldo
    
    def creditar(self, valor):
        self.__saldo += valor
    
    def debitar(self, valor):

        if self._saldo >= valor:
            self._saldo -= valor
        else:
            return "não ha saldo suficiente"
    
    
    
    def __str__(self):
      return f"ID -> {self.__ide}\nCPF ->{self.__cpf}\nSaldo -> {self.__saldo}R$\n\n"



    # ********************************* FILA ************************************






class FilaException(Exception):
  def __init__(self,mensagem):
    super().__init__(mensagem)




class FilaEncadeada:
  def __init__(self):
    self.__inicio = None
    self.__tamanho = 0

  @property
  def inicio(self):
      if self.vazia():
        raise FilaException('A fila está vazia')

      return self.__inicio

  def vazia(self):
    return self.__tamanho == 0
  
  def tamanho(self):
    return self.__tamanho
  
  def adicionar(self,id,cpf,saldo):
      novo = conta(id,cpf,saldo)
      
      aux = self.__inicio

      if aux == None:
          self.__inicio = novo

      else:
          while aux.prox != None:
              aux = aux.prox
      
          aux.prox = novo

      self.__tamanho += 1 

  def remover(self):
      if self.vazia():
        raise FilaException('A fila está vazia')

      self.__inicio = self.__inicio.prox
      self.__tamanho -= 1  
  
  def __str__(self):
    saida = 'Fila: ['
    p = self.__inicio

    while p != None:
      saida += f'{p}'
      p = p.prox

      if p != None:
        saida += ', '
    
    saida += ']'
    return saida

  def mostrar_elemento(self):
    return self.__inicio

  


