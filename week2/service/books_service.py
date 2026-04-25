from dao.books_dao import BooksDAO
from entity.book import Book
from exception.exceptions import BookNotFoundException
from utils import log


class BooksService:
    def __init__(self):
        self.books_dao = BooksDAO()

    def add_book(self, book):
        self.books_dao.add_book(book)
        log.info(f"添加图书成功：{book}")

    def delete_book_by_id(self, book_id):
        result = self.books_dao.delete_book_by_id(book_id)
        if result:
            log.info(f"删除图书成功：{book_id}")
        else:
            raise BookNotFoundException

    def delete_book_by_title(self, book_title):
        result = self.books_dao.delete_book_by_title(book_title)
        if result:
            log.info(f"删除图书成功：{book_title}")
        else:
            raise BookNotFoundException

    def update_book(self, book : Book):
        get_book = self.books_dao.get_book(book.id if book.id else book.title)
        get_book.number = book.number
        if get_book:
            self.books_dao.update_book(book)
            log.info(f"修改图书成功")
        else:
            raise BookNotFoundException

    def get_book(self, book_id : str = None, book_title : str = None):
        book = self.books_dao.get_book(book_id, book_title)
        if book:
            log.info(f"查询图书成功：{book}")
            return book
        else:
            raise BookNotFoundException

    def get_all_books(self):
        books = self.books_dao.get_all_books()
        log.info(f"查询所有图书成功")
        if len( books) > 0:
            print(f"查询所有图书成功：{books}")
        else:
            print("暂无图书")
        return books

