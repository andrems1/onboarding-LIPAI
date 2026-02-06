def verificar_conflito(nova_reserva, lista_reservas_existentes):
    
    for r in lista_reservas_existentes:
        if r.sala.id != nova_reserva.sala.id:
            continue
        if r.data != nova_reserva.data:
            continue
            
        if (nova_reserva.inicio < r.fim) and (nova_reserva.fim > r.inicio):
            return True # conflito 
            
    return False # sem conflito 