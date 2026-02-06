class Sala:
    def __init__(self, id_sala, nome, capacidade, tipo):
        self.id = id_sala
        self.nome = nome
        self.capacidade = capacidade
        self.tipo = tipo  

    @property
    def capacidade(self):
        return self._capacidade

    @capacidade.setter
    def capacidade(self, valor):
        if int(valor) <= 0:
            raise ValueError("A capacidade deve ser maior que zero.")
        self._capacidade = int(valor)

    def __str__(self):
        return f"[{self.id}] {self.nome} ({self.tipo}) - Cap: {self.capacidade} pessoas"


class Reserva:
    def __init__(self, id_reserva, sala_obj, responsavel, data, horario_inicio, horario_fim):
        self.id = id_reserva
        self.sala = sala_obj  
        self.responsavel = responsavel
        self.data = data      
        self.inicio = horario_inicio 
        self.fim = horario_fim       

    @property
    def sala(self):
        return self._sala
    
    @sala.setter
    def sala(self, valor):
        if not isinstance(valor, Sala):
            raise ValueError("O objeto associado deve ser do tipo Sala.")
        self._sala = valor

    def __str__(self):
        return (f"Reserva [{self.id}] - {self.data} | {self.inicio} às {self.fim}\n"
                f"   Local: {self.sala.nome} | Resp: {self.responsavel}")