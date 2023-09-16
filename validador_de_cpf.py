import sys


def validador_cpf(cpf):
    cpf = str(cpf)

    primeiro_digito = cpf[0]
    primeiro_digito_sequencial = primeiro_digito * len(cpf)

    if cpf == primeiro_digito_sequencial:
        print('CPF inválido. Motivo: Sequencial')
        sys.exit()

    if len(cpf) > 11:
        print('CPF inválido')
        sys.exit()

    numero_convertido = []

    for digito in cpf:
        try:
            digito_int = int(digito)
            numero_convertido.append(digito_int)

        except ValueError:
            print('Por favor, digite apenas dígitos')
            sys.exit()

    ultimo_digito = numero_convertido.pop()
    penultimo_digito = numero_convertido.pop()

    resultado1 = 0
    contador1 = 10
    for n in numero_convertido:
        num_peso = n * contador1
        resultado1 += num_peso
        contador1 -= 1

    resultado1 *= 10
    resultado1 = resultado1 % 11

    if resultado1 > 9:
        resultado1 = 0

    numero_convertido.append(resultado1)

    resultado2 = 0
    contador2 = 11
    for n in numero_convertido:
        num_peso = n * contador2
        resultado2 += num_peso
        contador2 -= 1

    resultado2 *= 10
    resultado2 = resultado2 % 11

    if resultado2 > 9:
        resultado2 = 0

    if resultado1 == penultimo_digito and resultado2 == ultimo_digito:
        print(f'CPF válido. O seu CPF é {cpf}')
        return True
    else:
        print('CPF inválido')
        return False
