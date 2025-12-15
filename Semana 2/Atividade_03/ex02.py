meses = (
    "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
)

num_mes = int(input("Digite o número do mês (1-12): "))

if 1 <= num_mes <= 12:
    print(f"O mês é: {meses[num_mes - 1]}")
else:
    print("Número inválido! Digite entre 1 e 12.")