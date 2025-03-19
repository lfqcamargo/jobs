from typing import Dict


class HttpResponse:
    """
    Represents an HTTP response, including status code and body.
    """

    def __init__(self, status_code: int, body: Dict = None) -> None:
        self.status_code = status_code
        self.body = body
