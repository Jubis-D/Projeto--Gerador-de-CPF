import random

for _ in range(10):
    nove_digitos = ''
    for i in range(9):
        nove_digitos += str(random.randint(0, 9))

    contador_regressivo1 = 10
    resultado_1 = 0

    for digito in nove_digitos:
        resultado_1 += int(digito) * contador_regressivo1
        contador_regressivo1 -=1
    digito1 = (resultado_1 * 10) % 11
    digito1 = digito1 if digito1 <= 9 else 0

    dez_digitos = nove_digitos + str(digito1)
    contador_regressivo2 = 11
    resultado_2 = 0

    for digito in dez_digitos:
        resultado_2 += int(digito) * contador_regressivo2
        contador_regressivo2 -=1
    digito2 = ((resultado_2 * 10) % 11)
    digito2 = digito2 if digito2 <= 9 else 0

    cpf_definitivo = f'{nove_digitos}{digito1}{digito2}'

    print(cpf_definitivo)
