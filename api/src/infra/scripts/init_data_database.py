from src.infra.database.interfaces.db_connection_handler_interface import (
    DBConnectionHandlerInterface,
)
from src.infra.database.postgres.models.company_model import CompanyModel


def init_data_database(db_handler: DBConnectionHandlerInterface) -> None:
    """
    Initialize the database with predefined company data if no records exist.

    This function checks if there are any existing records in the 'companies' table.
    If no records are found, it inserts a set of predefined company data into the table.

    Args:
        db_handler (DBConnectionHandlerInterface): The database connection handler
        to interact with the database.

    Returns:
        None
    """
    with db_handler as db:
        if db.session.query(CompanyModel).count() == 0:
            companies = [
                CompanyModel(name="Linkedin", link="https://www.linkedin.com/"),
                CompanyModel(
                    name="Glassdoor", link="https://www.glassdoor.com.br/index.htm"
                ),
                CompanyModel(name="Indeed", link="https://br.indeed.com/"),
            ]

            db.session.bulk_save_objects(companies)
            db.session.commit()
            print("Dados de empresas iniciais inseridos com sucesso!")
