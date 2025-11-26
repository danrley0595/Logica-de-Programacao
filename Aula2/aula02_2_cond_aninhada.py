passou_de_ano = str(input('Você passou de ano? (sim/não):')).strip().lower()
passou_no_vestibular = str(input('Você passou no vestibular? (sim/não):')).strip().lower()

if passou_de_ano == 'sim':
    if passou_no_vestibular == 'sim':
        print('Começarei a faculdade no próximo ano.')
    else:
        print('Vou precisar tentar o vestibular novamente.')
else:
    print('Preciso estudar mais para passar de ano.')