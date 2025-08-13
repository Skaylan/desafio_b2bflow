# Desafio b2bflow

Este projeto tem como objetivo implementar uma solução de fluxo de comunicação entre o Supabase e o envio de menssaem para o WhatsApp via api do Z-api.

---

## Configuração da tabela `user` no Supabase

Para o funcionamento do projeto, é necessário criar a tabela `user` no seu banco Supabase com a seguinte estrutura:

| Campo         | Tipo         | Observações                      |
|---------------|--------------|---------------------------------|
| `id`          | `int8`       | Chave primária, auto incrementa |
| `name`        | `varchar`    | Nome do usuário                 |
| `email`       | `varchar`    | E-mail do usuário               |
| `phone_number` | `varchar`   | Número de telefone WhatsApp              |
| `created_at`  | `timestamptz`| Data e hora da criação, padrão `now()` |

---

### Comando SQL para criar a tabela

Você pode criar a tabela usando o SQL editor do Supabase com o comando:

```sql
create table public.user (
    id bigserial primary key,
    name varchar not null,
    email varchar not null unique,
    phone_number varchar not null unique,
    created_at timestamptz default now()
);
```

## Inserindo dados na tabela `user`

Você pode inserir novos registros na tabela `user` de duas formas:
usando diretamente o editor SQL do Supabase ou via código Python.

---

### 1. Inserindo via Supabase (SQL Query)

Abra o **SQL Editor** no painel do Supabase e execute o comando:

```sql
insert into public.user (name, email, phone_number)
values ('Jhon Doe', 'jhondoe@email.com', '5599999999999');
```

### Inserindo via código Python

Você também pode inserir um usuário diretamente pelo código usando o método `insert_user` do `UserController`:

```python
from app.controllers.user_controller import UserController

UserController.insert_user({
    "name": "Jhon Doe",
    "email": "jhondoe@email.com",
    "phone_number": "5599999999999"
})
```

## Como rodar o projeto localmente

### 1. Clone o repositório

```bash
git clone https://github.com/Skaylan/desafio_b2bflow
cd desafio_b2bflow
```

### 2. Crie e ative o ambiente virtual

No Linux/macOS:
```bash
python3 -m venv venv
source venv/bin/activate
```

No Windows (PowerShell):
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

No Windows (Prompt de Comando):
```cmd
python -m venv venv
.\venv\Scripts\activate.bat
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto com as variáveis necessárias.
Exemplo:

```
SUPABASE_URL = 'sua url do supabase'
SUPABASE_KEY = 'sua chave do supabase'

Z_API_INSTANCE_TOKEN = 'seu token de instância do z-api'
Z_API_INSTANCE_ID = 'seu id de instância do z-api'
Z_API_INSTANCE_SECURITY_TOKEN = 'seu token de segurança do z-api'
```

### 5. Execute o projeto

```bash
python main.py
```

---

## Observações

- Certifique-se de ter o Python 3.8+ instalado.
- Caso use Windows, ative a execução de scripts no PowerShell se der erro (`Set-ExecutionPolicy RemoteSigned`).

---
