import customtkinter as ctk
from .components.button import Button
from .screens.users_screen import UserScreen


class TopFrame(ctk.CTkFrame):
    """
    Top Frame
    """

    def __init__(self, master, **kwargs) -> None:
        super().__init__(master, **kwargs)

        self.button_linkedin = Button(
            self, text="Linkedin", command=self.__handle_button_linkedin
        )
        self.button_linkedin.pack(side="left", padx=20, pady=10)

        self.button_indeed = Button(
            self, text="Indeed", command=self.__handle_button_indeed
        )
        self.button_indeed.pack(side="left", padx=20, pady=10)

        self.button_glassdor = Button(
            self, text="Glassdor", command=self.__handle_button_glassdor
        )
        self.button_glassdor.pack(side="left", padx=20, pady=10)

        self.pack(side="top", anchor="center")

    def __handle_button_linkedin(self) -> None:
        print("Linkedin")

    def __handle_button_indeed(self) -> None:
        print("Indeed")

    def __handle_button_glassdor(self) -> None:
        print("Glassdor")


class BottomFrame(ctk.CTkFrame):
    """
    Bottom Frame
    """

    def __init__(self, master, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.user_screen = None

        self.button_users = Button(
            self, text="Usuários", command=self.__handle_button_users
        )

        self.button_users.pack(side="left", padx=20, pady=10)

        self.button_skills = Button(
            self, text="Habilidades", command=self.__handle_button_skills
        )

        self.button_skills.pack(side="left", padx=20, pady=10)

        self.button_jobs = Button(self, text="Vagas", command=self.__handle_button_jobs)

        self.button_jobs.pack(side="left", padx=20, pady=10)

    def __handle_button_users(self) -> None:
        self.user_screen = UserScreen(self)

    def __handle_button_skills(self) -> None:
        self.user_screen = UserScreen(self)

    def __handle_button_jobs(self) -> None:
        self.user_screen = UserScreen(self)


class App(ctk.CTk):
    """
    Init App
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.geometry("600x500")
        self.title("Aplicação de Vagas de Empregos")
        ctk.set_appearance_mode("dark")
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=3)
        self.grid_columnconfigure(0, weight=1)

        self.top_frame = TopFrame(master=self)
        self.top_frame.grid(row=0, column=0, padx=20, pady=40, sticky="nsew")

        self.bottom_frame = BottomFrame(master=self)
        self.bottom_frame.grid(row=2, column=0, padx=20, pady=20, sticky="nsew")


app = App()
