def saudacao(nome):
    print(f"Olá, {nome}!")

def somar(a, b):
    return a + b

saudacao("André")
resultado = somar(10, 5)
print(f"Resultado da soma: {resultado}")

#--------------------------------------

def exibir_info(nome, idade=18, cidade="Desconhecida"):
    print(f"Nome: {nome}, Idade: {idade}, Cidade: {cidade}")

# Chamada posicional
exibir_info("Maria", 25, "São Paulo")

# Chamada nomeada 
exibir_info(cidade="Rio de Janeiro", nome="João", idade=30)

# valor padrão
exibir_info("Pedro")

#--------------------------------------

# múltiplos argumentos como uma tupla
def somar_todos(*args):
    return sum(args)

print(somar_todos(1, 2, 3, 4, 5))

# múltiplos argumentos nomeados como dicionário
def apresentar_dados(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

apresentar_dados(nome="Ana", curso="Python", nivel="Iniciante")