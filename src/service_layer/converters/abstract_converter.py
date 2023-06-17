from abc import ABC, abstractmethod


class AbstractConverter(ABC):
    """
    Abstract base class for converters
    This is used to convert one ds to another ds
    """

    @abstractmethod
    def _convert(self) -> str:
        raise NotImplementedError

    def convert(self) -> str:
        return self._convert()
