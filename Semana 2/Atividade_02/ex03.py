codigo = input("Digite o código identificador (ex: BR1234X): ")
valido = True

# Verificações
if len(codigo) != 7:
    valido = False
elif not codigo.startswith("BR"):
    valido = False
elif not codigo.endswith("X"):
    valido = False
else:
    numero_str = codigo[2:6]
    if not numero_str.isdigit():
        valido = False
    else:
        numero = int(numero_str)
        if not (1 <= numero <= 9999):
            valido = False

if valido:
    print("Identificador Válido")
else:
    print("Identificador Inválido")