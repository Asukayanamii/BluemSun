import json
import os

from . import log


def save_books_list(books_list : list):
    try:
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file_path = os.path.join(base_dir , "books" , "books.json")
        with open(file_path, "w" , encoding="utf-8") as f:
            json.dump(books_list , f,ensure_ascii=False,indent=4)
            log.info("保存图书列表成功")
    except Exception as e:
        log.info(f"保存图书列表失败：{e}")

def load_books_list():
    try:
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file_path = os.path.join(base_dir, "books" ,  "books.json")
        with open(file_path, "r" , encoding="utf-8") as f:
            books_list = json.load(f)
            log.info("加载图书列表成功")
    except FileNotFoundError:
        log.info("图书列表不存在,已启动初始化")
        books_list = []
        save_books_list(books_list)
        log.info("初始化图书列表成功,请检查项目下的books文件夹")
    return books_list