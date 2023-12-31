from abc import ABC, abstractmethod
from src.domain.models import request_models
import http.client


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


class HttpclientResponseConverterMethod(AbstractConverter, ABC):
    """
    Abstract base class for http client converter methods
    This is used to convert requests response calls to http client response calls
    eg .json() call will get converted to getting the text then json loading it
    """

