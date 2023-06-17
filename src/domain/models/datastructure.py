from dataclasses import dataclass
from typing import List


@dataclass
class DataStructure:
    type: str
    name: str
    methods_called: List[str]
