#media aritmética com numpy
import numpy as np 
notas =[5.0,7.5,8.0]
l= len(notas)
print(l)
#mean, faz a soma e calcula a media
media= np.mean(notas)
print(notas)
print(media)
#media aritmética sem numpy
m = sum(notas)/len(notas)
print(m)
#media ponderada
#calcula a soma da nota, vezes seu peso
notas_pesos=[6.0,9.0,10.0]
pesos=[1.0,3.0,2.0]
#calcula para cada posição na lista de notas e pesos, em um for de 0 a até o comprimento da lista de notas
#no for calcula para cada posição de notas e para cada posição da lista de pesos
#na media ponderada, calcula a soma da multiplicação de notas e pesos, dividido pelo número de pesos
sum_notas_pesos=[]
for item in range(0,len(notas)):
    soma=notas_pesos[item] * pesos[item]
    sum_notas_pesos.append(soma)
    
media_ponderada=sum(sum_notas_pesos)/len(pesos)
print(media_ponderada)
#com numpy
media_pond=np.mean(sum_notas_pesos)
print(media_pond)
    