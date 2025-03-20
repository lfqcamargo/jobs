import tkinter as tk
from src.screens.companies_screen import CompaniesScreen


class HomeScreen(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Bot de Candidaturas a Vagas!")
        self.geometry("1600x920")
        self.__button_companies()

    def __button_companies(self) -> None:
        self.button_company = tk.Button(
            self, text="Empresas", command=self.__handle_open_companies
        )
        self.button_company.pack(pady=20)

    def __handle_open_companies(self) -> None:
        company_window = CompaniesScreen(self)
        company_window.grab_set()
