import matplotlib.pyplot as plt
#subplots
x =[2,4,6,8]
y =[4,8,12,16]
#subplot
#34 de largura e 20 de altura em polegadas
figura = plt.figure(figsize=(3,5))
#titulo do subplot
figura.suptitle('titulo geral')
figura.suptitle("outro grafico")
#criar quadrantes
#os parametros do figura.add_subplot, é o numero de linhas, número de colunas e a posição do grafico
figura.add_subplot(131)
figura.add_subplot(133)
plt.plot(x,y, label = "dados")
plt.scatter(x,y,label = "dispersão de dados")
plt.title("dispersão de valores")
plt.title("y = 2x")
plt.xlabel("valores de x")
plt.ylabel("valores de y")
plt.legend()
plt.show()

#salvando
plt.savefig('graficos png')