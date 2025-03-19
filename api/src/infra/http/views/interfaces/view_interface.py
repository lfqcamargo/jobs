from abc import ABC, abstractmethod
from src.infra.http.views.http_types.http_request import HttpRequest
from src.infra.http.views.http_types.http_response import HttpResponse


class ViewInterface(ABC):
    """
    Interface for the View layer in an MVC.

    This interface defines a contract for classes that handle HTTP requests
    and return HTTP responses, ensuring the implementation of the `handle` method.
    """

    @abstractmethod
    def handle(self, http_request: HttpRequest) -> HttpResponse:
        """
        Handles an HTTP request and returns an HTTP response.

        This method must be implemented by all concrete classes that inherit
        from this interface.

        Args:
            http_request (HttpRequest): The incoming HTTP request.

        Returns:
            HttpResponse: The corresponding HTTP response.
        """
