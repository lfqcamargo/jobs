import customtkinter as ctk


class ButtonBottomFrame(ctk.CTkButton):
    def __init__(self, master=None, text="Button", command=None, **kwargs) -> None:
        super().__init__(
            master,
            text=text,
            command=command,
            fg_color="red",
            hover_color="#005582",
            text_color="white",
            corner_radius=4,
            **kwargs
        )
