frutas = []
fruta = str(input("Informe uma Fruta para adicionar na lista ou 0 pra sair:"))
pos = int(input("Informe a posição que deseja inserir na lista ou 0 pra sair:"))
frutas.insert(pos,fruta)

incluir = input("Deseja incluir mais um item na lista? S ou N")

if incluir == "S":
    while True:
        fruta = str(input("Informe uma Fruta para adicionar na lista ou 0 pra sair:"))
        pos = int(input("Informe a posição que deseja inserir na lista:"))
        if fruta != "0":
            frutas.insert(pos,fruta)
        else:
            break;
print(frutas)