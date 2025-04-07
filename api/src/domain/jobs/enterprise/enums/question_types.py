from enum import Enum


class QuestionTypes(Enum):
    """
    Enumeration representing the possible HTML input types for a question.

    Attributes:
        TEXT (str): Represents a text input.
        NUMBER (str): Represents a number input.
        DATE (str): Represents a date input.
        EMAIL (str): Represents an email input.
        PASSWORD (str): Represents a password input.
        CHECKBOX (str): Represents a checkbox input.
        RADIO (str): Represents a radio button input.
        SELECT (str): Represents a select (dropdown) input.
        TEXTAREA (str): Represents a multiline text area input.
    """

    TEXT = "text"
    NUMBER = "number"
    DATE = "date"
    EMAIL = "email"
    PASSWORD = "password"
    CHECKBOX = "checkbox"
    RADIO = "radio"
    SELECT = "select"
    TEXTAREA = "textarea"
