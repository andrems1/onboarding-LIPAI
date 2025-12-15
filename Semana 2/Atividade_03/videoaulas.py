# listas
frutas = ["Maçã", "Banana", "Uva"]
print(frutas)

# add elemento
frutas.append("Laranja")
print(frutas)

print(f"Primeira fruta: {frutas[0]}")
print(f"Última fruta: {frutas[-1]}")

frutas[1] = "Morango"
print(frutas)

#--------------------------------------

# Tuplas
dimensoes = (1920, 1080)
print(f"Largura: {dimensoes[0]}")
print(f"Altura: {dimensoes[1]}")

# Tentativa de alteração gera erro
# dimensoes[0] = 1280  # TypeError

# Desempacotamento
largura, altura = dimensoes
print(f"Resolução: {largura}x{altura}")

#--------------------------------------

# sets 
numeros = {1, 2, 3, 3, 4, 2}
print(numeros)  

# Operações de conjunto
a = {1, 2, 3}
b = {3, 4, 5}

print(f"União: {a.union(b)}")
print(f"Interseção: {a.intersection(b)}")

#--------------------------------------

# Dicionários
usuario = {
    "nome": "André",
    "idade": 23,
    "cidade": "Uberlândia"
}

print(usuario["nome"])

# add novo campo
usuario["profissao"] = "Dev"
print(usuario)

print(usuario.keys())
print(usuario.values())