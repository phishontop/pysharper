from src.service_layer.finders.abstract_finder import AbstractBuiltinFinder
from src.domain.models import for_bultin

import re


class ForFinder(AbstractBuiltinFinder):

    def __init__(self, text: str):
        self.text = text

    def _run_finder(self):
        for_loops = re.findall(r"\bfor\s+(\w+)\s+in\s+(.+):", self.text, re.MULTILINE)
        return [for_bultin.ForBuiltin(*for_loop) for for_loop in for_loops]
