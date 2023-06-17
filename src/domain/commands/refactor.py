from dataclasses import dataclass

from src.domain.commands.base import Command


@dataclass
class Refactor(Command):
    target_file: str
    output_file: str
