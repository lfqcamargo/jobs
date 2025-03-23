from enum import Enum
from typing import Literal
import customtkinter as ctk


class ButtonStyles(Enum):
    """
    Enum representing different button styles.

    Attributes:
        ACCEPT (str): Represents the 'accept' button style.
        WARNING (str): Represents the 'warning' button style.
        DANGER (str): Represents the 'danger' button style.
        NORMAL (str): Represents the 'normal' button style.
    """

    ACCEPT = "accept"
    WARNING = "warning"
    DANGER = "danger"
    NORMAL = "normal"


class Button(ctk.CTkButton):
    """
    Custom button component with predefined styles using CustomTkinter.

    Args:
        master (ctk.CTk | None): The parent widget for the button.
        types (Literal["accept", "warning", "danger", "normal"], optional):
        Defaults to "normal".
        *args: Additional positional arguments for CTkButton.
        **kwargs: Additional keyword arguments for CTkButton.
    """

    def __init__(
        self,
        *args,
        types: Literal["accept", "warning", "danger", "normal"] = "normal",
        **kwargs
    ) -> None:
        super().__init__(*args, **kwargs)

        if types == ButtonStyles.ACCEPT.value:
            self.configure(fg_color="green")

        elif types == ButtonStyles.WARNING.value:
            self.configure(fg_color="orange")

        elif types == ButtonStyles.DANGER.value:
            self.configure(fg_color="red")

        elif types == ButtonStyles.NORMAL.value:
            self.configure(fg_color="blue")
