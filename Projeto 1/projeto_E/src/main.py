from models import Sala, Reserva
import repositorios as repo
import validacoes as val

def menu():
    print("\n=== SISTEMA DE RESERVAS DE SALAS ===")
    print("1. Cadastrar Sala")
    print("2. Listar Salas")
    print("3. Fazer Reserva")
    print("4. Listar Reservas (Geral)")
    print("5. Listar Reservas por Data")
    print("6. Excluir Sala")
    print("7. Excluir Reserva")
    print("0. Sair")
    return input("\nOpção: ")

def cadastrar_sala():
    print("\n--- Nova Sala ---")
    id_sala = str(len(repo.listar_salas()) + 1)
    nome = input("Nome da sala: ")
    cap = input("Capacidade: ")
    tipo = input("Tipo (Lab/Aula): ")
    
    try:
        nova_sala = Sala(id_sala, nome, cap, tipo)
        repo.salvar_sala(nova_sala)
        print("Sala cadastrada com sucesso!")
    except ValueError as e:
        print(f"Erro: {e}")

def fazer_reserva():
    print("\n--- Nova Reserva ---")
    salas = repo.listar_salas()
    if not salas:
        print("Nenhuma sala cadastrada.")
        return

    for s in salas:
        print(s)
        
    id_sala = input("Digite o ID da sala desejada: ")
    sala_selecionada = repo.buscar_sala_por_id(id_sala)
    
    if not sala_selecionada:
        print("Sala não encontrada.")
        return

    # Coletar dados
    resp = input("Responsável: ")
    data = input("Data (AAAA-MM-DD): ")
    inicio = input("Horário Início (HH:MM): ")
    fim = input("Horário Fim (HH:MM): ")

    id_res = str(len(repo.listar_reservas()) + 1)
    
    try:
        nova_reserva = Reserva(id_res, sala_selecionada, resp, data, inicio, fim)
        
        # 3. Validar conflito
        todas_reservas = repo.listar_reservas()
        if val.verificar_conflito(nova_reserva, todas_reservas):
            print("ERRO: Conflito de horário! Já existe reserva neste período.")
        else:
            repo.salvar_reserva(nova_reserva)
            print("Reserva realizada com sucesso!")
            
    except ValueError as e:
        print(f"Erro nos dados: {e}")

def listar_reservas_filtro():
    print("\n--- Consultar Reservas por Data ---")
    
    
    datas_disponiveis = repo.obter_datas_com_reservas()
    
    if not datas_disponiveis:
        print("Nenhuma reserva cadastrada.")
        return
    
    print("\nDatas com reservas feitas:")
    for i, data in enumerate(datas_disponiveis, 1):
        print(f"{i}. {data}")
    
    
    try:
        escolha = input("\nDigite o número da data desejada: ")
        indice = int(escolha) - 1
        
        if indice < 0 or indice >= len(datas_disponiveis):
            print("Opção inválida.")
            return
        
        data_selecionada = datas_disponiveis[indice]
        
        
        todas = repo.listar_reservas()
        reservas_data = [r for r in todas if r.data == data_selecionada]
        
        print(f"\nReservas para {data_selecionada}:")
        if reservas_data:
            for r in reservas_data:
                print(f"- {r}")
        else:
            print("Nenhuma reserva encontrada.")
            
    except ValueError:
        print("Opção inválida. Digite um número.")

def excluir_sala():
    print("\n--- Excluir Sala ---")
    salas = repo.listar_salas()
    
    if not salas:
        print("Nenhuma sala cadastrada.")
        return
    
    for s in salas:
        print(s)
    
    id_sala = input("\nDigite o ID da sala a excluir: ")
    
    if repo.excluir_sala(id_sala):
        print("Sala excluída com sucesso!")
    else:
        print("Sala não encontrada.")

def excluir_reserva():
    print("\n--- Excluir Reserva ---")
    reservas = repo.listar_reservas()
    
    if not reservas:
        print("Nenhuma reserva cadastrada.")
        return
    
    for r in reservas:
        print(r)
        print()
    
    id_reserva = input("Digite o ID da reserva a excluir: ")
    
    if repo.excluir_reserva(id_reserva):
        print("Reserva excluída com sucesso!")
    else:
        print("Reserva não encontrada.")

if __name__ == "__main__":
    while True:
        op = menu()
        if op == "1":
            cadastrar_sala()
        elif op == "2":
            salas = repo.listar_salas()
            for s in salas: print(s)
        elif op == "3":
            fazer_reserva()
        elif op == "4":
            reservas = repo.listar_reservas()
            for r in reservas: print(r)
        elif op == "5":
            listar_reservas_filtro()
        elif op == "6":
            excluir_sala()
        elif op == "7":
            excluir_reserva()
        elif op == "0":
            break
        else:
            print("Opção inválida.")