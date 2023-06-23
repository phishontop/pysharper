from src.service_layer.creators.abstract_creator import AbstractFunctionCreator
from src.domain.models import classes, for_bultin
from typing import List


def calculate_indent(line: str) -> int:
    return len(line) - len(line.lstrip())


def clean_indents(lines: List[str]):
    line = lines[0]
    cleaned_lines = []
    remove_num = calculate_indent(line) - 4
    for line in lines:
        line_indent_count = calculate_indent(line)
        if line_indent_count >= remove_num:
            cleaned_lines.append(line[remove_num:])

    return cleaned_lines


class ForLoopMethod(AbstractFunctionCreator):

    def __init__(
        self,
        function: classes.Function,
        loop: for_bultin.ForBuiltin
    ):
        self.function = function
        self.loop = loop

    def _create(self):
        found = False
        new_lines = []
        for line in self.function.lines:
            if found:
                new_lines.append(line)
            if line.strip() == self.loop.text:
                found = True

        new_cleaned_lines = clean_indents(new_lines)
        return new_cleaned_lines
