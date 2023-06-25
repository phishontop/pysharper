from src.service_layer.converters.abstract_converter import AbstractConverter, HttpclientConverterMethod
from src.domain.models import request_models
from typing import List, Dict, Tuple


def find_indent(words: str, sub_word: str) -> str:
    for line in words.splitlines():
        if sub_word in line:
            return line.split(sub_word)[0]

    return ""


class GetRequestConverter(HttpclientConverterMethod):

    def __init__(
        self,
        client_variable: str,
        request_object: request_models.Request
    ):
        self.client_variable = client_variable
        self.request_object = request_object

    def _convert(self):
        return f"""{self.client_variable}.{self.convert_to_get_request()}"""


converter_table = {
    "get": GetRequestConverter
}


class RequestToHttpclientConverter(AbstractConverter):
    clients: Dict[str, Tuple[str, str]] = {}

    def __init__(
        self,
        request_object: request_models.Request
    ):
        self.request_object = request_object

        if request_object.host not in RequestToHttpclientConverter.clients:
            RequestToHttpclientConverter.clients[request_object.host] = (
                request_object.http_client_object,
                f"{self.request_object.host}_connection".replace(".", "_")
            )

        self.variable = RequestToHttpclientConverter.clients[self.request_object.host][1]

    def _convert(self):
        converter_method = converter_table[self.request_object.method]

        converter_object = converter_method(
            client_variable=self.variable,
            request_object=self.request_object
        )

        request_code = converter_object.convert()
        return request_code

    def add_to_text(self, text: str):
        """Replaces the request_object value to the convert func result"""
        new_request = self._convert()
        indent_string = None

        new_response = f"{self.request_object.response_name} = {self.variable}.getresponse()"
        old_requests = self.request_object.convert_to_code()

        for old_request in old_requests:
            if indent_string is None:
                indent_string = find_indent(
                    text.replace(old_request, new_request),
                    new_request
                )

            text = text.replace(old_request, f"{new_request}\n{indent_string}{new_response}")

        return text
