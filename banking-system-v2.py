import random as r
usuarios_nomes= []
usuarios_cpf=[]
saldo=0
numeros_saques=0
def criar_conta():
     nome=str(input("insira seu nome: "))
     sobrenome=str(input("insira o seu sobrenome: "))
     cpf=int(input('insira seu cpf: '))
     idade=int(input("insira sua idade:"))
     cep=int(input("insira seu cep: "))
     rua=str(input("insira o endereço: "))
     numero_casa=int(input("insira o número da casa: "))
     cidade=str(input("insira a cidade: "))
     estado=str(input("insira seu estado: "))
     print("conta criada com sucesso! :)")
     numero_conta=r.randint(0,1000)  
     print(f'sua conta corrente: 0{numero_conta}')     
      
        
        
        
            
            

                      
def bem_vindo():
   print("para operaçoes, usa: d para deposito, e para extrato, s para saque, q para sair")
   while True:
       opcao=str(input('insira o comando: '))
       if opcao=="d":
             print("deposito")
             deposito()
           
       elif opcao=="s":
             print("saque")
             saque()
             global numeros_saques
             numeros_saques+=1
             print(numeros_saques)
             if numeros_saques>=3:
                 print("limite atingido!")
                 break 
       elif opcao=="q":
            print("saindo")
            break 
       else:
             print("comando inválido :(")
 
 
    
        
    
   
    
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


#criar_conta()
bem_vindo()
#deposito()
#print(usuarios_nomes)
#print(contas_correntes)
#print(dados)





