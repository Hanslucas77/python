nome=str(input('digite seu 1 nome:'))

if len(nome) <=4:
    print('nome curto')
elif len(nome) >= 5 and len(nome) == 6:
    print('seu nome é medio')
elif len(nome) > 6:
    print('seu nome é longo')
else: 
    print('não são letras')
