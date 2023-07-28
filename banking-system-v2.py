import random 
usuarios_nomes= []
contas_correntes =[]

def criar_conta():
    while True:
        usuario_nome=str(input("insira seu nome e sobrenome: "))
        usuario_idade=int(input("insira sua idade: "))
        usuario_sexo=str(input("insira seu sexo: m/f/não-binário "))
        usuario_cidade=str(input("insira sua cidade: "))
        usuario_cep=int(input("insira seu cep: "))
        usuario_rua=str(input("insira seu endereço: "))
        usuario_numero_casa=int(input("insira o número de sua casa: "))
        usuario_complemento=str(input("complemento "))
        usuario_estado=str(input("seu estado: "))
        continuar= str(input("deseja continuar ? s/n  "))
        #inserindo as variáveis em uma lista
        usuarios_nomes.append(usuario_nome)
        
        
        if continuar== "s":
            print("continuando...")
        elif continuar=="n":
            print("obrigado")
            #print(usuarios)
            break
        else:
            print("comando inválido ")
            
            
            
def conta_corrente():
        numero_conta=random.randint(0,1000)
        for item in range(0,len(usuarios_nomes)):
            print(f'seu nome {usuarios_nomes[item]} e o número de sua conta #000{numero_conta}')
            contas_correntes.append(numero_conta)
            
        
                      
dados={
    "usuarios":usuarios_nomes,
    "conta_corrente":contas_correntes
}
def bem_vindo():
    print("*"*100)
    print("bem vindo ao cyber bank")
    print("para operaçoes, usa: d para deposito, e para extrato, s para saque, q para sair")
    opcao=input('insira o comando: ')
    if opcao=="d":
        print("deposito")
    
#def saldo():
    
def deposito():
    while True:
     
      deposito = float(input('insira o valor:'))
      saldo=0
      print(f'seu saldo inicial: R$ {saldo:.2f}\n')
      saldo+=deposito
      print(f'seu saldo atual: R$ {saldo:.2f}\n')
      continuar=str(input("quer continuar? s/n: ") 
      if continuar=="n":
          print(f'seu saldo atual: R$ {saldo:.2f}\n')
          break 
          
          
       
          
      
    
     
#def extrato():
      
#chamando as funções e imprimindo variáveis 
#criar_conta()
#conta_corrente()
bem_vindo()
deposito()
#print(usuarios_nomes)
#print(contas_correntes)
#print(dados)


