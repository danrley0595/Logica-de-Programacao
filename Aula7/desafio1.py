frutas = ["Maça", "Banana", "Uva","Morango","Laranja"]
frutas.sort()

print(frutas[0])

frutas[1] = "Tamarindo"

print(frutas)

frutas = ["Maça", "Banana", "Uva","Morango","Laranja"]

# append inclui o item no final da lista
frutas.append("Melão")
frutas.append("Abacaxi")
print(frutas)

#insert insere o item na posição informada
frutas.insert(0, "Amora")
frutas.insert(5, "Abacate")
print(frutas)

#remove pelo valor
frutas.remove("Banana")
print(frutas)

#remove pela posição
del frutas[0]
print(frutas)

maior_fruta = max(frutas)
print(maior_fruta)

numeros = [1,5,25,15,50,100,75]
numero_maior = max(numeros)
print(numero_maior)

# ou

print(f"{min(numeros)}")
