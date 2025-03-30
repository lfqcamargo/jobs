import os
import pytest
from alembic import command
from alembic.config import Config
from src.infra.server.server import create_app as app
from src.infra.database.postgres.settings.connection import db_connection_handler
from dotenv import load_dotenv

# Carregar as variáveis de ambiente
load_dotenv()


@pytest.fixture
def client():
    # Configuração de teste
    app.config["TESTING"] = True

    # Configurar a URL do banco de dados de teste e o esquema de teste
    os.environ["ENV"] = "test"
    os.environ["DATABASE_URL"] = os.getenv("TEST_DATABASE_URL")

    # Inicializa a aplicação
    with app.app_context():
        # Rodar o Alembic para aplicar as migrações
        alembic_cfg = Config("alembic.ini")
        command.upgrade(alembic_cfg, "head")  # Aplica as migrações

    # Criação do cliente de teste
    with app.test_client() as client:
        yield client

    # Aqui você pode adicionar código para limpar o banco de dados após o teste, se necessário
