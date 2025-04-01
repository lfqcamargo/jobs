from typing import Dict, Optional, Any
from werkzeug.datastructures import FileStorage


class HttpRequest:
    """
    Represents an HTTP request, including body and parameters.
    """

    def __init__(
        self,
        body: Optional[Dict[str, Any]] = None,
        params: Optional[Dict[str, Any]] = None,
        headers: Dict = None,
        token_infos: Dict = None,
        files: Optional[Dict[str, FileStorage]] = None,
    ) -> None:
        """
        Initializes an HttpRequest instance.

        Args:
            body (Optional[Dict[str, Any]]): The body of the HTTP request,
            containing key-value pairs.
            param (Optional[Dict[str, Any]]): Additional parameters for the HTTP request.
        """
        self.body = body or {}
        self.params = params or {}
        self.headers = headers or {}
        self.token_infos = token_infos or {}
        self.files = files or {}
