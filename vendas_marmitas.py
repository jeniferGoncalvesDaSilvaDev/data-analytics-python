import numpy as np 
import matplotlib.pyplot as plt 
#vendas de marmitas de uma empresa durante janeiro até setembro
meses = [1,2,3,4,5,6,7,8,9]
vendas_marmitas =[22,56,45,34,30,33,40,56,32]
#grafico de linhas
plt.plot(meses,vendas_marmitas, color='black',linestyle='dashed', label = 'vendas de marmitas')
#titulo do grafico
plt.title('vendas de marmitas')
#eixo x 
plt.xlabel('meses')
#eixo y
plt.ylabel('número de marmitas')
plt.show()
#legenda 
#media de vendas nesse periodo 
media= np.mean(vendas_marmitas)
plt.legend(media)
