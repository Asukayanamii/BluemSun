from sqlalchemy import create_engine, String, Integer, select
from sqlalchemy.orm import Session, DeclarativeBase, Mapped, mapped_column

DB_URL = 'mysql+pymysql://root:870218@localhost/music'

engine = create_engine(DB_URL, echo=True)

class Base(DeclarativeBase):
    pass

class Singer(Base):
    __tablename__ = 'singers'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    gender : Mapped[str] = mapped_column(String(2))
    phone : Mapped[str] = mapped_column(String(11))
    age: Mapped[int] = mapped_column(Integer)
    debut_year: Mapped[int] = mapped_column(Integer)
    representative_song : Mapped[str] = mapped_column(String(50))
    def __repr__(self):
        return f"Singer(id={self.id}, name={self.name}, gender={self.gender}, phone={self.phone}, age={self.age}, debut_year={self.debut_year}, representative_song={self.representative_song})"

def create_base():
    Base.metadata.create_all(engine)

if __name__ == '__main__':
    create_base()
    session = Session(engine)
    singers = [
        Singer(name='周杰伦', gender='男', age=45, phone='13800000001', debut_year=2000, representative_song='七里香'),
        Singer(name='林俊杰', gender='男', age=43, phone='13800000002', debut_year=2003, representative_song='江南'),
        Singer(name='邓紫棋', gender='女', age=32, phone='13800000003', debut_year=2008, representative_song='光年之外'),
        Singer(name='刘若英', gender='女', age=53, phone='13800000004', debut_year=1995, representative_song='后来'),
        Singer(name='李荣浩', gender='男', age=38, phone='13800000005', debut_year=2010, representative_song='年少有为')
    ]
    try:
        # 插入数据
        print("开始插入数据...")
        session.add_all(singers)
        session.commit()
        print("所有歌手数据插入成功！")
        # 查询年龄大于30的歌手
        print("查询年龄大于30的歌手")
        query_result = select(Singer).where(Singer.age > 30)
        result =session.scalars(query_result).all()
        print(f"查询结果：{result}")
        # 查询所有女歌手，打印姓名和代表作
        print("查询所有女歌手，打印姓名和代表作")
        where = select(Singer).where(Singer.gender == '女')
        where__all = session.scalars(where).all()
        for singer in where__all:
            print(f"姓名：{singer.name}，代表作：{singer.representative_song}")
        # 排序查询：查询所有歌手，按出道年份升序排列，打印姓名和出道年份。
        print("排序查询：查询所有歌手，按出道年份升序排列，打印姓名和出道年份。")
        select(Singer).order_by(Singer.debut_year.asc())
        result = session.scalars(select(Singer).order_by(Singer.debut_year.asc())).all()
        for singer in result:
            print(f"姓名：{singer.name}，出道年份：{singer.debut_year}")
        # 更新操作：把“周杰伦”的年龄修改为46。
        print("更新操作：把“周杰伦”的年龄修改为46。")
        update_result = session.query(Singer).filter(Singer.name == '周杰伦').update({'age': 46})
        if update_result:
            session.commit()
            print("更新成功！")
        # 更新代表作：把“邓紫棋”的代表作改为“泡沫”。
        print("更新代表作：把“邓紫棋”的代表作改为“泡沫”。")
        update_result = session.query(Singer).filter(Singer.name == '邓紫棋').update({'representative_song': '泡沫'})
        if update_result:
            session.commit()
            print("更新成功！")
        # 手机号查重练习：尝试插入“刘德华”，男，55
        # 岁，手机号
        # 13800000001，出道年份
        # 1985，代表
        # 作《忘情水》。
        print("手机号查重练习：尝试插入“刘德华”，男，55岁，手机号13800000001，出道年份1985，代表《忘情水》。")
        insert_result = session.query(Singer).filter(Singer.phone == '13800000001').first()
        if insert_result:
            print(f"插入失败：手机号 {insert_result.phone} 已存在")
        else:
            session.add(Singer(name='刘德华', gender='男', age=55, phone='13800000001', debut_year=1985, representative_song='《忘情水》'))
            session.commit()
            print("插入成功！")
        # 用同样的查重逻辑插入“陈奕迅”，男，50
        # 岁，手机号
        # 13800000006，出道年份
        # 1996，代表作
        # 《十年》，应该成功。
        print("用同样的查重逻辑插入“陈奕迅”，男，50岁，手机号13800000006，出道年份1996，代表作《十年》，应该成功。"
              )
        insert_result = session.query(Singer).filter(Singer.phone == '13800000006').first()
        if insert_result:
            print(f"插入失败：手机号 {insert_result.phone} 已存在")
        else:
            session.add(Singer(name='陈奕迅', gender='男', age=50, phone='13800000006', debut_year=1996, representative_song='《十年》'))
            session.commit()
            print("插入成功！")
        # 删除“邓紫棋”。
        print("删除“邓紫棋”")
        delete_result = session.query(Singer).filter(Singer.name == '邓紫棋').delete()
        if delete_result:
            session.commit()
            print("删除成功！")
        else:
            print("删除失败")
        # 再次查询表中所有歌手，打印验证。
        print("再次查询表中所有歌手，打印验证。")
        for singer in session.scalars(select(Singer)):
            print(singer)
        session.close()
        session = Session(engine)
        # 题目2：事务自动回滚
        print("题目2：事务自动回滚")
        # 在事务块内，先查询手机号
        # 13800000006
        # 是否存在（应该不存在），然后插入“王菲”，女，55
        # 岁，手机号
        # 13800000006。
        try:
            with session.begin():
                singer__filter = select(Singer).filter(Singer.phone == '13800000007')
                singer__filter_result = session.scalars(singer__filter).first()
                if singer__filter_result:
                    print(f"手机号 {singer__filter_result.phone} 已存在")
                    raise Exception("数据插入失败")
                else:
                    session.add(Singer(name='王菲', gender='女', age=55, phone='13800000007'))
                    # 在插入后故意抛出一个异常：raise Exception("模拟出错")。
                    raise Exception("模拟出错")
        except Exception as e:
            print(f"数据插入失败，已回滚：{e}")
        # 查询所有歌手，打印验证“王菲”没有被插入。
        print("查询所有歌手，打印验证“王菲”没有被插入。")
        for singer in session.scalars(select(Singer)):
            print(singer)
    except Exception as e:
        session.rollback()
        print(f"数据插入失败，已回滚：{e}")
    finally:
        session.close()  # 确保会话关闭
        print("会话已关闭")

