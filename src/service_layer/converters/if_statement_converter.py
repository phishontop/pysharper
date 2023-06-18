import re

from typing import Type, Tuple

from src.domain.models import if_statement
from src.service_layer.converters.abstract_converter import (
    AbstractConverter,
    IfStatementConverterMethod
)


class IfStatementConverter(AbstractConverter):
    """
    The main converter for if statements
    This runs the ConditionConverter which runs the methods
    """

    def __init__(self, statement: if_statement.IfStatement):
        self.statement = statement

    def _convert(self):
        new_statements = []
        for statement in self.statement.statements:
            condition_converter = ConditionConverter(statement)
            new_condition = condition_converter.convert()
            new_statements.append(new_condition)

        self.statement.statements = new_statements
        return self.statement


class ConditionConverter(AbstractConverter):
    """
    The main Converter for if statement conditions
    This will use different Method classes which helps abstract the conversion progress
    """

    def __init__(self, condition: str):
        self.condition = condition

    def _convert(self) -> str:
        for method in converter_methods:
            method_object = method(self.condition)
            new_condition = method_object.convert()
            if new_condition != self.condition:
                self.condition = new_condition

        return self.condition


class EmptyString(IfStatementConverterMethod):

    def __init__(self, statement: str):
        self.statement = statement.strip()

    def _convert(self) -> str:
        pattern = r"(\w+)\s*==\s*(['\"]{2})"
        error = re.search(pattern, self.statement)
        if error is not None:
            variable = error.group(1)
            replaces = (r"''", r'""')
            for replace in replaces:
                self.statement = self.statement.replace(f"{variable} == {replace}", f"not {variable}")

        return self.statement


converter_methods = (
    EmptyString,
)
