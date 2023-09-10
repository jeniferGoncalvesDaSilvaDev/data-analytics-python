#soma de lucros diários, sendo cartão, dinheiro ou pix 
valor_dinheiro=0.0
valor_cartao=0.0
valor_pix=0.0
def main():
  while True:
  	print("Digite as opções de pagamento")
  	print("1 para dinheiro")
  	print('2 para cartão')
  	print("3 para pix")
  	print("4 para sair")
  	pagamento=int(input('Digite sua forma de pagamento: '))
  	if pagamento==1:
  		lucro_dinheiro()
  	elif pagamento==2:
  		lucro_cartao()
  	elif pagamento==3:
  		lucro_pix()
  	elif pagamento==4:
  		print("Saindo...")
  		break 
  	else:
  		print("Comando inválido!")
  	
  
#pagamento no dinheiro	
def lucro_dinheiro():
	while True:
		dinheiro=float(input("Insira o valor:  "))
		print("s para sim")
		print("n para não")
		continuar=str(input("Deseja continuar? s/n: "))
		if continuar=='s':
			global valor_dinheiro
			valor_dinheiro+=dinheiro
			print(f'Lucro do dinheiro: {valor_dinheiro}')
		elif continuar=='n':
			print('Saindo...')
			valor_dinheiro+=dinheiro
			print(f'Lucro do dinheiro: {valor_dinheiro}')
			break 
			
		
#pagamento no cartão
def lucro_cartao():
	while True:
		cartao=float(input("Insira o valor: "))
		print("s para sim ")
		print("n para não")
		continuar=str(input("Deseja continuar: s/n:  "))
		if continuar=='s':
			global valor_cartao
			valor_cartao+=cartao
			print(f'Lucro do cartão: {valor_cartao}')
		elif continuar=='n':
			print("Saindo...")
			valor_cartao+=cartao
			print(f'Lucro do cartão: {valor_cartao}')
			break 
			
#pagamento no pix 
def lucro_pix():
	while True:
		pix=float(input("Insira o valor: "))
		print("s para sim ")
		print("n para não")
		continuar=str(input("Deseja continuar: s/n:  "))
		if continuar=='s':
		    global valor_pix 
		    valor_pix+=pix
		    print(f'Lucro do pix: {valor_pix}')
		elif continuar=='n':
			print("Saindo...")
			valor_pix+=pix
			print(f'Lucro do pix: {valor_pix}')
			break 
		
				
				
	
#chamando a função main()
main()	
