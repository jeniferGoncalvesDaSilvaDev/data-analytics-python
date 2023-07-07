#deposito 
#saque
#extrato-atividade
#a v1, usa apeans um usuario 
#no saque, deve permitor no maximo 3 saques-diarios, o limite eh de 500.00
#o extrato, deve listar todos as operaçoes eo valor atual do extrato 

saldo=0
limite=500
numeros_saques=0
#constante
LIMITE_SAQUES=3
print("--"*100)

print("Bem vindo ao Cyber Bank")
print("para operaçoes, usa: d para deposito, e para extrato, s para saque, q para sair")
#menu =""
while True:
   opcao=input('insira o comando: ')
   if opcao == "d":
     print('deposito')
     print(f'seu saldo inicial: {saldo}')
     deposito = float(input('insira o valor:'))
     saldo+=deposito
     print(f'seu saldo atual é de: {saldo}')
     if deposito < 0:
        print("saldo negativo, tente novamente")
   elif opcao == "e":
    print("extrato")
   elif opcao == "s":
    print("saque")
    if numeros_saques < LIMITE_SAQUES:
        saque = float(input('insira o valor:'))
        saldo-=saque
        print(f'seu saldo atual é de: {saldo}')
        if saque > saldo:
            print("saldo negativo, tente novamente")
        elif saque < saldo:
            numeros_saques+=1
        elif saque<0:
            print("saldo negativo, tente novamente")
        else:
            numeros_saques+=1
    elif numeros_saques == LIMITE_SAQUES:
        print("limite de saques atingido")
    elif saldo < limite:
        saque = float(input('insira o valor:'))
        saldo-=saque
        print(f'seu saldo atual é de: {saldo}')
    elif saldo == limite:
        print("nao é mais possível sacar, pode zerar sua conta!")
    
   elif opcao == "q":
    print("saindo...")
    break
   else:
    print("comando inválido! Tente novamento :(")
    