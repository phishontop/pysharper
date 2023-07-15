import re

from typing import Type, Tuple

from src.domain.models import if_statement
from src.service_layer.converters.abstract_converter import (
    AbstractConverter,
    IfStatementConverterMethod
)

eq_reverse_table = {
    "!=": "==",
    "==": "!="
}


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
            method_object = method(self.condition.strip())
            new_condition = method_object.convert()
            if new_condition != self.condition:
                self.condition = new_condition

        return self.condition


class EmptyString(IfStatementConverterMethod):

    def __init__(self, statement: str):
        self.statement = statement

    def _convert(self) -> str:
        pattern = r"(\w+)\s*==\s*(['\"]{2})"
        error = re.search(pattern, self.statement)
        if error is not None:
            variable = error.group(1)
            replaces = (r"''", r'""')
            for replace in replaces:
                self.statement = self.statement.replace(f"{variable} == {replace}", f"not {variable}")

        return self.statement


class LenDataType(IfStatementConverterMethod):

    def __init__(self, statement: str):
        self.statement = statement

    def _convert(self):
        methods = ((">", ""), ("==", "not "))
        for method in methods:
            pattern = rf"len\((\w+)\) {method[0]} 0"
            error = re.search(pattern, self.statement)
            if error is not None:
                return method[1] + error.group(1)

        return self.statement


class BoolValueConverter(IfStatementConverterMethod):

    def __init__(self, statement: str):
        self.statement = statement

    def _convert(self):
        pattern = r"== (False|True)$"
        match = re.search(pattern, self.statement)

        if match is not None:
            value = match.group(1)
            self.statement = re.sub(pattern, "", self.statement)

            if value == "False":
                self.statement = f"not {self.statement}"

        return self.statement.strip()


class BoolEqualConverter(IfStatementConverterMethod):

    def __init__(self, statement: str):
        self.statement = statement

    def _convert(self):
        split_statement = self.statement.split()
        if (
            len(split_statement) == 4 and
            split_statement[0] == "not" and
            split_statement[2] in eq_reverse_table
        ):
            split_statement[2] = eq_reverse_table[split_statement[2]]
            split_statement.pop(0)

        return " ".join(split_statement)


converter_methods = (
    EmptyString,
    LenDataType,
    BoolValueConverter,
    BoolEqualConverter
)
