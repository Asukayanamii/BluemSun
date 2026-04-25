from controller.books_controller import BooksController
from entity.book import Book
from exception.exceptions import BookNotFoundException, DuplicateKeyException
from service.books_service import BooksService
from utils import log

def catch_global_exception(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            print(f"值错误:{e}")
        except BookNotFoundException as e:
            print(f"图书不存在")
        except DuplicateKeyException as e:
            print(f"图书已存在:{e}")
        except Exception as e:
            print(f"错误:{e}")
    return wrapper


def main():
    log.info("图书管理系统启动")
    # 初始化
    book_controller = BooksController()
    book_service = BooksService()
    wel = "欢迎使用图书管理系统"
    fun = """
    1. 添加图书
    2. 删除图书
    3. 修改图书
    4. 查询图书
    5. 查询所有图书
    6. 退出系统
    """
    print(f"{wel:-^40}")

    while True:
        try:
            print(f"{fun}")
            # 校验操作序号是否有效
            while True:
                try:
                    ops: int = int(input("请输入操作序号："))
                    if ops not in [1,2,3,4,5,6]:
                        raise ValueError
                    break
                except ValueError:
                    print("请输入有效数字")
            # 主循环
            match ops:
                case 1:
                    log.info("添加图书")
                    print("请依次输入添加图书的图书编号,书名,作者,数量")
                    # 校验信息是否合法
                    while True:
                        try:
                            id = input("请输入图书编号：")
                            if id == " ":
                                raise ValueError
                            book_has_existed = True
                            try:
                                book_service.get_book(id)
                            except BookNotFoundException:
                                book_has_existed = False
                            if book_has_existed:
                                raise DuplicateKeyException("图书编号已存在")
                            title = input("请输入书名：")
                            if title == " ":
                                raise ValueError
                            author = input("请输入作者：")
                            if author == " ":
                                raise ValueError
                            break
                        except ValueError:
                            print("请输入有效信息")
                    while True:
                        try:
                            num = int(input("请输入数量："))
                            if num < 0 or num > 10000:
                                raise ValueError
                            break
                        except ValueError:
                            print("请输入有效数字")
                    book = Book(id = id,title= title,author = author,number = num)
                    book_controller.add_book(book)
                case 2:
                    log.info("删除图书")
                    print("请选择1.按编号删除,2.按书名删除")
                    while True:
                        try:
                            ops: int = int(input("请输入操作序号："))
                            if ops not in [1,2]:
                                raise ValueError
                            break
                        except ValueError:
                            print("请输入有效数字")
                    if ops == 1:
                        while True:
                            try:
                                id = input("请输入图书编号：")
                                if id == " ":
                                    raise ValueError
                                break
                            except ValueError:
                                print("请输入有效编号")
                        book_controller.delete_book_by_id(id)
                    elif ops == 2:
                        while True:
                            try:
                                title = input("请输入书名：")
                                if title == " ":
                                    raise ValueError
                                break
                            except ValueError:
                                print("请输入有效书名")
                        book_controller.delete_book_by_title(title)

                case 3:
                    log.info("修改图书数量")
                    print("请选择1.按编号修改,2.按书名修改")
                    while True:
                        try:
                            ops: int = int(input("请输入操作序号："))
                            if ops not in [1,2]:
                                raise ValueError
                            break
                        except ValueError:
                            print("请输入有效数字")
                    id = None
                    title = None
                    if ops == 1:
                        while True:
                            try:
                                id = input("请输入要修改的图书编号：")
                                if id == " ":
                                    raise ValueError
                                break
                            except ValueError:
                                print("请输入有效编号")
                    elif ops == 2:
                        while True:
                            try:
                                title = input("请输入要修改的书名：")
                                if title == " ":
                                    raise ValueError
                                break
                            except ValueError:
                                print("请输入有效书名")
                    while True:
                        try:
                            num = int(input("请输入要修改的图书数量："))
                            if num < 0 or num > 10000:
                                raise ValueError
                            break
                        except ValueError:
                            print("请输入有效数字")
                    book_controller.update_book(Book(id = id,title= title,number = num,author = None))
                case 4:
                    log.info("查询图书")
                    print("请选择1.按编号查询,2.按书名查询")
                    id = None
                    title = None
                    while True:
                        try:
                            ops: int = int(input("请输入操作序号："))
                            if ops not in [1,2]:
                                raise ValueError
                            break
                        except ValueError:
                            print("请输入有效操作序号")
                    if ops == 1:
                        while True:
                            try:
                                id = input("请输入要查询的图书编号：")
                                if id == " ":
                                    raise ValueError
                                break
                            except ValueError:
                                print("请输入有效编号")
                    elif ops == 2:
                        while True:
                            try:
                                title = input("请输入书名：")
                                if title == " ":
                                    raise ValueError
                                break
                            except ValueError:
                                print("请输入有效书名")
                    book_controller.get_book(id, title)
                case 5:
                    log.info("查询所有图书")
                    book_controller.get_all_books()
                case 6:
                    break
        except ValueError as e:
            print(f"值错误:{e}")
        except BookNotFoundException as e:
            print(f"图书不存在")
        except DuplicateKeyException as e:
            print(f"图书已存在:{e}")
        except Exception as e:
            print(f"错误:{e}")


if __name__ == '__main__':
    main()