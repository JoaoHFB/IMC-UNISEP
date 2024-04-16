"""
    solicite para o usuario imprimir
    - nome
    -altura(cm)
    -peso(kg)
    com base nestes dados realize o calculo para descobrir qual o imc (indice de massa corporea) da pessoa
    Para calcular utilize a tabela padrão di IMC
    Abaixo de 18,5 - Abaixo o peso (pegue suplementos do cariani)
    entre 18,5 e 24,9 - peso ideal (Para Bens)
    entre 25,0 e 29,9 - obesidade grau 1
    entre 35,0 e 39,9 - obesidaed grau 2
    acima de 40,0 - Obesidade grau 3 (Dr. Nowzaradan te espera)
    formula = IMC = peso / altura^2
"""
nome = input("Digite o nome do usuario: ")
altura = float(input("Digite a altura do usuario em (cm): "))
peso = float(input("Digite o peso do usuario em (kg): "))
altura_m = altura / 100

if peso <= 18.5:
    print("abaixo do peso")
elif peso >= 18.5 and peso <= 24.9:
    print("Peso ideal")
elif peso >= 25.0 and peso <= 29.9:
    print("obesidade grau 1")
elif peso >= 35.0 and peso <= 39.9:
    print("obesidade grau 2")
else:
    peso >= 40.0
    print("obesidade grau 4")

imc = peso / (altura_m ** 2)

texto = f"""Se {nome} estiver pesando {peso}kg ele esta:
se a altura de {nome} for {altura_m}cm e seu peso for {peso}kg o seu imc sera: {imc:.3f}
"""
print(texto)