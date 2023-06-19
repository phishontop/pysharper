from dataclasses import dataclass


@dataclass
class Rule:
    id: int
    name: str
    description: str
    enabled: bool = True
