from dataclasses import dataclass
from http.client import HTTPConnection, HTTPSConnection


@dataclass
class Request:
    response_name: str
    method: str
    args: dict

    def convert_to_code(self) -> list:
        arg_list_pairs = [
            f"{name}={value}"
            for name, value in self.args.items()
            if name != "url"
        ]

        new_strings = []
        for string_method in ('"', "'"):
            args_string = f"{string_method}{self.args['url']}{string_method}, {', '.join(arg_list_pairs)}"
            new_strings.append(f"{self.response_name} = requests.{self.method}({args_string})")

        return new_strings

    @property
    def url(self):
        return self.args["url"]

    @property
    def request_type(self):
        return self.url.split("://")[0]

    @property
    def host(self):
        return self.url.split("/")[2]

    @property
    def path(self):
        return f'/{"/".join(self.url.split("/")[3:])}'

    @property
    def http_client_object(self) -> str:
        client_table = {
            "http": "http.client.HTTPConnection('{}')",
            "https": "http.client.HTTPSConnection('{}')"
        }

        return client_table[self.request_type]
