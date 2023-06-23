from src.service_layer.checkers.abstract_checker import AbstractChecker
from src.service_layer.finders.class_finder import ClassFinder
from src.service_layer.converters.class_converter import ClassConverter
from src.domain.models import classes
from typing import List


class ClassChecker(AbstractChecker):

    def __init__(self, text: str):
        super().__init__(text=text)
        self.old_text = text
        self.new_text = text

    @staticmethod
    def _check_class(class_object: classes.Class):
        new_class_object = None
        for function in class_object.functions:
            if function.get_nest_count() > 4:
                converter = ClassConverter(class_object, function)
                new_class_object = converter.convert()

        return new_class_object

    def _run_checks(self):
        finder = ClassFinder(text=self.new_text)
        classes_found = finder.run_finder()

        for class_found in classes_found:
            converted_class = self._check_class(class_found)
