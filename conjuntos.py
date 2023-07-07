#estrutura de dados set
#criar conjuntos
#coleçao de objetos, com elementos UNICOS, eh usado para representar sequencias numericas, ou eleiminar itens iterveis de um loop
#set espera um objeto iteravel
#set nao garante a ordem de objetos
#para usar o set, pode ser set(obj) ou {}
#nao suportam indexaçao ou fatiamento, tem que converter para lista, usando list(), podendo percorrer com loop-iteraçao
#pode percorrer um set com for
#para saber o indice do set, usa-se o enumerate()
numeros=set([1,2,3,4,1,2,3])
fruta=set("abacaxi")
carros=set(('mitsubish','honda','hyundai','honda'))
#percorrendo um set com for 
for carro in carros:
    print(carro)
#percorrendo com for e enumerate()
for indice, carro in enumerate(carros):
    print(indice, carro)
print(carros)
print(fruta)

print(numeros)
linguagens={"python","javascript","lua","c#","c++","python"}
for lingua in linguagens:
    print(lingua)

print(linguagens)


nomes={"jey","jen","mika","kuro","lawly","oliver"}
#convertendo para lista
nomes= list(nomes)
print(nomes)
#percorrer com for
for nome in nomes:
    print(nome)
#metodos do set 
#union()
#junta dois conjuntos
matrix= {"neo", "trinity"}
ghost_in_the_shell={"Major","Batou"}
juntar=matrix.union(ghost_in_the_shell)
print(matrix)
print(ghost_in_the_shell)
print(juntar)
#interseccçao
#intersection()
#juntar elementos iguais a dois ou mais conjuntos
jogos={"tekken","cyberpunk 2077","final fight"}
animes= {"death note","cyberpunk 2077","naruto"}
cyber_anime = animes.intersection(jogos)

print(animes)
print(jogos)
print(cyber_anime)

#difference()

jogos={"tekken","cyberpunk 2077","final fight"}
animes= {"death note","cyberpunk 2077","naruto"}
anime_luta = animes.difference(jogos)
jogos_luta= jogos.difference(animes)

print(anime_luta)

print(jogos_luta)
#symetric_difference()

jogos={"tekken","cyberpunk 2077","final fight"}
animes= {"death note","cyberpunk 2077","naruto"}
anime_luta = animes.symmetric_difference(jogos)


print(anime_luta)

#isubset ()-retorna True ou False

jogos={"tekken","cyberpunk 2077","final fight","naruto","devil may cry"}
animes= {"death note","cyberpunk 2077","naruto","devil may cry"}
anime_luta = animes.issubset(jogos)
jogos_luta= jogos.issubset(animes)
print(anime_luta)

print(jogos_luta)
#isdijoint()-alteraçao de disjuntos-nao ha intersecçao
#retorna True se nao ha intersecçao
#retorna False se  ha intersecçao
personagens_jey={"kuro", "bruno","lawly", "ollie","math"}
personajens_death_note={"kira","L", "near","mello","misa","ryuuk","rem"}
personagens_naruto={"naruto","sasuke","sakura","kakashi"}

print(personagens_jey.isdisjoint(personajens_death_note))   

print(personagens_jey.isdisjoint(personagens_naruto))
#add 
#passa um elemento que nao existe no conjunto
alice= personagens_jey.add("alice")

#clear ()
#limpar o set 
#cop 
#copia o set 
#discard 
#discarta um valor no set 
print(personagens_jey.discard("bruno"))