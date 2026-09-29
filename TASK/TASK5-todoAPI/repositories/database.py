import sqlite3
import os
DATABASE="todo.db"
def get_connection():
    conn=sqlite3.connect(DATABASE)
    conn.row_factory=sqlite3.Row#factory 是让每一行数据按我想要的形式返回，这里就是sqlite.3
    return conn

def init_db():#初始化数据库
    if not os.path.exists(DATABASE):
        print("数据不存在喵，等我初始化喵")
        with get_connection() as conn:
            with open("../todo-api/schema.sql", "r", encoding="utf-8") as f:
                conn.executescript(f.read())#excutescript执行多条sql

