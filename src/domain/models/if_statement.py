from dataclasses import dataclass
from typing import List


@dataclass
class IfStatement:
    statements: List[str]
    start_keyword: str

    @property
    def line(self):
        return f"{self.start_keyword} {''.join(self.statements)}:"
