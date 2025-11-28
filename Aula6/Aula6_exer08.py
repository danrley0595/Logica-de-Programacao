num = int(input("Digite um número inteiro:"))

if num % 2 == 0:
    result_paridade = "Par"
else:
    result_paridade = "Ímpar"
    
if num > 0:
    result = "Positivo"
elif num < 0:
    result = "Negativo"
else:
    result = "Zero"

print(f"O número {num} é {result_paridade} e {result}.")
