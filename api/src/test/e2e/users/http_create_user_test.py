import os
import pytest
from dotenv import load_dotenv
from alembic import command
from alembic.config import Config
from src.infra.server.server import create_app
from src.infra.database.postgres.settings.connection import DBConnectionHandler
import logging


load_dotenv()


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@pytest.fixture(scope="module")
def client():
    """Configuração do cliente de teste"""

    app = create_app()

    app.config["TESTING"] = True

    with app.app_context():
        alembic_cfg = Config("alembic.ini")
        try:
            logger.info("Aplicando migrações Alembic...")
            command.upgrade(alembic_cfg, "head")
            logger.info("Migrações aplicadas com sucesso.")
        except Exception as e:
            logger.error(f"Erro ao aplicar migrações: {e}")
            raise

    # Criação do cliente de teste
    with app.test_client() as client:
        yield client


def test(client):
    assert True


# def test_banco(client):
#     # Verificar se a conexão com o banco de dados foi realizada corretamente
#     response = client.get(
#         "/some_endpoint"
#     )  # Altere para um endpoint válido de sua aplicação

#     # Verificar se a resposta é bem-sucedida (200 OK)
#     assert response.status_code == 200

#     # Aqui você pode adicionar mais verificações para validar os dados no banco
#     # Por exemplo, criar um registro e verificar se ele foi inserido corretamente
#     # Isso depende da lógica de sua aplicação e do banco de dados

#     # Exemplo: Verificar se existe algum dado específico no banco
#     with DBConnectionHandler(db_url=os.getenv("TEST_DATABASE_URL")).session.begin():
#         result = DBConnectionHandler().session.execute("SELECT COUNT(*) FROM users")
#         count = result.scalar()

#     # Verificar se há registros na tabela 'users'
#     assert count > 0  # Verifique se ao menos um usuário foi criado

#     # Limpeza após o teste, se necessário
#     with DBConnectionHandler(db_url=os.getenv("TEST_DATABASE_URL")).session.begin():
#         DBConnectionHandler().session.execute("DELETE FROM users")
