from src.service_layer.converters.abstract_converter import AbstractConverter
from src.domain.models import request_models
from typing import List, Dict, Tuple


def find_indent(words: str, sub_word: str) -> str:
    for line in words.splitlines():
        if sub_word in line:
            return line.split(sub_word)[0]

    return ""


def get_request_converter(
    client_variable: str,
    request_object: request_models.Request
) -> str:
    args = ", ".join([
        f'"GET"',
        f'"{request_object.path}"',
        f"headers={request_object.args['headers']}"
    ])

    return f"{client_variable}.request({args})"


def payload_request_converter(
    client_variable: str,
    request_object: request_models.Request
) -> str:
    args = ", ".join([
        f'"{request_object.method.upper()}"',
        f'"{request_object.path}"',
        f"body={request_object.args['body']}"
        f"headers={request_object.args['headers']}"
    ])

    return f"{client_variable}.request({args})"


converter_table = {
    "get": get_request_converter,
    "post": payload_request_converter,
    "put": payload_request_converter,
    "patch": payload_request_converter,
    "delete": payload_request_converter
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

        return converter_method(
            client_variable=self.variable,
            request_object=self.request_object
        )

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
