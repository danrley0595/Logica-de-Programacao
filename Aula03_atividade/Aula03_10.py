velo_carro = int(input("Informe a velocidade do carro:"))
velo_perm = int(80)
print(f"A sua velocidade foi de {velo_carro}km/h.\nVelocidade permitida é de {velo_perm}km/h")     
      
if (velo_carro - velo_perm) > 20:
    print(f"Você cometeu uma infração por dirigir acima da velocidade. \nReceberá 7 pontos na carteira - Infração grave")
elif (velo_carro - velo_perm) >= 11:
    print(f"Você cometeu uma infração por dirigir acima da velocidade.\n Receberá 4 pontos na carteira - Infração média")
elif (velo_carro - velo_perm) > 0:
    print(f"Você cometeu uma infração por dirigir acima da velocidade.\n Receberá 3 pontos na carteira - Infração Leve")
else:
    print(f"Você digiriu dentro do limite.\n Sem multa")
