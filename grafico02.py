import matplotlib.pyplot as plt 
#quando dar plot, e colocar "ro", mostra apenas os pontos no grafico
#label, nome dos dados
#ticks, é escala de x e y
#marker é marcador de pontos em grafico de pontos
#color altera a cor do grafico
x =[1,2,3,5]
y=[56,12,15,17]
#plt.plot mostra graficos em linhas
#plt.plot(x,y, label = 'dados',linestyle='solid',color='red')
#escala de x
plt.xlabel('eixo x')
plt.xticks([0,1,2,3])
plt.ylabel('eixo y')
#escala de y 
plt.yticks([56,12,16,18])
#plt.title é o nome do grafico
plt.title('grafico')
#legenda no grafico, usando a label = dados
plt.legend()
#grafico em barra 
#plt.bar(x,y,color='b')
#grafico de pontos 
plt.scatter(x,y,color='b', marker = 's')
#mostra o grafico na tela
plt.show()
