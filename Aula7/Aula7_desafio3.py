lista = []

while True:
    produto = input("Digite o nome de um produto ou 0 pra sair:")
    if produto != "0":
        lista.append(produto)
    else:
        break;

lista.sort()
print(f"Lista de Compras: {lista}")