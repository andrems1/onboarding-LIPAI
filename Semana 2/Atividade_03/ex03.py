meses_dict = {
    1: "Janeiro", 2: "Fevereiro", 3: "Março", 4: "Abril",
    5: "Maio", 6: "Junho", 7: "Julho", 8: "Agosto",
    9: "Setembro", 10: "Outubro", 11: "Novembro", 12: "Dezembro"
}

num_mes = int(input("Digite o número do mês (1-12): "))

resultado = meses_dict.get(num_mes, "Mês inválido")
print(f"O mês é: {resultado}")