# Operadores
x = 10
y = 3
print(f"Soma: {x + y}")
print(f"Divisão inteira: {x // y}")
print(f"Resto: {x % y}")
print(f"Potência: {x ** y}")

saldo = 500
saque = 200
cheque_especial = True

pode_sacar = (saldo >= saque) or cheque_especial
print(f"Pode sacar? {pode_sacar}")

# Estrutura if/else
idade = 18
if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")

# for 
for i in range(1, 6):
    print(i)

# Estrutura while com break e continue
print("Contagem com while (pulando o 3 e parando no 5):")
contador = 0
while True:
    contador += 1
    if contador == 3:
        continue  
    if contador > 5:
        break     
    print(contador)