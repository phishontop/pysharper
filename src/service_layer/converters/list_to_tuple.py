import re

from src.service_layer.converters.abstract_converter import AbstractConverter


class ListToTupleConverter(AbstractConverter):

    def __init__(self, variable_name: str, code: str):
        self.variable_name = variable_name
        self.code = code

    def _convert(self):
        search_pattern = rf'\b{re.escape(self.variable_name)}\s*=\s*(\[[^\]]*\])'
        result = re.search(search_pattern, self.code)

        list_content = result.group(1)
        new_content = tuple(eval(list_content))

        return re.sub(search_pattern, f'{self.variable_name} = {new_content}', self.code)
