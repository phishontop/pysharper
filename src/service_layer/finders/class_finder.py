from src.service_layer.finders.abstract_finder import AbstractBuiltinFinder
from src.service_layer.finders.function_finder import FunctionFinder
from src.domain.models import classes
import re


class ClassFinder(AbstractBuiltinFinder):

    def __init__(self, text: str):
        self.text = text

    def _run_finder(self):
        # noinspection SpellCheckingInspection
        pattern = r"class\s+(\w+):\s*(.*?)\n\s*def\s+(\w+)\((.*?)\):([\s\S]*?)(?=\nclass|\Z)"
        class_names = [class_found.group(1) for class_found in re.finditer(pattern, self.text)]
        class_list = []
        for class_name in class_names:
            class_pattern = rf"class\s+{class_name}:([\s\S]+?)(?=class|\Z)"
            class_match = re.search(class_pattern, self.text, re.MULTILINE)

            function_finder = FunctionFinder(class_match)
            functions = function_finder.run_finder()
            class_list.append(classes.Class(
                name=class_name,
                functions=functions
            ))

        return class_list
