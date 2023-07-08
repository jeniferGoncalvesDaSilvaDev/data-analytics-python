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
     print(f'seu saldo inicial: R$ {saldo:.2f}\n')
     deposito = float(input('insira o valor:'))
     saldo+=deposito
     extrato = print(f'seu saldo atual é de: R$ {saldo:.2f}\n')
     if deposito < 0:
        print("saldo negativo, tente novamente")
        break
   elif opcao == "e":
    print("--"*100)
    print("extrato")
    print("--"*100)
    
    if saldo ==0:
        print(f'seu saldo inicial: R$ {saldo:.2f}\n')
        print("nenhum movimento")
    else:
        extrato = print(f'seu saldo inicial é de: R$ {saldo:.2f}\n')
        extrato = print(f'seu saldo atual é de: R$ {saldo:.2f}\n')
   elif opcao == "s":
    print("saque")
    if numeros_saques < LIMITE_SAQUES:
        saque = float(input('insira o valor:'))
        limite_saque= saque > limite 
        saldo-=saque
        extrato=print(f'seu saque atual é de: R$ {saque:.2f}\n')
        extrato=print(f'seu saldo atual é de: R$ {saldo:.2f}\n')
        numeros_saques+=1
        if saque < 0:
            print('saque negativo')
            break
        elif saque > saldo:
            print('saldo insuficiente')
            break
    elif numeros_saques == LIMITE_SAQUES:
        print("limite atingido de saques diários!")
    elif limite_saque:
        print('limite de R$ 500.00 atingido')
    else:
        saldo-=saldo
        extrato=print(f'seu saldo atual é de: R$ {saldo:.2f}\n')
        extrato=print(f'seu saque atual é de: R$ {saque:.2f}\n')
        numeros_saques+=1
   elif opcao == "q":
    print("saindo...")
    break
   else:
    print("comando inválido! Tente novamento :(")
    