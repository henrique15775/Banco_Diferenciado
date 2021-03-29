import classes
import os  
import time
from classes import posicaoinvalidaException
bank = classes.Banco("Banco ITAU")

while __name__ == '__main__':

  os.system('clear')
  print('#'*36)
  print('#'*36)
  print('#'*6 + "  SISTEMA CONFIDENCIAL " + '#'*7)
  print('#'*36)
  print('#'*9 + "  Banco ITAU   " + '#'*12)
  print('#'*36 + '\n'*3)
  #print(bank.contasL.cabeca)
  #print(bank.contasP.mostrar_elemento())
  #print(bank.contasF.mostrar_elemento())
  opcao = input('#1- Adicionar conta  \n#2- Remover Conta \n#3- Mostrar tamanho \n#4- Imprimir contas \n#5- Fazer uma busca na Lista  \n#6- Adicionar Valor para a conta\n#7- Ordenar Lista\n#8- Mostrar valor total do banco\n\n-> ')
  
  if opcao == '1':
    while True:
      try:
        os.system("clear")
        id = int(input("Digite o ID -> "))
        cpf = input("Digite o CPF -> ")
        sald = float(input("Digite o Saldo -> "))
        account = classes.conta(id,cpf,sald)
        while id != None:
          opt_add = input("\n\n#1- Adicionar na Lista\n#2- Adicionar na Pilha\n#3- Adicionar na Fila\n\n-> ")
          if opt_add == '1':
            posicao = int(input("Digite a posição -> "))
            bank.adicionar_conta_L(account,posicao)
            break
          elif opt_add == '2':
            bank.adicionar_conta_P(account)
            break 
          elif opt_add == '3':
            bank.adicionar_conta_F(account)
            break
          else:
            print("Digite Novamente")
        break
      except ValueError:
        print("O Valor inserido é de um tipo inválido!")
        time.sleep(1)
      except posicaoinvalidaException:
        print("Posição Invalida!!")
        time.sleep(1)
  elif opcao == '2':
    while True:
      try:
        os.system("clear")
        opt_add = input("\n\n#1- Remover na Lista\n#2- Remover na Pilha\n#3- Remover na Fila\n\n-> ")
        while opt_add != None:
          if opt_add == '1':
            posicao = int(input("Digite o posição -> "))
            bank.remover_conta_L(posicao)
            break
          elif opt_add == '2':
            bank.remover_conta_P()
            break 
          elif opt_add == '3':
            bank.remover_conta_F()
            break
          else:
            print("Digite Novamente")
        break
      except ValueError:
        print("O Valor inserido é de um tipo inválido!")
        time.sleep(1)
      except posicaoinvalidaException:
        print("Posicao Invalida! Digite Novamente!")
        time.sleep(1)
  elif opcao == '3':
     while True:
      try:
        os.system("clear")
        while 1:
          opt_add = input("\n\n#1- Tamanho Lista\n#2- Tamanho na Pilha\n#3- Tamanho na Fila\n\n-> ")
          if opt_add == '1':
            
            
            print(f"{bank.mostrar_tamanho_L()} Elementos")
            time.sleep(1)
            break
          elif opt_add == '2':
            print(f"{bank.mostrar_tamanho_P()} Elementos")
            time.sleep(1)
            break 
          elif opt_add == '3':
            print(f"{bank.mostrar_tamanho_F()} Elementos")
            time.sleep(1)
            break
          else:
            print("Digite Novamente")
        break
      except ValueError:
        print("O Valor inserido é de um tipo inválido!")
        time.sleep(1)      
  elif opcao == '4':
    bank.imprimir_contas()
    time.sleep(3)
  elif opcao == '5':
    while True:
     try:
       os.system("clear")
       id = int(input("Digite o ID -> "))
       print(bank.busca_conta(id))
       break
     except ValueError:
       print("Valor errado!")
    time.sleep(3)
  elif opcao == '6':
    while True:
     try:
        os.system("clear")
        id = int(input("Digite o ID -> "))
        value = float(input("Digite o valor -> "))
        bank.adiciona_valor_conta(id,value)
        break
     except ValueError:
        print("Valor Invalido!!")
  elif opcao == '7':
        bank.ordenar_contas()
        time.sleep(1)
  elif opcao == '8':
        print("\n Valotr total ->"+ bank.total_valor_contas() + " R$")
        time.sleep(1)
  else:
      print('Erro! Digite a opção novamente!')   
      time.sleep(2)
          




 # p.remover()
 # print(p)

 # p.remover()
 # print(p)

  
  #banco1 =  classes.Banco("Banco do Brasil")
  #conta1 = classes.conta(157,1,2000)
 # banco1.contasL.inserir(1,conta1)
  #lista = classes.ListaEncadeada()
  #lista = classes.ListaEncadeada()
 # print("Lista vazia:", lista)
  #conta1 = classes.conta(157,1,5000)
  #lista.inserir(1,conta1)
#  lista.inserir(1,10)
#  print("Lista contém um único elemento:", lista)
 # conta2 = classes.conta(147,2,10000)
  #lista.inserir(2,conta2)
 # conta3  = classes.conta(137,3,20000)
#  lista.inserir(3,conta3)
  #print(lista)
#  print()
  #lista.inserir(2,20)
  #print("Inserindo um novo elemento:", lista)

  #lista.inserir(3,20)
 # lista.inserir(2,20)
  #print(lista.cabeça)
 # print(lista.tamanho)
 # print(lista)

 #banco1 =  classes.Banco("Banco do Brasil")
 #conta1 = classes.conta(147,1,2000)
 #banco1.adicionar_conta_L(conta1)
 #conta2 = classes.conta(137,2,5000)
 #banco1.adicionar_conta_L(conta2)
 #conta3 = classes.conta(157,3,5000)
 #banco1.adicionar_conta_L(conta3)
 #banco1.contasL.ordernar()
 #conta4 = classes.conta(177,3,5000)
 #banco1.contasL.adicionar(4,conta4)
 #print(banco1.contasL.ordernar())
 #conta_pilha1 = classes.conta(177,4,10000)
 #banco1.contasP.adicionar(conta_pilha1)
 #print(banco1.total_valor_contas())
# print(banco1.contasL.busca(137,3))
 #print(banco1.total_valor_contas()) 
# print(banco1.contasL.imprimir(137,3))
 #print(banco1.contasP)
 #print(banco1.contasL.cabeca)
 #print(banco1.contasL)