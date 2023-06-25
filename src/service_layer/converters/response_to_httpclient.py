from src.service_layer.converters.abstract_converter import HttpclientResponseConverterMethod, AbstractConverter
from typing import List

import io


class JsonEncodingConverter(HttpclientResponseConverterMethod):

    def __init__(self, variable_name):
        self.variable_name = variable_name

    def _convert(self):
        return f"json.loads({self.variable_name}.read().decode())"


method_table = {
    "json": JsonEncodingConverter
}


class ResponseToHttpclientConverter(AbstractConverter):

    def __init__(self, calls: List[str]):
        self.calls = calls

    def _convert(self):
        new_code = []
        for call in self.calls:
            name, call = call.split(".")
            method_callable = method_table.get(call)
            if method_callable is not None:
                method_object = method_callable(variable_name=name)
                new_code.append((call, method_object.convert()))

        return new_code

    def add_to_text(self, text: str, request):
        responses = self._convert()
        for response in responses:
            replace_string = f"{request.response_name}.{response[0]}"
            text = text.replace(f"{replace_string}()", response[1])
            text = text.replace(replace_string, response[1])

        return text
