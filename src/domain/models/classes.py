from dataclasses import dataclass
from typing import List


def get_empty_string_count(line: str):
    for count, char in enumerate(line):
        if char.isalpha():
            return count

    return 0


@dataclass
class Function:
    name: str
    arguments: List[str]
    content: str

    @property
    def lines(self):
        return self.content.splitlines()

    def get_nest_count(self):
        indents = [len(line) - len(line.lstrip()) for line in self.lines]
        return int(max(indents) / 4)


@dataclass
class Class:
    name: str
    functions: List[Function]
