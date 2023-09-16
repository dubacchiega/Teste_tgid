import sys


def validador_cnpj(cnpj):
    cnpj = str(cnpj)
    primeiro_digito = cnpj[0]
    primeiro_digito_sequencial = primeiro_digito * len(cnpj)

    if cnpj == primeiro_digito_sequencial:
        print('CNPJ inválido. Motivo: Sequencial')
        sys.exit()

    if len(cnpj) > 14:
        print('CNPJ inválido')
        sys.exit()

    numero_convertido = []

    for digito in cnpj:
        try:
            digito_int = int(digito)
            numero_convertido.append(digito_int)

        except ValueError:
            print('Por favor, digite apenas dígitos')
            sys.exit()

    quatro_digitos = numero_convertido[:4]
    oito_digitos = numero_convertido[4:12]

    contador_primeira_parte = 5
    contador_segunda_parte = 9
    soma = 0

    for n in quatro_digitos:
        numero_peso = n * contador_primeira_parte
        soma += numero_peso
        contador_primeira_parte -= 1

    for n2 in oito_digitos:
        numero_peso2 = n2 * contador_segunda_parte
        soma += numero_peso2
        contador_segunda_parte -= 1

    resto_divisao = soma % 11

    if resto_divisao < 2:
        resultado1 = 0
    else:
        resultado1 = 11 - resto_divisao

    cinco_digitos = numero_convertido[:5]
    oito_digitos2 = numero_convertido[5:13]

    contador_primeira_parte2 = 6
    contador_segunda_parte2 = 9
    soma2 = 0

    for num in cinco_digitos:
        numero_peso22 = num * contador_primeira_parte2
        soma2 += numero_peso22
        contador_primeira_parte2 -= 1

    for num2 in oito_digitos2:
        numero_peso23 = num2 * contador_segunda_parte2
        soma2 += numero_peso23
        contador_segunda_parte2 -= 1

    resto_divisao2 = soma2 % 11

    if resto_divisao2 < 2:
        resultado2 = 0

    else:
        resultado2 = 11 - resto_divisao2

    entrada_invertida = numero_convertido[::-1]

    if resultado1 == entrada_invertida[1] and resultado2 == entrada_invertida[0]:
        print(f'CNPJ válido. Seu CNPJ é: {cnpj}')
        return True
    else:
        print('CNPJ inválido')
        return False
