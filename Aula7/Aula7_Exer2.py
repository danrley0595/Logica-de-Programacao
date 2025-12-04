lista = []

print("Digite 5 Números")
for i in range(0,5,1):
    n = int(input(f"Número {i+1}:"))
    lista.append(n)

max = max(lista)
min = min(lista)
soma = sum(lista)
media = soma / len(lista) # len retorna a quantidade de itens da lista
print(f"Menor Número:{min}")
print(f"Maior Número:{max}")
print(f"Soma:{soma}")
print(f"Média: {media}")
