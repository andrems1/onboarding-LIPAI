def soma_tupla(numeros):
    soma = 0
    for num in numeros:
        soma += num
    return soma

valores = (5, 10, 15)
print(f"Soma da tupla: {soma_tupla(valores)}")