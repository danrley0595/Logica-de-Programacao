lista = []
print("Digite 5 Números")
for i in range(0,5,1):
    n = int(input(f"Número {i+1}:"))
    lista.append(n)

lista.sort()
print(lista)
