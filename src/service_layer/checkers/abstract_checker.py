from abc import ABC, abstractmethod


class AbstractChecker(ABC):
    """Abstract base class for the checkers"""
    old_text: str
    new_text: str

    def __init__(self, text: str):
        pass

    @abstractmethod
    def _run_checks(self):
        raise NotImplementedError

    def run_checks(self):
        return self._run_checks()

    def has_changed(self) -> bool:
        """
        Checks to see if the text (code) has changed
        therefore meaning an error has been fixed
        """
        return self.old_text != self.new_text
