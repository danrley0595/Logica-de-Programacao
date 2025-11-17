#nome = str(input('Informe seu nome:'))
#idade = int(input('Qual a sua idade:'))
 
#if idade >= 18:
#    print(f'{nome} você é maior de idade!')

#else:
#    print(f'{nome} você é menor de idade!')


#nota = float(input('Digite sua nota:'))

#if nota == 10:
#    print(f'Nota Máxima! Parabéns {nome}!')
#elif nota >=7:
#    print(f'{nome} você foi aprovado!')
#elif nota >=5:
#    print(f'{nome} você está de recuperação!')
#else:
#    print(f'{nome} você foi reprovado!')

nome = str(input('Informe seu nome:'))
peso = float(input('Digite seu peso:'))
altura = float(input('Digite sua altura:'))
imc = float(peso / (altura * altura) )

if imc > 40:
    print(f'{nome} Seu IMC é {imc} Sua classificão é Obesidade Morbida grau 3')
elif imc >=35.0:
    print(f'{nome} Seu IMC é {imc} Sua classificão é Obesidade Severa grau 2')
elif imc >=30.0:
    print(f'{nome} Seu IMC é {imc} Sua classificão é Obesidade Severa grau 1')
elif imc >=25.0:
    print(f'{nome} Seu IMC é {imc} Sua classificão é Sobrepeso')
elif imc >=18.5:
    print(f'{nome} Seu IMC é {imc} Sua classificão é Saudável')
else:
    print(f'{nome} Seu IMC é {imc} Sua classificão é magreza')
