print("############ DESAFIO 1 - COFRINHO ############")
meta = float(input("Quanto você quer juntar no cofrinho:"))

valor_total = float(0)

while valor_total <= meta:
    valor_adicionado = float(input("Quanto você quer adicionar:"))
    valor_total += valor_adicionado
    
    if valor_total >= meta:
        print(f"Valor Meta: {meta:.2f} \nValor Total: {valor_total:.2f}")
        alt_meta = str(input("Deseja aumentar o valor da sua meta(s/n)?"))
        if alt_meta == "s":
            meta = float(input("Informe a nova meta do cofrinho:"))
