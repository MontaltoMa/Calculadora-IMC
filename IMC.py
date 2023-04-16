peso = float(input('Digite seu peso em Kg: '))
altura = float(input('Digite sua altura em metros: '))

if altura == 0:
    print('Erro, altura não pode ser zero.')
else:
    imc = peso / altura ** 2
    if imc <= 18.5:
        print(f'Seu imc é {imc:.2f}, você está abaixo do peso ideal. ')
    elif imc <= 24.9:
        print(f'Seu imc é {imc:.2f}, você está no peso ideal.')
    elif imc <= 29.9:
        print(f'Seu imc é {imc:.2f}, você está acima do peso.')
    elif imc <= 34.9:
        print(f'Seu imc é {imc:.2f}, você está com obesidade grau 1.')
    elif imc <= 39.9:
        print(f'Seu imc é {imc:.2f}, você esta com obesidade grau 2 (severa).')
    else:
        print(f'Seu imc é {imc:.2f}, você esta com obesidade grau 3 (mórbida).')
