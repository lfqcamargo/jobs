from tkinter import StringVar
from tkinter import messagebox
import customtkinter as ctk
from pydantic import ValidationError


from src.core.errors.resource_not_found_error import ResourceNotFoundError
from src.core.errors.error_server import ErrorServer
from src.domain.users.enterprise.entities.user import User
from src.infra.desktop.composers.fetch_users_composer import fetch_users_composer
from src.infra.desktop.composers.create_user_composer import create_user_composer
from src.infra.desktop.composers.delete_user_composer import delete_user_composer
from src.infra.desktop.composers.edit_user_composer import edit_user_composer
from .confirmation_screen import ConfirmationScreen
from ..components.button import Button
from ..components.label import Label


class FrameUser(ctk.CTkFrame):
    def __init__(
        self,
        *args,
        identifier: int,
        name: StringVar,
        email: StringVar,
        birthday_date: StringVar,
        password: StringVar,
        **kwargs
    ) -> None:
        super().__init__(*args, **kwargs)

        self.identifier = identifier
        self.name = name
        self.email = email
        self.birthday_date = birthday_date
        self.password = password


class TableFrame(ctk.CTkScrollableFrame):
    """
    Table Frame
    """

    def __init__(self, master, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.__row = 0

        self.header = self.__create_table_header()
        self.header.grid(row=0, column=0, columnspan=4, padx=5, pady=10, sticky="nsew")

        self.__init_users()

    def __create_table_header(self) -> ctk.CTkFrame:
        """
        Creates a header for the table with column names.
        """
        header_frame = ctk.CTkFrame(self)

        Label(header_frame, text="Nome", types="h2", anchor="w", width=350).grid(
            row=0, column=0, padx=5, pady=5, sticky="w"
        )

        Label(
            header_frame,
            text="Email",
            types="h2",
            anchor="w",
            width=350,
        ).grid(row=0, column=1, padx=5, pady=5, sticky="w")

        Label(
            header_frame,
            text="Nascimento",
            types="h2",
            anchor="w",
            width=90,
        ).grid(row=0, column=2, padx=5, pady=5, sticky="w")

        Label(
            header_frame,
            text="Senha",
            types="h2",
            anchor="w",
            width=200,
        ).grid(row=0, column=3, padx=5, pady=5, sticky="w")

        Button(
            header_frame,
            text="+",
            types="accept",
            width=50,
            command=lambda: self.__add_user(None),
        ).grid(row=0, column=4, padx=5, pady=5, sticky="e")

        return header_frame

    def __init_users(self) -> None:
        try:
            users = fetch_users_composer().handle()
            for user in users:
                self.__add_user(user)
        except Exception as e:
            if isinstance(e, ErrorServer):
                messagebox.showerror("Error", str(e), parent=self)

    def __add_user(self, user: User = None) -> None:
        self.__row += 1

        if user:
            identifier = user.get_identifier()
            name = StringVar()
            name.set(user.get_name())

            email = StringVar()
            email.set(user.get_email())

            birthday_date = StringVar()
            birthday_date.set(user.get_birthday_date().strftime("%d/%m/%Y"))
            birthday_str = birthday_date.get()
        else:
            identifier = 0
            name = StringVar()
            name.set("")
            email = StringVar()
            email.set("")
            birthday_date = StringVar()
            birthday_date.set("")

        password = StringVar()

        user_frame = FrameUser(
            self,
            identifier=identifier,
            name=name,
            email=email,
            birthday_date=birthday_date,
            password=password,
        )

        user_frame.grid(
            row=self.__row, column=0, columnspan=4, padx=5, pady=5, sticky="w"
        )

        ctk.CTkEntry(user_frame, textvariable=name, font=("Arial", 12), width=350).grid(
            row=0, column=0, padx=5, pady=5, sticky="w"
        )

        ctk.CTkEntry(
            user_frame, textvariable=email, font=("Arial", 12), width=350
        ).grid(row=0, column=1, padx=5, pady=5, sticky="w")

        ctk.CTkEntry(
            user_frame,
            textvariable=birthday_date,
            font=("Arial", 12),
            width=90,
        ).grid(row=0, column=2, padx=5, pady=5)

        ctk.CTkEntry(
            user_frame,
            textvariable=password,
            font=("Arial", 12),
            width=200,
            show="*",
        ).grid(row=0, column=3, padx=5, pady=5, sticky="w")

        Button(
            user_frame,
            text="S",
            width=50,
            command=lambda: self.__save_user(user_frame),
        ).grid(row=0, column=4, padx=5, pady=5, sticky="e")

        Button(
            user_frame,
            text="E",
            types="danger",
            width=50,
            command=lambda: self.__delete_user(user_frame),
        ).grid(row=0, column=5, padx=5, pady=5, sticky="e")

    def __delete_user(self, user_frame: ctk.CTkFrame) -> None:
        identifier = getattr(user_frame, "identifier", 0)
        if identifier > 0:
            confirmation_screen = ConfirmationScreen(
                self, "Usuário sera deletado, deseja continuar?"
            )

            self.wait_window(confirmation_screen)

            if confirmation_screen.response is True:
                try:
                    delete_user_composer().handle(identifier)
                    user_frame.destroy()
                except Exception as e:
                    if isinstance(e, ValidationError):
                        messagebox.showerror("Error", str(e), parent=self)
                    if isinstance(e, ResourceNotFoundError):
                        messagebox.showerror("Error", str(e), parent=self)
                    else:
                        messagebox.showerror("Error", "Erro Interno.")
        else:
            user_frame.destroy()

    def __save_user(self, user_frame: FrameUser) -> None:
        identifier = getattr(user_frame, "identifier", 0)

        if identifier == 0:
            try:
                create_user_composer().handle(
                    user_frame.name.get(),
                    user_frame.email.get(),
                    user_frame.birthday_date.get(),
                    user_frame.password.get(),
                )
                messagebox.showinfo("Usuário", "Usuário criado com sucesso.")
            except Exception as e:
                if isinstance(e, ValidationError):
                    messagebox.showerror("Error", str(e), parent=self)
                else:
                    messagebox.showerror("Error", "Erro Interno.")
        else:
            try:
                edit_user_composer().handle(
                    identifier,
                    user_frame.name.get(),
                    user_frame.email.get(),
                    user_frame.birthday_date.get(),
                    user_frame.password.get(),
                )
                messagebox.showinfo("Usuário", "Usuário alterado com sucesso.")
            except Exception as e:
                if isinstance(e, ValidationError):
                    messagebox.showerror("Error", str(e), parent=self)
                else:
                    messagebox.showerror("Error", "Erro Interno.")


class UserScreen(ctk.CTkToplevel):
    """
    User Screen
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.geometry("1400x800")
        self.title("Usuários")
        self.grab_set()

        self.label = Label(self, text="Usuários", types="h1").pack(pady=10)

        self.table_frame = TableFrame(master=self, height=500, width=1300)
        self.table_frame.pack(pady=20)
