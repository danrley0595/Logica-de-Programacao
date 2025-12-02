quant_itens = int(0)
valor_compra = float(0)
valor_prod = float(input("Digite o valor do produto:"))

while valor_prod != 0:
    quant_itens = quant_itens + 1
    valor_compra += valor_prod
    valor_prod = [float(input("Digite o valor do produto:"))]

print(f"\nQuantidade de itens: {quant_itens}\nValor Final da Compra:R$ {valor_compra}")
print("Forma de pagamento disponivel: ")
if valor_compra > 200.0:
    print("Cartão de crédito parcelado em até 3 vezes")
elif valor_compra > 100.0:
    print("Cartão de crédito parcelado em até 2 vezes")
elif valor_compra >= 50.0:
    print("Cartão de crédito à vista")
else:
    print("Cartão de Débito ou Pix")