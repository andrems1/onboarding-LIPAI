codigo = input("Digite o identificador para análise de erros: ")
erros = []

# tamanho
if len(codigo) != 7:
    erros.append("Erro: deve ter exatamente 7 caracteres")

#  início
if not codigo.startswith("BR"):
    erros.append("Erro: não inicia com BR")

#  fim
if not codigo.endswith("X"):
    erros.append("Erro: não finaliza X")

#  parte numérica 
if len(codigo) >= 6:
    numero_str = codigo[2:6] # Pega o meio da string
    numero = int(numero_str)
    if not (1 <= numero <= 9999):
        erros.append("Erro: numero deve estar entre 0001 e 9999")

# Resultado 
if len(erros) == 0:
    print("Identificador Válido!")
else:
    print(f"Foram encontrados {len(erros)} erros:")
    for erro in erros:
        print(erro)