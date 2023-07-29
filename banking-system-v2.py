import random as r
usuarios_nomes= []
contas_correntes =[]
saldo=0
numeros_saques=0
nome=str(input("insira seu nome: "))
sobrenome=str(input("insira o seu sobrenome: "))
idade=int(input("insira sua idade:"))
cep=int(input("insira seu cep: "))
rua=str(input("insira o endereço: "))
numero_casa=int(input("insira o número da casa: "))
cidade=str(input("insira a cidade: "))
estado=str(input("insira seu estado: "))
print("conta criada com sucesso! :)")
conta=r.randint(0,1000)  
print(f'sua conta corrente: {conta}')     
      
        
        
        
            
            

                      
def bem_vindo():
    print("*"*100)
    print(f"bem vindo ao cyber bank, {nome} {sobrenome}")
    print("para operaçoes, usa: d para deposito, e para extrato, s para saque, q para sair")
    opcao=input('insira o comando: ')
    while True:
        if opcao=="d":
           print("deposito")
           deposito()
           
        elif opcao=="s":
            print("saque")
            saque()
    
    
def deposito():
     
      deposito = float(input('insira o valor:'))
      global saldo
      print(f'seu saldo inicial: R$ {saldo:.2f}\n')
      saldo+=deposito
      print(f'seu saldo atual: R$ {saldo:.2f}\n')
      if deposito < 0:
            print("saldo negativo")
            modulo= -1
            saldo_corrigido= saldo * modulo
            saldo=saldo_corrigido
            print(f'seu saldo corrigido: R$ {saldo:.2f}\n')
            
         
def saque():
          saque = float(input('insira o valor: '))
          global saldo 
          print(f'valor inicial do saldo: R$ {saldo:.2f}\n')
          saldo-=saque
          print(f'valor sacado: R$ {saque:.2f}\n')
          print(f'valor atual do saldo: R$ {saldo:.2f}\n')
          
              
         
  
          
#chamando as funções e imprimindo variáveis 


bem_vindo()




aques in range(1,4):
            if numeros_saques >=3:
               print('limite diário de saques atingidos! ')
               print(f'valor atual do saldo: R$ {saldo:.2f}\n')
               break 
              
         
  
          
#chamando as funções e imprimindo variáveis 


bem_vindo()




()




indo variáveis 
#criar_conta()
#conta_corrente()
bem_vindo()
#deposito()
#print(usuarios_nomes)
#print(contas_correntes)
#print(dados)


print(dados)


