from dataclasses import dataclass


@dataclass
class ForBuiltin:
    iterator_name: str
    iterable_name: str

    @property
    def text(self) -> str:
        return f"for {self.iterator_name} in {self.iterable_name}:"
