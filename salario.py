#salario.py 
"""
    quero verificar em qual faixa de contribuicao do inss o salario informado se enquadra.
    de 0.00 até 1.412,00 - 7,5%
    de 1.412,01 até 2.666,68 - 9,0%
    de 2.666,69 até 4.000,03 - 12,0%
    de 4.000 até 7.786,02 - 14,0%
    acima de 7.786,03 - R$908,85
"""
""""
salario = 2000.00

if salario <= 1412.00:
    aliquota = 7.5
else:
    if salario >= 1412.01 and salario <= 2666.68:
        aliquota = 9
    else:
        if salario >= 2666.69 and salario <= 4000.03:
            ailquota = 12
        else:
            if salario >= 4000.04 and salario <= 7786.02:
                aliquota = 14
            else:
                valor = 908.65
print('O salario eh...')
"""
salario = float(input("Digite o salario bruto: "))
nome = input("Digite o nome do funcionario: ")
if salario <= 1421.00:
    aliquota = 7.5
elif salario >= 1412.01 and salario <= 2666.68:
    aliquota = 9
elif salario >= 2666.69 and salario <= 4000.02:
    aliquota = 12
elif salario >= 4000.02 and salario <= 7786.02:
    aliquota = 14
else:
    valor = 908.85

if aliquota != 0:
    valor = salario * aliquota / 100

texto = f"""O salario do funcionario {nome} é: {salario:.2f}\n eles está na aliquota de {aliquota}% 
Deve pagar de inss os valor de R${valor} 
Recebera o valor de R$ {salario - valor}"
"""
print(texto)




























