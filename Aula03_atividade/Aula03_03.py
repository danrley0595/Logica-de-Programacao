n1 = float(input("Digite a primeira nota:"))
n2 = float(input("Digite a segunda nota:"))
n3 = float(input("Digite a terceira nota:"))
n4 = float(input("Digite a quarta nota:"))

media = (n1 + n2 + n3 + n4) / 4

if media >= 6.0:
    print(f"Você foi aprovado na disciplina, a média foi de {media}")
elif media >= 5.0:
    print(f"Você ficou de recuperação na disciplina, a média foi de {media}")
else:
     print(f"Você foi reprovado na disciplina, a média foi de {media}")