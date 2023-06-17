from src.adapter.repository import FileRepository


class FileUnitOfWork:

    def __init__(self):
        self.repository = FileRepository

    def read_file(self, file: str):
        return self.repository.get_file_content(path=file)

    def write_to_file(self, file: str, content: str):
        self.repository.write_to_file(path=file, content=content)
