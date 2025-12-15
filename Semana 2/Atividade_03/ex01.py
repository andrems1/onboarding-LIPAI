lista_numeros = []

print("Digite 3 números:")
for i in range(3):
    num = int(input(f"Número {i+1}: "))
    lista_numeros.append(num)

print(f"Lista digitada: {lista_numeros}")
print(f"Maior valor: {max(lista_numeros)}")
print(f"Menor valor: {min(lista_numeros)}")