from abc import ABC, abstractmethod
from src.domain.models import datastructure
from typing import List


class AbstractDataStructureFinder(ABC):
    """Abstract base class for ds finders eg: tuple, list, string, sets, dicts, etc"""

    @abstractmethod
    def _run_finder(self) -> List[datastructure.DataStructure]:
        raise NotImplementedError

    def run_finder(self) -> List[datastructure.DataStructure]:
        return self._run_finder()
