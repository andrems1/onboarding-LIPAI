# comentário
print("Olá, mundo!")

"""
comentário 
de 
múltiplas 
linhas
"""

#--------------------------------------

# Declaração de variávei
nome_completo = "André"     # String/Texto
idade = 23                  # Inteiro
altura = 1.75               # Ponto Flutuante/Real
esta_estudando = True       # Booleano/Lógico

print("Nome:", nome_completo, "- Tipo:", type(nome_completo))
print("Idade:", idade, "- Tipo:", type(idade))
print("Altura:", altura, "- Tipo:", type(altura))
print("Estudando:", esta_estudando, "- Tipo:", type(esta_estudando))

#--------------------------------------

# A função input lê dados string
valor1_str = input("Digite um número inteiro: ")
valor2_str = input("Digite outro número inteiro: ")

# Conversão de tipos 
valor1 = int(valor1_str)
valor2 = int(valor2_str)

soma = valor1 + valor2

# saída 
print("A soma é:", soma)
print(f"O resultado de {valor1} + {valor2} é igual a {soma}")


