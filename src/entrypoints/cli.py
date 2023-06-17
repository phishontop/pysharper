from argparse import ArgumentParser

from src.service_layer.master_services.service_runner import MasterServiceRunner
from src.domain.commands import refactor


def get_args():
    parser = ArgumentParser()

    parser.add_argument(
        "-f", "--file",
        help="target file to run pysharper on",
        metavar="<file>"
    )

    parser.add_argument(
        "-o", "--output",
        help="output file to put the finished refactored code",
        metavar="<file>",
        nargs="?",
        type=str,
        const=1,
        default="output.py"
    )

    return parser.parse_args()


def main():
    args = get_args()
    command = refactor.Refactor(
        target_file=args.file,
        output_file=args.output
    )

    service_controller = MasterServiceRunner(cmd=command)
    service_controller.run_checkers()

    print("Finished Running Checkers")
