def calcular_imc(individuo):
    """Retorna o IMC de um indivíduo com base na sua altura e peso."""
    peso = individuo['peso']
    altura = individuo['altura']
    return peso / (altura * altura)

def obter_classificacao(imc):
    """Retorna a classificação com base no IMC."""
    if imc < 18.5:
        return "Baixo peso"
    elif 18.5 <= imc <= 24.9:
        return "Peso normal"
    elif 25.0 <= imc <= 29.9:
        return "Excesso de peso"
    elif 30.0 <= imc <= 34.9:
        return "Obesidade de Classe 1"
    elif 35.0 <= imc <= 39.9:
        return "Obesidade de Classe 2"
    else:
        return "Obesidade de Classe 3"

def situacao_individuo(imc):
    """Retorna a situação ('normal', 'perder peso', 'ganhar peso')."""
    if 18.5 <= imc <= 24.9:
        return "Normal"
    elif imc < 18.5:
        return "Ganhar peso"
    else:
        return "Perder peso"

# Programa principal
p = float(input("Digite o peso (kg): "))
a = float(input("Digite a altura (m): "))

pessoa = {'peso': p, 'altura': a}

imc_calc = calcular_imc(pessoa)
classificacao = obter_classificacao(imc_calc)
situacao = situacao_individuo(imc_calc)

print(f"\nIMC: {imc_calc:.2f}")
print(f"Classificação: {classificacao}")
print(f"Recomendação: {situacao}")