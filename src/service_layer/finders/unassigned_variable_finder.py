from src.service_layer.finders.abstract_finder import AbstractDataStructureFinder
import tokenize
import io


class VariableFinder(AbstractDataStructureFinder):

    def __init__(self, text: str):
        self.text = text

    def _run_finder(self):
        tokens = tokenize.tokenize(io.BytesIO(self.text.encode('utf-8')).readline)
        for token in tokens:
            if token[0] == tokenize.NAME:
                print(token[1])
