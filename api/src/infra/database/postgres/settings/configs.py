import os
from collections import namedtuple
from dotenv import load_dotenv
from dotenv import dotenv_values


load_dotenv()

DatabaseConfig = namedtuple(
    "DatabaseConfig",
    ["DB_USER", "DB_PASSWORD", "DB_HOST", "DB_PORT", "DB_NAME", "DATABASE_URL"],
)


def load_database_config() -> DatabaseConfig:
    env = dotenv_values().get("ENV")

    if "test" in env.lower():
        print("CARREGANDO TEST")
        return DatabaseConfig(
            DB_USER=os.getenv("DB_USER_TEST"),
            DB_PASSWORD=os.getenv("DB_PASSWORD_TEST"),
            DB_HOST=os.getenv("DB_HOST_TEST"),
            DB_PORT=os.getenv("DB_PORT_TEST"),
            DB_NAME=os.getenv("DB_NAME_TEST"),
            DATABASE_URL=os.getenv("DATABASE_URL_TEST"),
        )
    else:
        print("CARREGANDO PROD")
        return DatabaseConfig(
            DB_USER=os.getenv("DB_USER"),
            DB_PASSWORD=os.getenv("DB_PASSWORD"),
            DB_HOST=os.getenv("DB_HOST"),
            DB_PORT=os.getenv("DB_PORT"),
            DB_NAME=os.getenv("DB_NAME"),
            DATABASE_URL=os.getenv("DATABASE_URL"),
        )


# Criar a instância de configuração de banco de dados conforme o ambiente
database_configs = load_database_config()
