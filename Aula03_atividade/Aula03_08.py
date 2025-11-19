peso = float(input('Digite seu peso:'))
altura = float(input('Digite sua altura:'))
imc = round(peso / (altura * altura),2)

if imc > 25.0:
    print(f'Seu IMC é {imc}. Acima do peso.')
elif imc >=18.5:
    print(f'Seu IMC é {imc}. Peso normal.')
else:
    print(f'Seu IMC é {imc}. Abaixo do peso. ')
