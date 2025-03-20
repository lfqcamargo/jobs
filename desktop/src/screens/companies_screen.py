import tkinter as tk


class CompaniesScreen(tk.Toplevel):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.title("Empresas")
        self.geometry("800x600")

        label = tk.Label(self, text="Bem-vindo à tela de Empresas!")
        label.pack(pady=50)

        button_close = tk.Button(self, text="Fechar", command=self.destroy)
        button_close.pack(pady=10)
