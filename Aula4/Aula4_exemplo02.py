senha_correta = "python123"

tentativa = input("Digite a senha:")

while tentativa != senha_correta:
    print("Senha Incorreta. Tenta novamente.")
    tentativa = input("Digite a senha:")

print("Acesso Liberado.")
