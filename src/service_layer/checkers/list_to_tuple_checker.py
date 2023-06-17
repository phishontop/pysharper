from src.service_layer.checkers.abstract_checker import AbstractChecker
from src.service_layer.converters.list_to_tuple import ListToTupleConverter
from src.service_layer.finders.list_finder import ListFinder


class ListToTupleChecker(AbstractChecker):

    def __init__(self, text: str):
        self.old_text = text
        self.new_text = text

    def _run_checks(self):
        list_finder = ListFinder(text=self.new_text)
        lists_found = list_finder.run_finder()
        for list_ds in lists_found:
            if not list_ds.methods_called:
                converter = ListToTupleConverter(code=self.new_text, variable_name=list_ds.name)
                self.new_text = converter.convert()
