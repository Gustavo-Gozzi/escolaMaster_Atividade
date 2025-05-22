# Microserviço: Atividade

Microserviço responsável por administrar as atividades escolares, ligando-as às turmas e a um professor. Permite cadastrar, listar e consultar atividade além de ter algumas validações importantes: 

- Verifica se a turma e o professor existem. 
- Valida se a data de entrega é maior que a data atual.

# Tecnologias Utilizadas

- Python 3.12  
- Flask  
- SQLAlchemy  
- SQLite  
- REST API  

---

# Estrutura de Diretórios

```
escolaMaster_Atividade/
│
├── app.py                      # Ponto de entrada da aplicação Flask
├── database.py                 # Configuração e instância do banco de dados
├── control/
│   └── control_atividade.py    # Lógica de controle e rotas da API
├── model/
│   └── model_atividade.py      # Modelo ORM da Atividade
├── instance/
│   └── atividade.db            # Banco de dados SQLite
```

---

# Endpoints da API

### POST `/atividade`

Cria uma nova atividade.

#### Corpo da Requisição (JSON)

```json
{
  "professor_id": 1,
  "turma_id": 2,
  "materia": "História",
  "dt_entrega": "15-05-2024"
}
```

#### Validações

- Verifica a existência do professor e da turma via chamadas HTTP externas.
- A data de entrega deve ser posterior ao dia atual.

#### Respostas

- `200 OK` – Atividade criada com sucesso.  
- `400 Bad Request` – Professor ou turma não encontrados, ou data inválida.

---

### GET `/atividade`

Retorna a lista de todas as atividades cadastradas.

#### Resposta

```json
[
  {
    "id": 1,
    "professor_id": 1,
    "turma_id": 2,
    "materia": "História",
    "data_entrega": "15-05-2024"
  }
]
```

- `200 OK` – Lista retornada com sucesso.

---

### GET `/atividade/<id>`

Consulta uma atividade específica pelo ID.

#### Exemplo

```http
GET /atividade/1
```

#### Resposta

```json
{
  "id": 1,
  "professor_id": 1,
  "turma_id": 2,
  "materia": "História",
  "data_entrega": "15-05-2024"
}
```

#### Erros Possíveis

- `400 Bad Request` – Atividade não encontrada.

---

## Observações

- Validação da turma:
  ```
  GET http://localhost:8000/turmas/{idTurma}
  ```

- Validação do professor:
  ```
  GET http://localhost:8000/professores/{idProfessor}
  ```

- O banco de dados SQLite (`atividade.db`) é gerado automaticamente na primeira execução da aplicação.

---
