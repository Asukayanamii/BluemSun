# 图书管理系统 (Book Management System)

一个基于Python的控制台图书管理系统，采用经典的三层架构设计，实现图书的增删改查功能。

## 功能特性

    - **图书管理**: 支持图书的添加、删除、修改和查询
    - **多种查询方式**: 可按图书编号或书名进行精确查询
    - **批量操作**: 支持查询所有图书列表
    - **数据持久化**: 使用JSON文件存储图书数据
    - **中文友好**: 支持中文书名拼音排序
    - **输入验证**: 对用户输入进行严格验证和异常处理

## 技术栈

- **Python 3.10+**: 主要编程语言
- **Pydantic**: 数据模型验证和序列化
- **PyPinyin**: 中文拼音转换，用于中文书名排序
- **JSON**: 数据存储格式

## 项目结构

```
week2/
├── main.py                    # 程序入口，控制台交互界面
├── README.md                  # 项目说明文档
├── books/                     # 数据存储目录
│   ├── books.json            # 图书数据文件
│   └── books_template.json   # 数据模板文件
├── controller/                # 控制层
│   ├── __init__.py
│   └── books_controller.py   # 图书控制器
├── dao/                       # 数据访问层
│   ├── __init__.py
│   └── books_dao.py          # 图书数据访问对象
├── entity/                    # 实体层
│   ├── __init__.py
│   └── book.py               # 图书实体类
├── exception/                 # 异常处理
│   ├── __init__.py
│   └── exceptions.py         # 自定义异常类
├── service/                   # 业务逻辑层
│   ├── __init__.py
│   └── books_service.py      # 图书服务类
└── utils/                     # 工具类
    ├── __init__.py
    ├── book_file_utils.py    # 文件操作工具
    └── log.py                # 日志工具
```

## 设计亮点

### 1. 清晰的三层架构
- **Controller层**: 负责用户交互和请求转发，处理控制台输入输出
- **Service层**: 封装业务逻辑，处理业务规则和异常
- **DAO层**: 负责数据访问，实现与JSON文件的交互

### 2. 完善的异常处理机制
- 自定义异常类（`BookNotFoundException`, `DuplicateKeyException`）
- 全局异常捕获装饰器，统一处理各种异常情况
- 友好的错误提示信息

### 3. 数据模型验证
- 使用Pydantic的`BaseModel`定义图书实体
- 自动类型验证和数据序列化
- 支持可选字段，灵活适应不同查询场景

### 4. 中文友好设计
- 利用PyPinyin库实现中文书名的拼音排序
- 添加图书时自动按书名拼音排序保存
- 支持中文输入和显示

### 5. 数据持久化
- 使用JSON文件存储数据，便于查看和备份
- 自动创建数据文件和初始化数据
- 文件操作封装在工具类中，提高代码复用性

### 6. 输入验证与用户体验
- 严格的输入验证（非空检查、数值范围、有效选项）
- 清晰的用户操作指引
- 操作日志记录，便于追踪系统状态

## 快速开始

### 环境要求
- Python 3.10或更高版本
- 依赖包：pydantic, pypinyin

### 安装依赖
```bash
pip install pydantic pypinyin
```

### 运行程序
```bash
python main.py
```

## 使用示例
可以以books/books_template.json文件作为数据模板，
将图书信息格式化为json格式并命名为books.json来批量导入图书信息，
若不存在books.json， 运行程序后，
会自动创建books.json文件并初始化数据。

启动程序后，系统显示如下菜单：
```
欢迎使用图书管理系统
1. 添加图书
2. 删除图书
3. 修改图书
4. 查询图书
5. 查询所有图书
6. 退出系统
```

### 添加图书
选择操作1，依次输入图书编号、书名、作者和数量。系统会自动检查编号是否重复，并按书名拼音排序保存。

### 查询图书
支持两种查询方式：
1. 按图书编号查询
2. 按书名查询

### 修改图书
可修改图书的数量信息，支持按编号或书名定位图书。

### 删除图书
支持按编号或书名删除图书。

### 批量查询
选择操作5可查看所有图书列表，按书名拼音排序显示。

## 代码示例

### 实体类定义
```python
from pydantic import BaseModel

class Book(BaseModel):
    id: str | None
    title: str | None
    author: str | None
    number: int | None
```

### 中文拼音排序
```python
from pypinyin import lazy_pinyin

# 按书名拼音排序
sorted_books = sorted(books_list, key=lambda x: lazy_pinyin(x["title"]))
```

### 全局异常处理
```python
def catch_global_exception(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            print(f"值错误:{e}")
        except BookNotFoundException as e:
            print(f"图书不存在")
        # ... 其他异常处理
    return wrapper
```

## 项目特色总结

1. **架构规范**: 严格遵循MVC模式，代码结构清晰，便于维护和扩展
2. **工程化实践**: 包含完整的异常处理、日志记录、输入验证等工程化要素
3. **实用功能**: 针对中文环境的拼音排序，提升用户体验
5. **轻量级**: 无需数据库，JSON文件存储，部署简单

## 未来扩展建议

1. 添加Web界面，使用Flask或FastAPI框架
2. 支持更多查询条件（作者、数量范围等）
3. 添加数据导入导出功能（Excel、CSV格式）
4. 实现用户认证和权限管理
5. 添加数据统计和报表功能

## 许可证

本项目为培训作业项目，仅供学习和参考使用。