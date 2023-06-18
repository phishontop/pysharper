from abc import ABC, abstractmethod


class AbstractFinder(ABC):

    @abstractmethod
    def _run_finder(self):
        raise NotImplementedError

    def run_finder(self):
        return self._run_finder()


class AbstractDataStructureFinder(AbstractFinder, ABC):
    """Abstract base class for ds finders eg: tuple, list, string, sets, dicts, etc"""


class AbstractBuiltinFinder(AbstractFinder, ABC):
    """Abstract base class for builtin finders eg: if statements"""
