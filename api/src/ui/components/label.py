from enum import Enum
from typing import Literal
import customtkinter as ctk


class LabelStyles(Enum):
    """
    Enum representing different label styles.

    Attributes:
        H1 (str): Represents the 'H1' style with larger font size.
        H2 (str): Represents the 'H2' style with medium font size.
        NORMAL (str): Represents the 'normal' style with default font size.
    """

    H1 = "h1"
    H2 = "h2"
    NORMAL = "normal"


class Label(ctk.CTkLabel):
    """
    Custom label component with predefined styles using CustomTkinter.

    Args:
        master (ctk.CTk | None): The parent widget for the label.
        types (Literal["h1", "h2", "normal"], optional):
        Defaults to "normal".
        *args: Additional positional arguments for CTkLabel.
        **kwargs: Additional keyword arguments for CTkLabel.
    """

    def __init__(
        self, *args, types: Literal["h1", "h2", "normal"] = "normal", **kwargs
    ) -> None:
        super().__init__(*args, **kwargs)

        if types == LabelStyles.H1.value:
            self.configure(font=("Arial", 24, "bold"))

        elif types == LabelStyles.H2.value:
            self.configure(font=("Arial", 16, "bold"))

        elif types == LabelStyles.NORMAL.value:
            self.configure(font=("Arial", 14))
