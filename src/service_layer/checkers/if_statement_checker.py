import copy

from src.service_layer.checkers.abstract_checker import AbstractChecker
from src.service_layer.finders.if_statement_finder import IfStatementFinder
from src.service_layer.converters.if_statement_converter import IfStatementConverter


class IfStatementChecker(AbstractChecker):

    def __init__(self, text: str):
        super().__init__(text=text)
        self.old_text = text
        self.new_text = text

    def _run_checks(self):
        statement_finder = IfStatementFinder(text=self.new_text)
        if_statements_found = statement_finder.run_finder()
        for if_statement in if_statements_found:
            converter = IfStatementConverter(copy.copy(if_statement))
            new_if_statement = converter.convert()

            self.new_text = self.new_text.replace(
                if_statement.line,
                new_if_statement.line
            )
