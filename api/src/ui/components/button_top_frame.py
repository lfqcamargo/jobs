import customtkinter as ctk


class ButtonTopFrame(ctk.CTkButton):
    def __init__(self, master=None, text="Button", command=None, **kwargs) -> None:
        super().__init__(
            master,
            text=text,
            command=command,
            fg_color="#0077b5",
            hover_color="#005582",
            text_color="white",
            corner_radius=12,
            **kwargs
        )
