peso = float(input("Digite seu peso em kg (ex: 70): ").replace(",", "."))
altura = float(input("Digite sua altura em metros (ex: 1.75): ").replace(",", "."))

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
