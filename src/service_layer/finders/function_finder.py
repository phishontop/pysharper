from src.service_layer.finders.abstract_finder import AbstractBuiltinFinder
from src.domain.models import classes
import re


class FunctionFinder(AbstractBuiltinFinder):

    def __init__(self, class_match):
        self.class_match = class_match

    def _run_finder(self):
        function_pattern = r"def\s+(\w+)\((.*?)\):([\s\S]*?)(?=def|\Z)"
        functions = re.findall(function_pattern, self.class_match.group(1), re.MULTILINE)
        return [
            classes.Function(
                name=function_info[0],
                arguments=function_info[1].split(", "),
                content=function_info[2]
            )
            for function_info in functions
        ]
