start = int(input("Digite um número interior que será  start(Iniciar):"))
stop = int(input("Digite número interior que será stop(Parada):"))
step = int(input("Digite número interior que será o step(Intervalo):"))
i = int(start)
soma = int(0)

for i in range(start,stop,step):
    print(i, end=" ")
    soma += i

print(f"\nTotal da soma dos números entre o internado: {soma}")