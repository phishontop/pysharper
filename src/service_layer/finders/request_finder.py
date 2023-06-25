from src.service_layer.finders.abstract_finder import AbstractLibraryFinder
from src.domain.factories.request_factory import RequestFactory
import re


class RequestFinder(AbstractLibraryFinder):

    def __init__(self, text: str):
        self.text = text

    def _run_finder(self):
        request_objects = []
        methods = ("get", "post", "put", "patch", "delete")

        for method in methods:
            request = re.search(rf'(\w+)\s*=\s*requests\.{method}\((.*?)\)', self.text)
            if request is not None:
                request_objects.append(RequestFactory.create_from_string(
                    response_name=request.group(1),
                    method=method,
                    args=request.group(2)
                ))

        return request_objects


class ResponseFinder(AbstractLibraryFinder):

    def __init__(self, text: str, variable_name: str):
        self.text = text
        self.variable_name = variable_name

    def _run_finder(self):
        response_calls = re.findall(rf'{self.variable_name}\.[^\s()]+', self.text)
        return response_calls
