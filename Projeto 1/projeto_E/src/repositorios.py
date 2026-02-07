import os
from models import Sala, Reserva

# Pasta "data" sempre na raiz do projeto (não dentro de src/)
_raiz_projeto = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_pasta_data = os.path.join(_raiz_projeto, "data")
ARQUIVO_SALAS = os.path.join(_pasta_data, "salas.csv")
ARQUIVO_RESERVAS = os.path.join(_pasta_data, "reservas.csv")

# SALAS 
def salvar_sala(sala):
    # Cria a pasta
    os.makedirs(_pasta_data, exist_ok=True)
    with open(ARQUIVO_SALAS, 'a', encoding='utf-8') as f:
        linha = f"{sala.id},{sala.nome},{sala.capacidade},{sala.tipo}\n"
        f.write(linha)

def listar_salas():
    salas = []
    if not os.path.exists(ARQUIVO_SALAS):
        return salas

    with open(ARQUIVO_SALAS, 'r', encoding='utf-8') as f:
        for linha in f:
            linha = linha.strip()
            if not linha: continue
            dados = linha.split(',')
            s = Sala(dados[0], dados[1], dados[2], dados[3])
            salas.append(s)
    return salas

def buscar_sala_por_id(id_busca):
    salas = listar_salas()
    for s in salas:
        if s.id == id_busca:
            return s
    return None

def excluir_sala(id_sala):
    salas = listar_salas()
    salas_atualizadas = [s for s in salas if s.id != id_sala]
    
    if len(salas_atualizadas) == len(salas):
        return False  
    
    os.makedirs(_pasta_data, exist_ok=True)
    with open(ARQUIVO_SALAS, 'w', encoding='utf-8') as f:
        for sala in salas_atualizadas:
            linha = f"{sala.id},{sala.nome},{sala.capacidade},{sala.tipo}\n"
            f.write(linha)
    
    reservas = listar_reservas()
    reservas_atualizadas = [r for r in reservas if r.sala.id != id_sala]
    
    with open(ARQUIVO_RESERVAS, 'w', encoding='utf-8') as f:
        for reserva in reservas_atualizadas:
            linha = f"{reserva.id},{reserva.sala.id},{reserva.responsavel},{reserva.data},{reserva.inicio},{reserva.fim}\n"
            f.write(linha)
    return True

# RESERVAS 
def salvar_reserva(reserva):
    os.makedirs(_pasta_data, exist_ok=True)
    with open(ARQUIVO_RESERVAS, 'a', encoding='utf-8') as f:
        linha = f"{reserva.id},{reserva.sala.id},{reserva.responsavel},{reserva.data},{reserva.inicio},{reserva.fim}\n"
        f.write(linha)

def listar_reservas():
    reservas = []
    if not os.path.exists(ARQUIVO_RESERVAS):
        return reservas

    with open(ARQUIVO_RESERVAS, 'r', encoding='utf-8') as f:
        for linha in f:
            linha = linha.strip()
            if not linha: continue
            
            dados = linha.split(',')
            id_res = dados[0]
            id_sala = dados[1]
            resp = dados[2]
            data = dados[3]
            ini = dados[4]
            fim = dados[5]
            sala_obj = buscar_sala_por_id(id_sala)
        
            if sala_obj:
                r = Reserva(id_res, sala_obj, resp, data, ini, fim)
                reservas.append(r)
    return reservas

def buscar_reserva_por_id(id_busca):
    reservas = listar_reservas()
    for r in reservas:
        if r.id == id_busca:
            return r
    return None

def excluir_reserva(id_reserva):
    reservas = listar_reservas()
    reservas_atualizadas = [r for r in reservas if r.id != id_reserva]
    
    if len(reservas_atualizadas) == len(reservas):
        return False 
    os.makedirs(_pasta_data, exist_ok=True)
    with open(ARQUIVO_RESERVAS, 'w', encoding='utf-8') as f:
        for reserva in reservas_atualizadas:
            linha = f"{reserva.id},{reserva.sala.id},{reserva.responsavel},{reserva.data},{reserva.inicio},{reserva.fim}\n"
            f.write(linha)
    
    return True

def obter_datas_com_reservas():
    reservas = listar_reservas()
    datas = set()
    for r in reservas:
        datas.add(r.data)
    return sorted(list(datas))