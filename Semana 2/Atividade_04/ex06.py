def calcular_volume(medidas):
    v = (medidas['comprimento'] * medidas['altura'] * medidas['largura']) / 1000
    return v

def calcular_potencia_termostato(volume, t_desejada, t_ambiente):
    return volume * 0.05 * (t_desejada - t_ambiente)

def calcular_filtragem(volume):
    minimo = 2 * volume
    maximo = 3 * volume
    return minimo, maximo

# Entrada
dados_aquario = {
    'comprimento': float(input("Comprimento (cm): ")),
    'altura': float(input("Altura (cm): ")),
    'largura': float(input("Largura (cm): "))
}
temp_amb = float(input("Temperatura ambiente (°C): "))
temp_des = float(input("Temperatura desejada (°C): "))

# Processamento
vol = calcular_volume(dados_aquario)
potencia = calcular_potencia_termostato(vol, temp_des, temp_amb)
filt_min, filt_max = calcular_filtragem(vol)

# Saída
print(f"\n--- Resultados ---")
print(f"Volume do aquário: {vol:.2f} Litros")
print(f"Potência do termostato: {potencia:.2f} W")
print(f"Filtragem necessária: entre {filt_min:.1f} e {filt_max:.1f} Litros/hora")