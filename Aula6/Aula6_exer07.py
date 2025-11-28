 # num 1 e num 2 iniciando com 1, pois não é um número par, assim irá entrar no loop para verificação de número par, se iniciasse com 0 não entraria no laço para solicitar os valores e fazer a verificação

num1 = int(1) 
num2 = int(1)

while num1 % 2 == 1:
    num1 = int(input("Digite o primeiro número interio par:"))
    if num1 % 2 == 1:
        print("Número não é par, digite novamente")
    
while num2 % 2 == 1:
    num2 = int(input("Digite o segundo número interio par:"))
    if num2 % 2 == 1:
        print("Número não é par, digite novamente")
    
soma = num1 + num2
media = soma / 2

print(f"A soma dos números é: {soma} e média dos números é: {media}")
