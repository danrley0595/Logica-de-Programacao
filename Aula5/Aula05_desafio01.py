start = int(input("Digite um número interior que será  start(Iniciar):"))
stop = int(input("Digite número interior que será stop(Parada):"))
step = int(input("Digite número interior que será o step(Intervalo):"))
i = int(start)
#step = intervalo qie acrescido ou diminuido, se positivo = crescente, se negativo = descrescente, exemplo 1, -1

print("\nNúmeros pares entre o intervalo:\n")
for i in range(start, stop, step):
    if i % 2 == 0:
        print(i, end=", ")
print("\n")        

print("Números impares entre o intervalo\n")
for i in range(start, stop, step):
    if i % 2 == 1:
        print(i, end=", ")
        
