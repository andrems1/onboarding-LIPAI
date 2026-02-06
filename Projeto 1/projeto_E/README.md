# Sistema de Reservas de Salas

Sistema para **gestão de salas e laboratórios**, permitindo cadastrar salas, realizar reservas e consultar a agenda. O projeto resolve o problema de organizar o uso de salas de aula e laboratórios, evitando conflitos de horário e mantendo o histórico em arquivos.

---

## Funcionalidades 

| Funcionalidade | Descrição |
|----------------|-----------|
| **Cadastrar salas** | Inclusão de salas com nome, capacidade e tipo (Lab/Aula) |
| **Listar salas** | Exibição de todas as salas cadastradas |
| **Fazer reserva** | Criação de reservas com sala, responsável, data e horário (início e fim) |
| **Validação de conflito** | Impede reservas que se sobrepõem no mesmo dia e mesma sala |
| **Listar reservas (geral)** | Listagem de todas as reservas do sistema |
| **Listar reservas por data** | Exibe datas que possuem reservas; o usuário escolhe uma data e vê as reservas daquele dia |
| **Excluir sala** | Remoção de uma sala e de todas as reservas associadas a ela |
| **Excluir reserva** | Remoção de uma reserva específica |
| **Persistência em CSV** | Dados de salas e reservas armazenados em arquivos CSV na pasta data |

---

## Como executar

1. Abra o terminal na pasta raiz do projeto.
2. Entre na pasta onde está o código:

   ```bash
   cd src
   ```
   
3. Execute o programa:

    ```bash
   python main.py
   ```

4. Escolha as opções (1 a 7 ou 0 para sair).

---

## Estrutura de diretórios

```
projeto_E/
│
├── README.md                 # Este arquivo
│
├── src/                      # Código-fonte da aplicação
│   ├── main.py               # Ponto de entrada; menu e fluxo principal
│   ├── models.py             # Modelos: Sala e Reserva
│   ├── repositorios.py       # Acesso a dados: leitura/gravação em CSV
│   └── validacoes.py         # Regras de negócio
│
└── data/                     # Dados persistidos (gerados em execução)
    ├── salas.csv             # Cadastro de salas
    └── reservas.csv          # Cadastro de reservas
```

---
