import keyword

from .database import get_connection
from datetime import datetime


def create_task(title):
    now=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with get_connection() as conn:
        cursor=conn.execute(
            "INSERT INTO tasks (title,completed,created_at) VALUES(?,?,?)",
            (title,0,now)
        )
        conn.commit()
        return cursor.lastrowid
import inspect
print(">>> 实际调用的函数文件路径：", inspect.getfile(create_task))
print(">>> 实际调用的函数签名：", inspect.signature(create_task))
def get_all_tasks(page=1,limit=10,keyword=None,completed=None):
    offset=(page-1)*limit
    sql="SELECT*FROM tasks WHERE 1=1"
    params=[]

    if keyword:
        sql+=" AND title LIKE ?"#关键词搜索
        params.append(f"%{keyword}%")#模糊匹配
    if completed is not None:
        sql+=" AND completed =?"
        params.append(1 if completed else 0)
#分页和排序
    sql+="ORDER BY id DESC LIMIT ? OFFSET ?"#字符串拼接赋值，title字段模糊匹配某个值,ORDER BY id DESC倒序排序
    params.extend([limit,offset])

    with get_connection() as conn:
        rows=conn.execute(sql,params).fetchall()
        return [dict(row) for row in rows]#把row转为字典

def get_task_by_id(task_id):
    with get_connection() as conn:
        row=conn.execute("SELECT*FROM tasks WHERE id=?",(task_id,)).fetchone()#查寻id等于某个数的row
        return dict(row) if row else None

def update_task(task_id,title=None,completed=None):
    sql="UPDATE tasks SET"
    params=[]#为什么可以用两个params？因为作用域不同

    if title is not None:
        sql+="title=?"
        params.append(title)
    if completed is not None:
        sql+="completed=?"
        params.append(1 if completed else 0)#completed有值那么就执行
    if not params:#空的列表
        return False
    sql=sql.rstrip(",")+"WHERE id=?"
    params.append(task_id)
    with get_connection() as conn:
        cursor=conn.execute(sql,params)
        conn.commit()
        return cursor.rowcount>0
def delete_task(task_id):
    with get_connection() as conn:
        cursor=conn.execute("DELETE FROM tasks WHERE id=?",(task_id,))
        conn.commit()
        return cursor.rowcount>0





