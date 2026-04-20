from week2.entity.book import Book
from week2.service.books_service import BooksService


class BooksController:
    def __init__(self):
        self.books_service = BooksService()

    def add_book(self, book : Book):
        self.books_service.add_book(book)
        print(f"添加图书成功：{book}")

    def get_book(self, book_id : str = None, book_title : str = None):
        book = self.books_service.get_book(book_id, book_title)
        print(f"查询图书成功：{book}")
        return book

    def get_all_books(self):
        return self.books_service.get_all_books()

    def update_book(self, book : Book):
        self.books_service.update_book(book)
        print(f"修改图书成功：{book}")

    def delete_book_by_id(self, book_id : str):
        self.books_service.delete_book_by_id(book_id)
        print(f"删除图书成功：{book_id}")

    def delete_book_by_title(self, book_title : str):
        self.books_service.delete_book_by_title(book_title)
        print(f"删除图书成功：{book_title}")
