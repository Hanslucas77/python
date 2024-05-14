horario = int(input('Digite a hora em inteiros: '))

if 0 <= horario <= 11:
    print('Bom dia!')
elif 12 <= horario <= 17:
    print('Boa tarde!')
elif 18 <= horario <= 23:
    print('Boa noite!')
else:
    print('Hora inválida!')
