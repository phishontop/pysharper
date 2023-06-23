from src.domain.commands import base
from dataclasses import dataclass


@dataclass
class CreateFunction(base.Command):
    name: str
    content: str
