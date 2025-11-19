valor_compra = float(input("Informe o valor da compra:"))

if valor_compra >= 200.0:
    if valor_compra >= 500.0:
        print("Você ganhou frete grátis e um brinde!")
    else:
        print("Você ganhou frete grátis!")
else:
    if valor_compra <= 50:
        print("O valor do frete é de R$20")
    else:
        print("O valor do frete é de R$10")

