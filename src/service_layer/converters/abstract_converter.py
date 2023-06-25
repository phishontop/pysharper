from abc import ABC, abstractmethod
from src.domain.models import request_models


class AbstractConverter(ABC):
    """
    Abstract base class for converters
    This is used to convert one ds to another ds
    """

    @abstractmethod
    def _convert(self):
        raise NotImplementedError

    def convert(self):
        return self._convert()


class IfStatementConverterMethod(AbstractConverter, ABC):
    """
    Abstract base class for if statement converter methods
    This is implemented in the strategy pattern to help abstract the task
    """


class HttpclientConverterMethod(AbstractConverter, ABC):
    """
    Abstract base class for http client converter methods
    This is implemented to help with abstraction using the strategy design pattern
    """
    client_variable: str
    request_object: request_models.Request

    def convert_to_get_request(self) -> str:
        """
        Converts request object to httpclient request string
        Eg: request("GET", "/3/", headers={"Host": host})
        """
        args = ", ".join([
            f'"{self.request_object.method.upper()}"',
            f'"{self.request_object.path}"',
            f"headers={self.request_object.args['headers']}"
        ])

        return f"request({args})"


class HttpclientResponseConverterMethod(AbstractConverter, ABC):
    """
    Abstract base class for http client converter methods
    This is used to convert requests response calls to http client response calls
    eg .json() call will get converted to getting the text then json loading it
    """

