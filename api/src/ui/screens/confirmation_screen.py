import customtkinter as ctk


class ConfirmationScreen(ctk.CTkToplevel):
    """
    Confirmation Screen
    """

    def __init__(self, master, message: str) -> None:
        super().__init__(master)
        self.geometry("300x150")
        self.title("Confirmação")
        self.grab_set()

        self.label = ctk.CTkLabel(self, text=message)
        self.label.pack(pady=20)

        self.response = None

        self.yes_button = ctk.CTkButton(
            self, text="Sim", command=self._on_yes, fg_color="green"
        )
        self.yes_button.pack(side="left", padx=10, pady=10)

        self.no_button = ctk.CTkButton(
            self, text="Não", command=self._on_no, fg_color="red"
        )
        self.no_button.pack(side="right", padx=10, pady=10)

    def _on_yes(self) -> None:
        self.response = True
        self.destroy()

    def _on_no(self) -> None:
        self.response = False
        self.destroy()

    def get_response(self) -> str:
        self.wait_window(self)
        return self.response
