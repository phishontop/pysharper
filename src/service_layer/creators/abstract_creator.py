from abc import ABC, abstractmethod


class AbstractCreator(ABC):
    """The ABC for creation of objects, items, etc"""

    @abstractmethod
    def _create(self):
        raise NotImplementedError

    def create(self):
        return self._create()


class AbstractFunctionCreator(AbstractCreator, ABC):
    """Abstract Base Class for the creation of functions using different methods"""
