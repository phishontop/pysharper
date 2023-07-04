from dataclasses import dataclass

from src.domain.commands.base import Command


class RefactorArgumentError(Exception):
    pass


@dataclass
class Refactor(Command):
    target_file: str
    output_file: str
