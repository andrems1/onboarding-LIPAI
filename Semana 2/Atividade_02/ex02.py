entrada = input("Digite as notas separadas por vírgula (ex: 10, 5.5, 8): ")

# Separa e converte cada item para float
lista_notas_str = entrada.split(",")
notas = []
soma = 0

for item in lista_notas_str:
    valor = float(item.strip()) 
    notas.append(valor)
    soma += valor

media = soma / len(notas)
print(f"Média calculada: {media:.2f}")

if media > 6.0:
    print("Situação: Aprovado")
elif media >= 4.0: 
    print("Situação: Recuperação")
else:
    print("Situação: Reprovado")