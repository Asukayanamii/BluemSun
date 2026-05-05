import pymysql

# 题目 3：PyMySQL 参数化防注入
# 使用 PyMySQL 连接 music 数据库（使用字典游标）。
print("题目 3：PyMySQL 参数化防注入")
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '870218',
    'database': 'music',
    'charset': 'utf8mb4'
}
if __name__ == '__main__':
    print("使用 PyMySQL 连接 music 数据库（使用字典游标）。")
    connection = pymysql.connect(**DB_CONFIG)
    # 插入一条测试歌手：姓名'测试歌手'，性别'保密'，年龄20，手机'13800000099'，出道年份2020，代表作'测试歌曲'。
    print("插入一条测试歌手：姓名'测试歌手'，性别'保密'，年龄20，手机'13800000099'，出道年份2020，代表作'测试歌曲'。")
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO singers (name, gender, age, phone, debut_year, representative_song) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, ('测试歌手', '保密', 20, '13800000099', 2020, '测试歌曲'))
            connection.commit()
            print("数据插入成功！")
            # 定义恶意输入："测试歌手' OR '1'='1"
            # 错误方式：用f - string拼接SQL，查询名字等于该恶意输入的歌手，打印所有结果。
            print("错误方式：用f - string拼接SQL，查询名字等于该恶意输入的歌手，打印所有结果。")
            name = "测试歌手' OR '1'='1"
            sql = f"SELECT * FROM singers WHERE name = '{name}'"
            cursor.execute(sql)
            results = cursor.fetchall()
            for result in results:
                print(result)
            # 正确方式：用 % s占位符和参数元组查询，打印结果。
            print("正确方式：用 % s占位符和参数元组查询，打印结果。")
            sql = "SELECT * FROM singers WHERE name = %s"
            cursor.execute(sql, (name,))
            results = cursor.fetchall()
            for result in results:
                print(result)
            # 在注释中写清楚：为什么参数化能防注入？
            #参数化查询能防止 SQL 注入的核心原因是：SQL 语句和数据完全分离处理。
            # 数据库永远不会将用户输入解析为 SQL 代码，
            # 无论输入什么内容，都只会被当作纯数据处理。
    except Exception as e:
        print(f"数据插入失败：{e}")