import re

from src.domain.models import datastructure
from src.service_layer.finders import abstract_finder


class ListFinder(abstract_finder.AbstractDataStructureFinder):

    def __init__(self, text: str):
        self.text = text

    def _run_finder(self):
        data_structure_list = []
        list_vars = re.findall(r'\b(\w+)\s*=\s*\[[^\]]*\]', self.text)
        for var in list_vars:
            method_regex = rf'\b{re.escape(var)}\s*\.\s*(\w+)\([^\)]*\)'
            methods = re.findall(method_regex, self.text)
            data_structure_list.append(datastructure.DataStructure(
                type="list",
                name=var,
                methods_called=methods
            ))

        return data_structure_list
