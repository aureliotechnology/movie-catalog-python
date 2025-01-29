# Define variáveis para os serviços Docker
DOCKER_COMPOSE = docker-compose
SERVICE_API = movie_api
SERVICE_DB = movie_db

# Inicia o ambiente Docker (API + Banco de Dados)
up:
	$(DOCKER_COMPOSE) up --build -d

# Para os containers Docker
down:
	$(DOCKER_COMPOSE) down

# Reinicia a API sem reiniciar o banco de dados
restart-api:
	$(DOCKER_COMPOSE) restart $(SERVICE_API)

# Executa um shell dentro do container da API
shell:
	$(DOCKER_COMPOSE) exec $(SERVICE_API) /bin/sh

# Executa um shell dentro do container do banco de dados
db-shell:
	$(DOCKER_COMPOSE) exec $(SERVICE_DB) psql -U user -d movie_catalog

# Verifica os logs da API
logs-api:
	$(DOCKER_COMPOSE) logs -f $(SERVICE_API)

# Verifica os logs do banco de dados
logs-db:
	$(DOCKER_COMPOSE) logs -f $(SERVICE_DB)

# Roda os testes dentro do container da API
test:
	$(DOCKER_COMPOSE) exec $(SERVICE_API) pytest -v

# Executa migrações do Alembic dentro do container
migrate:
	$(DOCKER_COMPOSE) exec $(SERVICE_API) alembic upgrade head

# Cria uma nova migração com o nome especificado
migrate-create:
	$(DOCKER_COMPOSE) exec $(SERVICE_API) alembic revision --autogenerate -m "$(M)"

# Apaga os containers, imagens e volumes (usar com cautela)
reset:
	$(DOCKER_COMPOSE) down --volumes --remove-orphans
