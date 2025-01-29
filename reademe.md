# 🎬 Movie Catalog API

## 📌 Sobre o Projeto
Este é um projeto de catálogo de filmes desenvolvido com **FastAPI** e **PostgreSQL**, seguindo **Clean Architecture**. A API permite o cadastro de filmes, diretores, atores, avaliações, comentários e muito mais.

## 🚀 Tecnologias Utilizadas
- **Linguagem**: Python 3.11+
- **Framework**: FastAPI
- **Banco de Dados**: PostgreSQL
- **ORM**: SQLAlchemy + Alembic
- **Autenticação**: JWT (PyJWT)
- **Testes**: Pytest
- **Containerização**: Docker + Docker Compose
- **Gerenciamento de Tarefas**: Makefile

## 📂 Estrutura do Projeto
```
movie-catalog-api/
├── app/
│   ├── api/                # Handlers e rotas
│   │   ├── endpoints/      # Rotas organizadas por módulo
│   │   ├── dependencies.py # Dependências globais da API
│   ├── core/               # Configuração central da aplicação
│   │   ├── config.py       # Configurações gerais e variáveis de ambiente
│   │   ├── security.py     # Autenticação e segurança
│   ├── models/             # Definição das tabelas (ORM)
│   ├── schemas/            # Modelos Pydantic para entrada/saída
│   ├── services/           # Lógica de negócios (CRUDs)
│   ├── db/                 # Conexão e migrações do banco
│   ├── main.py             # Ponto de entrada da API
├── tests/                  # Testes unitários e de integração
│   ├── unit/               # Testes unitários
│   ├── features/           # Testes de funcionalidades
├── docker-compose.yml      # Configuração do PostgreSQL
├── Makefile                # Comandos utilitários
├── .env                    # Variáveis de ambiente
├── requirements.txt        # Dependências do projeto
├── alembic/                # Diretório para migrações
└── README.md               # Documentação do projeto
```

## 🔧 Configuração e Instalação
### 1️⃣ Clonar o Repositório
```bash
git clone git@github.com:aureliotechnology/movie-catalog-python.git
cd movie-catalog-api
```

### 2️⃣ Configurar Variáveis de Ambiente
Crie um arquivo `.env` na raiz do projeto com:
```ini
DATABASE_URL=postgresql://user:password@db/movie_catalog
SECRET_KEY=seu_segredo_super_secreto
```

### 3️⃣ Subir a Aplicação com Docker
```bash
make up
```

### 4️⃣ Acessar a API
A API estará disponível em: **http://localhost:8000**

Documentação interativa:
- Swagger UI: **http://localhost:8000/docs**
- Redoc: **http://localhost:8000/redoc**

### 5️⃣ Executar Testes
```bash
make test
```

## 🎯 Principais Endpoints
| Método | Rota               | Descrição |
|--------|--------------------|-----------|
| `POST` | `/api/movies`      | Criar um novo filme |
| `GET`  | `/api/movies`      | Listar todos os filmes |
| `GET`  | `/api/movies/{id}` | Obter detalhes de um filme |
| `POST` | `/api/movies/{id}/rate` | Avaliar um filme |
| `POST` | `/api/movies/{id}/comment` | Comentar sobre um filme |
| `GET`  | `/api/movies/{id}/comments` | Listar comentários de um filme |
| `GET`  | `/api/health`      | Verificar o status da API |
| `GET`  | `/api/db-health`   | Verificar a conexão com o banco |

## 📌 Comandos Úteis no Makefile
| Comando | Descrição |
|---------|-------------|
| `make up` | Inicia a API e o Banco de Dados via Docker |
| `make down` | Para os contêineres do Docker |
| `make restart-api` | Reinicia apenas a API |
| `make shell` | Acessa um shell dentro do contêiner da API |
| `make db-shell` | Acessa o PostgreSQL no contêiner |
| `make logs-api` | Exibe os logs da API |
| `make logs-db` | Exibe os logs do banco |
| `make test` | Roda os testes dentro do contêiner |
| `make migrate` | Aplica as migrações do Alembic |
| `make migrate-create M="descricao"` | Cria uma nova migração Alembic |
| `make reset` | Remove contêineres e volumes do Docker |

## 📜 Licença
Este projeto está licenciado sob a [MIT License](LICENSE).


