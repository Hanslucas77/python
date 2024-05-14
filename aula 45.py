nome=input ('digite seu nome:')
idade=input('digite sua idade')
if nome and idade:
    print(f'seu nome é, {nome}')
    print(f'seu nome invertido é,{nome[::-1]}')
    print(f'seu nome tem {len(nome)},caracteres')
    print(f'a primeira letra do seu nome é,{nome[0]}')
    print(f'a ultima letra de seu nome é:{nome[9]}')
    if '' in nome:
        print(f'nome tem espaço, {nome}')

    else:
        print(f'seu nome não tem espaços, {nome}')

else:
    print(f'desculpe voce digitou campos vazios')


	
		 
