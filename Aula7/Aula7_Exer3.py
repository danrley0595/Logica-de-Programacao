nomes = ["Maria","João","Matheus","Monica","Renata","Edivaldo"]

pos = int(input("Informe a posição que deseja deletar o nome:"))

del nomes[pos]
#nomes.pop(pos)  instrução para deletar um item da lista pelo indice

print(nomes)