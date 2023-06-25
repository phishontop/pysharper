import io

from src.service_layer.checkers.abstract_checker import AbstractChecker
from src.service_layer.finders.request_finder import (
    RequestFinder,
    ResponseFinder
)

from src.service_layer.converters import (
    response_to_httpclient,
    requests_to_httpclient
)


class RequestToHttpclientChecker(AbstractChecker):

    def __init__(self, text: str):
        super().__init__(text=text)
        self.old_text = text
        self.new_text = self.old_text.replace("import requests", "import json\nimport http.client")

    def _create_requests(self, request):
        clients_added = []
        request_converter = requests_to_httpclient.RequestToHttpclientConverter(
            request_object=request
        )

        clients = requests_to_httpclient.RequestToHttpclientConverter.clients
        for host, client in clients.items():
            if client not in clients_added:
                new_string = f"import http.client\n\n{client[1]} = {client[0].format(host)}"

                self.new_text = self.new_text.replace("import http.client", new_string)
                clients_added.append(client)

        self.new_text = request_converter.add_to_text(text=self.new_text)

    def _parse_response_calls(self, request):
        call_finder = ResponseFinder(text=self.new_text, variable_name=request.response_name)
        calls = call_finder.run_finder()

        response_converter = response_to_httpclient.ResponseToHttpclientConverter(
            calls=calls
        )

        self.new_text = response_converter.add_to_text(
            text=self.new_text,
            request=request
        )

    def _run_checks(self):
        request_finder = RequestFinder(text=self.new_text)
        requests = request_finder.run_finder()
        for request in requests:
            self._create_requests(request=request)
            self._parse_response_calls(request=request)

        return self.new_text
