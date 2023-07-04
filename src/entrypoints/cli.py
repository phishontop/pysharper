from argparse import ArgumentParser

from src.service_layer.master_services.service_runner import MasterServiceRunner
from src.domain.commands import refactor


def parse_arguments():
    parser = ArgumentParser()

    parser.add_argument(
        "-f", "--file",
        help="target file to run pysharper on",
        metavar="<file>"
    )

    parser.add_argument(
        "-o", "--output",
        help="output file to put the finished refactored code",
        metavar="<file>"
    )

    return parser.parse_args()


def main():
    args = parse_arguments()
    command = refactor.Refactor(
        target_file=args.file,
        output_file=args.output
    )

    if command.target_file is None:
        raise refactor.RefactorArgumentError("--file or -f has not been defined")

    if command.output_file is None:
        raise refactor.RefactorArgumentError("--output or -o has not been defined")

    service_controller = MasterServiceRunner(cmd=command)
    service_controller.run_checkers()

    print("Finished Running Checkers")
