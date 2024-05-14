while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')

    numeros_validos = None

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except ValueError:
        numeros_validos = False

    if not numeros_validos:
        print('Um ou ambos os números digitados são inválidos.')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos or len(operador) > 1:
        print('Operador inválido.')
        continue

    if operador == '/' and num_2_float == 0:
        print('Divisão por zero não é permitida.')
        continue

    resultado = None
    if operador == '+':
        resultado = num_1_float + num_2_float
    elif operador == '-':
        resultado = num_1_float - num_2_float
    elif operador == '*':
        resultado = num_1_float * num_2_float
    elif operador == '/':
        resultado = num_1_float / num_2_float

    print(f'O resultado é: {resultado}')

    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair:
        break
