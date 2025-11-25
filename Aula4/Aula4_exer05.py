soma = int(0)
i = int(0)


idade = int(input("Digite uma idade ou 0 para sair:"))

while idade != 0:
    soma += idade
    i = i + 1
    idade = int(input("Digite outra idade ou 0 para sair:"))

if i > 0:
    media = int(soma / i )
    print(f"Media de idade:{media}")
    
else:
    print("Idades não informadas!")
