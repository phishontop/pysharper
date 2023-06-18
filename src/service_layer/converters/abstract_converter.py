from abc import ABC, abstractmethod


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
