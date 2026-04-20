from week2.entity.book import Book
from week2.utils.book_file_utils import load_books_list, save_books_list
from pypinyin import lazy_pinyin

class BooksDAO:
    book_list = []
    def __init__(self):
        BooksDAO.book_list = load_books_list()
    def add_book(self, book : Book):
        self.book_list.append(book.model_dump())
        BooksDAO.book_list = sorted(BooksDAO.book_list, key=lambda x: lazy_pinyin(x["title"]))
        save_books_list(self.book_list)

    def get_book(self, book_id : str = None,book_title : str = None):
        for book_json in self.book_list:
            book = Book(**book_json)
            if book_id:
                if book.id == book_id:
                    return book
            elif book_title:
                if book.title == book_title:
                    return book
        return None

    def get_all_books(self):
        return self.book_list

    def update_book(self,book : Book):
        for i in range(len(self.book_list)):
            if self.book_list[i]["id"] == book.id:
                self.book_list[i] = book.model_dump()
                save_books_list(self.book_list)
                return True
        return False

    def delete_book_by_id(self, book_id : str):
        for i in range(len(self.book_list)):
            if self.book_list[i]["id"] == book_id:
                self.book_list.pop(i)
                save_books_list(self.book_list)
                return True
        return False

    def delete_book_by_title(self, book_title : str):
        for i in range(len(self.book_list)):
            if self.book_list[i]["title"] == book_title:
                self.book_list.pop(i)
                save_books_list(self.book_list)
                return True
        return False

if __name__ == '__main__':
    dump = Book(id = "1",title = "1",author = "1",number = 1).model_dump()
    print( dump)