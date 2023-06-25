from src.domain.models import request_models
import ast


class RequestFactory:

    @staticmethod
    def create_from_string(
        response_name,
        method: str,
        args: str
    ) -> request_models.Request:
        """
        Proxy for the request_models.Request init dunder
        Creates and parses the proper args
        """
        new_args = {}
        for arg in args.split(","):
            arg_split = arg.strip().split("=")
            if len(arg_split) == 1:
                new_args["url"] = ast.literal_eval(arg_split[0])

            elif len(arg_split) == 2:
                new_args[arg_split[0]] = ast.literal_eval(arg_split[1])

        return request_models.Request(
            response_name=response_name,
            args=new_args,
            method=method
        )
