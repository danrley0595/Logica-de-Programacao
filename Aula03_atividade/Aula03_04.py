valor_prod = float(input("Digite o valor do produto:"))

if valor_prod >= 100.0:
    valor_com_desc = valor_prod - (valor_prod * 0.05)
    print(f"Você ganhou desconto de 5%, o valor a ser pago é {valor_com_desc}")
else:
    print(f"O valor a ser pago é {valor_prod}")