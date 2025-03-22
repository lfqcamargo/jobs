import customtkinter as ctk
from src.domain.users.enterprise.entities.user import User
from src.infra.desktop.composers.fetch_users_composer import fetch_users_composer


class TableFrame(ctk.CTkScrollableFrame):
    """
    Table Frame
    """

    def __init__(self, master, **kwargs) -> None:
        super().__init__(master, **kwargs)

        users = fetch_users_composer().execute()
        self.header = self.create_table_header()
        self.header.grid(row=0, column=0, columnspan=4, padx=5, pady=10, sticky="nsew")

        self.display_users(users)

    def create_table_header(self) -> ctk.CTkFrame:
        """
        Creates a header for the table with column names.
        """
        header_frame = ctk.CTkFrame(self)

        header_frame.columnconfigure(0, weight=1, minsize=250)
        header_frame.columnconfigure(1, weight=1, minsize=250)
        header_frame.columnconfigure(2, weight=1, minsize=100)
        header_frame.columnconfigure(3, weight=1, minsize=100)

        ctk.CTkLabel(
            header_frame, text="Nome", font=("Arial", 14, "bold"), anchor="w"
        ).grid(row=0, column=0, padx=5, pady=5)
        ctk.CTkLabel(
            header_frame, text="Email", font=("Arial", 14, "bold"), anchor="w"
        ).grid(row=0, column=1, padx=5, pady=5)

        ctk.CTkLabel(
            header_frame, text="Nascimento", font=("Arial", 14, "bold"), anchor="e"
        ).grid(row=0, column=2, padx=5, pady=5, sticky="e")

        ctk.CTkButton(
            header_frame,
            text="+",
            font=("Arial", 14, "bold"),
            width=50,
            fg_color="green",
        ).grid(row=0, column=3, padx=5, pady=5, sticky="e")

        return header_frame

    def display_users(self, users: list[User]) -> None:
        """
        Displays the list of users in the table-like format.
        """
        if users:
            for index, user in enumerate(users, start=1):
                user_frame = ctk.CTkFrame(self)

                user_frame.columnconfigure(0, weight=1, minsize=300)
                user_frame.columnconfigure(1, weight=1, minsize=250)
                user_frame.columnconfigure(2, weight=1, minsize=100)
                user_frame.columnconfigure(3, weight=1, minsize=100)
                user_frame.columnconfigure(3, weight=1, minsize=100)

                user_frame.grid(
                    row=index, column=0, columnspan=4, padx=5, pady=5, sticky="w"
                )

                ctk.CTkLabel(user_frame, text=user.get_name(), font=("Arial", 12)).grid(
                    row=0, column=0, padx=5, pady=5, sticky="w"
                )

                ctk.CTkLabel(
                    user_frame, text=user.get_email(), font=("Arial", 12)
                ).grid(row=0, column=1, padx=5, pady=5, sticky="w")

                ctk.CTkLabel(
                    user_frame,
                    text=user.get_birthday_date().strftime("%d/%m/%Y"),
                    font=("Arial", 12),
                ).grid(row=0, column=2, padx=5, pady=5)

                ctk.CTkButton(user_frame, text="/", font=("Arial", 12), width=50).grid(
                    row=0, column=3, padx=5, pady=5, sticky="e"
                )

                ctk.CTkButton(
                    user_frame, text="E", font=("Arial", 12), width=50, fg_color="red"
                ).grid(row=0, column=4, padx=5, pady=5, sticky="e")


class UserScreen(ctk.CTkToplevel):
    """
    User Screen
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.geometry("600X500")
        self.title("Usuários")
        self.grab_set()

        self.label = ctk.CTkLabel(self, text="Usuários")
        self.label.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

        self.table_frame = TableFrame(master=self, width=900)
        self.table_frame.grid(row=1, column=0, padx=20, pady=40, sticky="nsew")
