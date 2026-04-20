class BookNotFoundException(Exception):
    def __init__(self, message = "图书不存在"):
        super().__init__(message)

class DuplicateKeyException(Exception):
    def __init__(self, message = "图书已存在"):
        super().__init__(message)