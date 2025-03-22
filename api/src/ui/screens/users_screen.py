import customtkinter as ctk
from src.domain.users.enterprise.entities.user import User
from src.infra.desktop.composers.fetch_users_composer import fetch_users_composer


class TableFrame(ctk.CTkScrollableFrame):
    """
    Table Frame
    """

    def __init__(self, master, **kwargs) -> None:
        super().__init__(master, **kwargs)

        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        users = fetch_users_composer().execute()
        self.header = self.create_table_header()
        self.header.grid(row=0, column=0, columnspan=3, padx=5, pady=10, sticky="nsew")

        self.display_users(users)

    def create_table_header(self) -> ctk.CTkFrame:
        """
        Creates a header for the table with column names.
        """
        header_frame = ctk.CTkFrame(self)
        ctk.CTkLabel(header_frame, text="Nome", font=("Arial", 16, "bold")).grid(
            row=0, column=0, padx=5, pady=5
        )
        ctk.CTkLabel(header_frame, text="Email", font=("Arial", 16, "bold")).grid(
            row=0, column=1, padx=5, pady=5
        )
        ctk.CTkLabel(
            header_frame, text="Data de Anivsersário", font=("Arial", 16, "bold")
        ).grid(row=0, column=2, padx=5, pady=5)

        ctk.CTkLabel(header_frame, text="", font=("Arial", 16, "bold")).grid(
            row=0, column=2, padx=5, pady=5
        )

        return header_frame

    def display_users(self, users: list[User]) -> None:
        """
        Displays the list of users in the table-like format.
        """
        if users:
            for index, user in enumerate(users, start=1):
                user_frame = ctk.CTkFrame(self)
                user_frame.grid(
                    row=index, column=0, columnspan=4, padx=5, pady=5, sticky="nsew"
                )

                ctk.CTkLabel(user_frame, text=user.get_name(), font=("Arial", 12)).grid(
                    row=0, column=0, padx=5, pady=5
                )

                ctk.CTkLabel(
                    user_frame, text=user.get_email(), font=("Arial", 12)
                ).grid(row=0, column=1, padx=5, pady=5)

                ctk.CTkLabel(
                    user_frame, text=user.get_birthday_date(), font=("Arial", 12)
                ).grid(row=0, column=2, padx=5, pady=5)

                # action_button = ctk.CTkButton(
                #     user_frame,
                #     text="View",
                # )
                # action_button.grid(row=0, column=2, padx=5, pady=5)


class UserScreen(ctk.CTkToplevel):
    """
    User Screen
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.geometry("800x600")
        self.title("Usuários")
        self.grab_set()

        self.label = ctk.CTkLabel(self, text="Usuários")
        self.label.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

        self.table_frame = TableFrame(master=self, width=600)
        self.table_frame.grid(row=1, column=0, padx=20, pady=40, sticky="nsew")
