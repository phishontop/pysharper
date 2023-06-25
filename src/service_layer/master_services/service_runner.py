from typing import List, Type

from src.service_layer.checkers import (
    list_to_tuple_checker,
    abstract_checker,
    if_statement_checker,
    request_to_httpclient_checker
)
from src.service_layer.uow import file_uow
from src.domain.commands import refactor


checkers: List[Type[abstract_checker.AbstractChecker]] = [
    list_to_tuple_checker.ListToTupleChecker,
    if_statement_checker.IfStatementChecker,
    request_to_httpclient_checker.RequestToHttpclientChecker
]


class MasterServiceRunner:
    """Runs and controls all the services in the service_layer"""

    def __init__(self, cmd: refactor.Refactor):
        self.cmd = cmd
        self.file_uow = file_uow.FileUnitOfWork()

    def get_input_code(self):
        content = self.file_uow.read_file(self.cmd.target_file)
        return content

    def save_new_code(self, code: str):
        self.file_uow.write_to_file(
            file=self.cmd.output_file,
            content=code
        )

    def run_checkers(self):
        code = self.get_input_code()
        for checker in checkers:
            checker_object = checker(code)
            checker_object.run_checks()
            if checker_object.has_changed():
                print("Code has changed")
                code = checker_object.new_text

        self.save_new_code(code=code)
