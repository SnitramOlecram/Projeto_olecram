import os
os.system ("cls")

print("====== Calculadora de IMC ======")
print("")

print("=== OBS: VALORES SÓ SE APLICA A PESSOAS QUE NÃO PRATICA MUSCULAÇÃO ===")
print("")

peso = float(input("Digite seu peso em kg (ex: 00.00): ").replace(",", "."))
altura = float(input("Digite sua altura em metros (ex: 0.00): ").replace(",", "."))

imc = peso / (altura ** 2)

print(f"Seu IMC é: {imc:.2f}")

if imc < 18.5:
    print("Classificação: Abaixo do peso")
elif imc < 25:
    print("Classificação: Peso normal")
elif imc < 30:
    print("Classificação: Sobrepeso")
else:
    print("Classificação: Obesidade")
