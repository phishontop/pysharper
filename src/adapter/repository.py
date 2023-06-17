

class FileRepository:

    @staticmethod
    def get_file_content(path: str):
        with open(path, "r") as file:
            return file.read()

    @staticmethod
    def write_to_file(path: str, content: str):
        with open(path, "w") as file:
            file.write(content)
