numero_inteiro = input('Digite um número inteiro: ')

if numero_inteiro.isdigit():
    numero_inteiro = int(numero_inteiro)  # Convertendo a entrada para inteiro
    resto = numero_inteiro % 2
    if resto == 0:
        print(f'O número {numero_inteiro} é par.')
    else:
        print(f'O número {numero_inteiro} é ímpar.')
else:
    print(f'O valor "{numero_inteiro}" não é um número inteiro válido.')





    