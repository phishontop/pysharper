from src.service_layer.converters.abstract_converter import AbstractConverter
from src.service_layer.finders import for_finder, unassigned_variable_finder
from src.service_layer.creators import function_creator
from src.domain.models import classes


class ClassConverter(AbstractConverter):

    def __init__(
        self,
        class_object: classes.Class,
        target_function_object: classes.Function
    ):
        self.class_object = class_object
        self.target_function_object = target_function_object

    def _convert(self):
        # TODO: Finish the class converter off
        for_loop_finder = for_finder.ForFinder(text=self.target_function_object.content)
        for_loops = for_loop_finder.run_finder()
        for loop in for_loops:
            creator = function_creator.ForLoopMethod(
                function=self.target_function_object,
                loop=loop
            )

            func_text = "\n".join(creator.create())
            variable_finder = unassigned_variable_finder.VariableFinder(func_text)
            variable_finder.run_finder()

