import re

from src.service_layer.finders import abstract_finder
from src.domain.models import if_statement


class IfStatementFinder(abstract_finder.AbstractBuiltinFinder):

    def __init__(self, text: str):
        self.text = text

    def _run_finder(self):
        statements = re.findall(
            pattern=r'(if|elif)\s+(.*?)(?=:|$)',
            string=self.text,
            flags=re.MULTILINE | re.DOTALL
        )

        statement_list = []
        for statement in statements:
            conditions = re.split(r'\b(and|or)\b', statement[1])
            statement_list.append(if_statement.IfStatement(
                statements=conditions,
                start_keyword=statement[0]
            ))

        return statement_list
