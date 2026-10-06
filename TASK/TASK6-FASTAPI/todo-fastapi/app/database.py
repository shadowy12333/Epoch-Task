#SQLAlchemy：负责操作数据库，把 Python 对象映射成数据库表，帮你执行增删改查。
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
#declarative_base：定义数据库表的基类
#session maker：创建数据库会话的工厂
SQLALCHEMY_DATABASE_URL = "sqlite:///./todo_fastapi.db"#本地数据库
engine=create_engine(SQLALCHEMY_DATABASE_URL,connect_args={"check_same_thread":False})#连接 SQLite 数据库，并允许所有线程都能访问它
SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base=declarative_base()#？
def get_db():
    db=SessionLocal()
    try:
        yield db#把数据库会话 db 交给路由函数使用，等路由执行完（不管成功还是报错），再继续执行 finally 里的 db.close() 来释放连接。
    finally:
        db.close()